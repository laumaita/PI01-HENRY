from fastapi import FastAPI
from fastapi import Query
import pandas as pd


app = FastAPI()


@app.get("/")
def root():
    return {"PI-01 Laura Maita"}