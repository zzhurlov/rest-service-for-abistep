import pytest
import asyncio
import pytest_asyncio
import aiosqlite
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

from app.models.users import User
from app.db.repositories.user import UserRepository

DATABASE_URL_TEST = "sqlite+aiosqlite:///:memory:"

Base = declarative_base()


@pytest_asyncio.fixture(scope="session")
def event_loop():
    """Создаём event loop для всех тестов."""
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="session")
async def async_engine():
    engine = create_async_engine(DATABASE_URL_TEST, echo=False)
    yield engine
    await engine.dispose()


@pytest_asyncio.fixture(scope="session", autouse=True)
async def setup_db(async_engine):
    """Создаём таблицы в тестовой БД перед тестами."""
    async with async_engine.begin() as conn:
        await conn.run_sync(User.metadata.create_all)
    yield
    async with async_engine.begin() as conn:
        await conn.run_sync(User.metadata.drop_all)


@pytest_asyncio.fixture
async def session(async_engine) -> AsyncSession:
    """Фикстура для новой сессии."""
    async_session = async_sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
