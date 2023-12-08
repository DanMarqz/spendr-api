import datetime
from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/status")
def index():
    return JSONResponse({
        'label': 'ok',
        'message': 'Budget Admin!?',
        'color': 'green'
    })