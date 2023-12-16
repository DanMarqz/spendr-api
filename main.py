from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.controllers.home import router as home
from api.controllers.status import router as status
from api.controllers.transactions import router as transactions

app = FastAPI()

# CORS Integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(home)
app.include_router(status)
app.include_router(transactions)

if __name__ == "__main__":
    app.run(debug=True)
