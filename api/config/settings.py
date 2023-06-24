from sqlalchemy.orm import DeclarativeBase, sessionmaker
from pydantic import BaseSettings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


class Settings(BaseSettings):
    bd_url: str = "postgresql+asyncpg://user:password@data_base:5432/database_name"


    class Config:
        env_file = ".env"
        env_file_ecnoding = "utf-8"

settings:Settings = Settings()


engine = create_async_engine(
    settings.bd_url
)

async def get_session():
    async_session = async_sessionmaker(engine, expire_on_commit=False)
    async with async_session() as session:
        yield session
        await session.close()

class Base(DeclarativeBase):
    pass