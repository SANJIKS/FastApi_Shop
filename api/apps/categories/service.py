from typing import Type
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from .models import Category
from apps.base_repo.base_class import BaseService
from config.settings import get_session

class CategoryService(BaseService[Category]):
    def __init__(self, db_session: Session):
        super(CategoryService,self).__init__(Category, db_session)


def get_category_service(db_session:AsyncSession = Depends(get_session)):
    return CategoryService(db_session)