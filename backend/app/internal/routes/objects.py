from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.package.database.tools import Database


router = APIRouter(prefix='/api/v1')
db = Database()


@router.get('/objects/')
def get_objects(active: bool | None = None, search: str | None = None):
    return db.get_objects(active, search)


@router.get('/objects/find/{text}')
def get_objects(text: str):
    return db.get_search_object(text=text)


@router.get('/financing/{id}')
def get_objects(id: int):
    return db.get_cash_object(id_object=id)
