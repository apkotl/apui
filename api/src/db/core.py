from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.config import DATABASE_CONFIG


engine = create_async_engine(DATABASE_CONFIG['url'])

AsyncSessionFactory = async_sessionmaker(engine, expire_on_commit=False)