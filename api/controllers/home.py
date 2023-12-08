import datetime
from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/")
def index():
    return JSONResponse({
        'label': 'ok',
        'message': 'Budget Admin!?',
        'color': 'green',
        'Date': datetime.datetime.now().isoformat()
    })