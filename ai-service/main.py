from fastapi import FastAPI
from pydantic import BaseModel
import random


app = FastAPI()


class Expense(BaseModel):
    amount: float
    description: str


@app.post("/predict")
def predict_category(expense: Expense):
    categories = ['food', 'transport', 'rent', 'entertainment', 'other']
    return {"category": random.choice(categories)}
