from typing import Type
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from .models import Brand
from apps.base_repo.base_class import BaseService
from config.settings import get_session

class BrandService(BaseService[Brand]):
    def __init__(self, db_session: Session):
        super(BrandService,self).__init__(Brand, db_session)


def get_brand_service(db_session:AsyncSession = Depends(get_session)):
    return BrandService(db_session)