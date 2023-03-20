from fastapi import FastAPI
from fastapi import Query
import pandas as pd


app = FastAPI()


@app.get("/")
def root():
    return {"PI-01 Laura Maita"}

@app.get("/get_max_duration/")
def get_max_duration(year:int= Query(None),platform:str= Query(None),duration_type:str= Query(None)):#Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN
    #import pandas as pd
    #import numpy as np
    
    if platform == 'netflix':
        inicioId = 'n'
    elif platform == 'hulu':
        inicioId = 'h'
    elif platform == 'disney':
        inicioId = 'd'
    elif platform == 'amazon':
        inicioId = 'a'
    elif platform is None:
        inicioId = None
    else:
        return 'no se encuentra plataforma, ingrear una de las opciones: netflix, hulu, disney o amazon'
    

    if duration_type == 'season':
        durationtype= 'season'
    elif duration_type == 'film':
        durationtype = 'min'
    else:
        return 'ingresar season o film en minuscula'


    df_plataformagral =  pd.read_csv('https://drive.google.com/file/d/1fu79gI8aJZA33_8KX-fvPZaGBImq1l1O/view?usp=share_link', delimiter=',', encoding='utf-8')

    if year and platform and  duration_type  is not None:

        filtro1= df_plataformagral[df_plataformagral.id.str.contains(inicioId) #filtro por primer letra de plataforma
                            & (df_plataformagral.release_year==year)  #filtro por el año
                            & (df_plataformagral.duration_type==durationtype) ] #filtro por la duracion
        max = filtro1['duration_int'].max()
        filtro2 = filtro1.query("duration_int==@max")
        pelicula = filtro2[['id','title', 'duration_int', 'duration_type']]

        if  not pelicula.empty:

            return (pelicula)
    
    elif year is None:
        
        if inicioId is None :
            
            filtro1= df_plataformagral[(df_plataformagral.duration_type==durationtype) ] #filtro por la duracion
            max = filtro1['duration_int'].max()
            filtro2 = filtro1.query("duration_int==@max")
            pelicula = filtro2[['title', 'duration_int', 'duration_type']]
            return print(pelicula)           
        
        filtro1= df_plataformagral[df_plataformagral['id'].str.contains(inicioId) #filtro por primer letra de plataforma
                            & (df_plataformagral.duration_type==durationtype) ] #filtro por la duracion
        max = filtro1['duration_int'].max()
        filtro2 = filtro1.query("duration_int==@max")
        pelicula = filtro2[['title', 'duration_int', 'duration_type']]
        return pelicula
                   
    elif inicioId is None :
        if durationtype is None:

            filtro1= df_plataformagral[(df_plataformagral.release_year==year)]#filtro por año                    
            max = filtro1['duration_int'].max()
            filtro2 = filtro1.query("duration_int==@max")
            pelicula = filtro2[['id','title', 'duration_int', 'duration_type']]
            return pelicula 
     
        filtro1= df_plataformagral[(df_plataformagral.release_year==year) #filtro por año
                                   & (df_plataformagral.duration_type==durationtype) ] #filtro por la duracion
        max = filtro1['duration_int'].max()
        filtro2 = filtro1.query("duration_int==@max")
        pelicula = filtro2[['id','title', 'duration_int', 'duration_type']]   
        return pelicula