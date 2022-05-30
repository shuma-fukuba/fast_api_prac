from operator import rshift
import re
from typing import List
from http.client import HTTPException
from urllib import response
from fastapi import APIRouter
from fastapi import Response, Request
from fastapi.encoders import jsonable_encoder
from schemas import Todo, TodoBody
from database import db_create_todo, db_get_todos
from starlette.status import HTTP_201_CREATED

router = APIRouter()


@router.post('/api/todo', response_model=Todo)
async def craete_todo(request: Request, response: Response, data: TodoBody):
    todo = jsonable_encoder(data)
    res = await db_create_todo(todo)
    response.status_code = HTTP_201_CREATED
    if res:
        return res
    raise HTTPException(
        status_code=404, detail="Create task failed"
    )


@router.get('/api/todo', response_model=List[Todo])
async def get_todos():
    res = await db_get_todos()
    return res


@router.get("/api/todo/{id}", response_model=Todo)
async def get_single_todo(id: str):
    res = await db_create_todo(id)
    if res:
        return res
    raise HTTPException(
        status_code=404, detail=f"task of Id: {id} doesn't exist"
    )
