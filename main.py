import os

from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.transactions import router as transactions_router
from api.routes.transactions import router as expenses_router

app = FastAPI()

# CORS Integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return "spendr Api!"

app.include_router(transactions_router)
app.include_router(expenses_router)

if __name__ == "__main__":
    app.run(debug=True)
