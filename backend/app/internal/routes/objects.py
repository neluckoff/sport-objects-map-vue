from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.package.database.tools import Database


router = APIRouter(prefix='/api/v1')
db = Database()


@router.get('/objects/open')
def get_objects():
    return db.get_online_objects()


@router.get('/objects/closed')
def get_objects():
    return db.get_offline_objects()


@router.get('/objects/find/{text}')
def get_objects(text: str):
    return db.get_search_object(text=text)


@router.get('/financing/{id}')
def get_objects(id: int):
    print(id)
    return db.get_cash_object(id_object=id)
