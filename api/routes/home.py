import datetime
from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/")
def index():
    return JSONResponse({
        'Status': 'ok',
        'Name': 'Spendr!?',
        'Date': datetime.datetime.now()
    })