from fastapi import FastAPI

app = FastAPI(debug=True)

from src.orders.api import api