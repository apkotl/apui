from typing import Annotated

from fastapi.params import Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from .config import settings



"""
db = "db"
if settings.APP_ENVIRONMENT == 'dev':
    db = f"{settings.NGINX_WEB_SERVER_NAME}"
"""
db = "db"
if not settings.DOCKER_CONTAINER_MODE:
    db = f"{settings.NGINX_WEB_SERVER_NAME}"


db_line = f"{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{db}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"

print("++++++++++++++++++++++++++++++++++++++")
print(f"{db_line=}")
print("++++++++++++++++++++++++++++++++++++++")

engine = create_async_engine(
    f"postgresql+asyncpg://{db_line}"
)

new_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_session():
    async with new_session() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


SessionDep = Annotated[AsyncSession, Depends(get_session)]




class Base(DeclarativeBase):
    pass

class BookModel(Base):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[str]




class BookAddSchema(BaseModel):
    title: str
    author: str



class BookSchema(BookAddSchema):
    id: int








async def setup_database(session:SessionDep):
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        """

    async  with session.bind.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)



    new_book = BookModel(
        title='Nineteen Eighty-Four',
        author='George Orwell',
    )
    session.add(new_book)
    new_book = BookModel(
        title='For Whom the Bell Tolls',
        author='Ernest Miller Hemingway',
    )
    session.add(new_book)
    await session.commit()






if __name__ == "__main__":
    print("debug")
    print(db_line)
    print(engine)