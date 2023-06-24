import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from config.settings import get_session
from sqlalchemy.ext.asyncio import create_async_engine
from main import app
from apps.brands.models import Brand
from apps.brands.service import BrandService
from apps.brands.schema import BrandCreateUpdate

test_db_url = "postgresql+asyncpg://username:password@localhost:5432/test_db"
test_engine = create_async_engine(test_db_url)

@pytest.fixture(scope="module")
async def test_db_session():
    async with test_engine.begin() as conn:
        await conn.run_sync(Brand.metadata.drop_all)
        await conn.run_sync(Brand.metadata.create_all)
    
    async_session = AsyncSession(test_engine)
    yield async_session
    await async_session.close()

@pytest.fixture(scope="module")
async def test_app():
    app.dependency_overrides[get_session] = test_db_session
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        yield client

@pytest.mark.asyncio
async def test_create_brand(test_app: AsyncClient, test_db_session: AsyncSession):
    brand_service = BrandService(test_db_session)
    
    brand_data = {
        "slug": "test-brand",
        "name": "Test Brand"
    }
    
    response = await test_app.post("/api/brands/", json=brand_data)
    
    assert response.status_code == 201
    
    created_brand = await brand_service.get_one(response.json()["id"])
    assert created_brand.slug == brand_data["slug"]
    assert created_brand.name == brand_data["name"]
