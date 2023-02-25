from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.package.database.tools import Database


router = APIRouter(
    prefix='/api/v1/user'
)


@router.get('/set_user')
def set_user():

    return {
        'hello': 'world'
    }

@router.get('/get_user_file')
def get_user_file(data=Body()):

    return {
        'hello': 'world'
    }

@router.get('/get_users_list')
def get_users_list():

    return {
        'hello': 'world'
    }