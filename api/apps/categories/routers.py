from typing import Optional, List
from fastapi import APIRouter, Depends

from .service import CategoryService, get_category_service
from . import schema

app = APIRouter(prefix='/api/categories', tags=['Категории'])

@app.get(
        '/',
        summary='Список',
        response_model=List[schema.CategoryInfo])
async def list(
    limit:int,
    service:CategoryService = Depends(get_category_service)
    ):
    return await service.get_list(limit)


@app.get(
        '/{id}',
        summary='Item',
        response_model=schema.CategoryInfo)
async def get_one(
    id:int,
    service:CategoryService = Depends(get_category_service)
    ):
    return await service.get_one(id)


@app.post('/{id}',summary='Создание', status_code=201)
async def create(
    data:schema.CategoryCreateUpdate,
    service:CategoryService = Depends(get_category_service)
    ):
    return await service.create(data)


@app.delete('/', summary='Удаление')
async def delete(
    id:int,
    service: CategoryService = Depends(get_category_service)
    ):
    return await service.delete(id)