import datetime
from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/")
def index():
    return JSONResponse({
        'Status': 'ok',
        'Name': 'Spendr or Budget Admin!?',
        'Date': datetime.datetime.now().isoformat()
    })