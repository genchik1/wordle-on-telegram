from environs import Env
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

env = Env()

POSTGRES_SERVER = env.str('POSTGRES_HOST', default='wordle_db')
POSTGRES_PORT = env.str('POSTGRES_PORT', default='5432')
POSTGRES_USER = env.str('POSTGRES_USER')
POSTGRES_PASSWORD = env.str('POSTGRES_PASSWORD')
POSTGRES_DB = env.str('POSTGRES_DB', default='wordle_db')

SQLALCHEMY_ORM_URL = (
    f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}'  # noqa: E501
)

engine = create_async_engine(
    SQLALCHEMY_ORM_URL,
    echo=False,
    future=True,
    pool_pre_ping=True,
    pool_recycle=3600,
    poolclass=NullPool,
)
async_session = async_sessionmaker(engine, expire_on_commit=False)

Base = declarative_base()


async def get_async_session() -> AsyncSession:
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()


async_test_session_marker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
test_session = async_test_session_marker()
