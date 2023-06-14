import os
from typing import Type
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from .models import Products
from apps.base_repo.base_class import BaseService
from config.settings import get_session
from utils.save_image import image_add_origin


class ProductsService(BaseService[Products]):
    def __init__(self, db_session: Session):
        super(ProductsService,self).__init__(Products, db_session)

    async def create(self, product):
        path_folder = 'static/images/products'
        if not os.exist(path_folder):
            os.mkdir(path_folder)
        
        path_image = image_add_origin(product.image, path_folder)

        async with self.db_session as session:
            new_product = self.table(
                name = product.name,
                image = product.image,
                article = product.article,
                price = product.price,
                body = product.body,
                category_it = product.category_id,
                brand_id = product.brand_id
            )

            await session.add(new_product)
            await session.commit()
    
        return new_product
    
    # def update(self, data):
    #     return await super().update(data)


def get_products_service(db_session:AsyncSession = Depends(get_session)):
    return ProductsService(db_session)