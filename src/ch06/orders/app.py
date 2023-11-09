from fastapi import FastAPI

app = FastAPI(debug=True)

from src.ch06.orders.api import api