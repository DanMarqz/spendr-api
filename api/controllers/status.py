from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/status")
def getStatus():
    return JSONResponse({
        'label': 'ok',
        'message': 'Budget Admin!?',
        'color': 'green'
    })