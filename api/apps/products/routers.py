from typing import Optional, List
from fastapi import APIRouter, Depends

from .service import ProductsService, get_products_service
from . import schema

app = APIRouter(prefix='/api/products', tags=['Товары'])

@app.get(
        '/',
        summary='Список',
        response_model=List[schema.ProductInfo])
async def list(
    limit:int,
    service:ProductsService = Depends(get_products_service)
    ):
    return await service.get_list(limit)


@app.get(
        '/',
        summary='Item',
        response_model=List[schema.ProductInfo])
async def get_one(
    id:int,
    service:ProductsService = Depends(get_products_service)
    ):
    return await service.get_one(id)


@app.post('/', summary='Создание', status_code=201)
async def create(
    data:schema.ProductCreateUpdate,
    service:ProductsService = Depends(get_products_service)
    ):
    return await service.create(data)


@app.delete('/', summary='Удаление')
async def delete(
    id:int,
    service: ProductsService = Depends(get_products_service)
    ):
    return await service.delete(id)