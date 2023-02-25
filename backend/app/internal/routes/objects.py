from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.package.database.tools import Database


router = APIRouter(prefix='/api/v1')
db = Database()

@router.get('/objects')
def get_objects():
    return db.get_objects()
