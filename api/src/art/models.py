from sqlalchemy.orm import Mapped, mapped_column
from src.core.models import Base


### OLD
class BookModel(Base):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[str]



### NEW
import datetime
import enum

from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship


from src.core.models import (
    BaseOrm,
    pk_column,
    str_column,
    created_at_column,
    updated_at_column
)


class ReadingLevel(enum.Enum):
    Children = "Children"
    YoungAdult = "Young Adult"
    Adult = "Adult"
    AllAges = "All Ages"

    #def __str__(self) -> str:
    #    return self.value


class BookGenresOrm(BaseOrm):
    __tablename__ = 'book_genres'
    __table_args__ = {'schema': 'art'}

    id: Mapped[int] = pk_column()
    name: Mapped[str] = str_column(64)
    created_at: Mapped[datetime.datetime] = created_at_column()
    updated_at: Mapped[datetime.datetime] = updated_at_column()


class BooksOrm(BaseOrm):
    __tablename__ = 'books'
    __table_args__ = {'schema': 'art'}

    id: Mapped[int] = pk_column()
    isbn: Mapped[str] = mapped_column(unique=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("art.authors.id", ondelete="CASCADE"))
    genre_id: Mapped[int | None] = mapped_column(ForeignKey("art.book_genres.id", ondelete="SET NULL"))
    reading_level: Mapped[ReadingLevel] = mapped_column(Enum(ReadingLevel, schema='art', name='reading_level'))
    title: Mapped[str] = str_column()
    first_publication_year: Mapped[int]
    volume: Mapped[int | None]
    created_at: Mapped[datetime.datetime] = created_at_column()
    updated_at: Mapped[datetime.datetime] = updated_at_column()

    author: Mapped[list["AuthorsOrm"]] = relationship(
        back_populates="books",
    )

    genre: Mapped[list["BookGenresOrm"]] = relationship()




class AuthorsOrm(BaseOrm):
    __tablename__ = 'authors'
    __table_args__ = {'schema': 'art'}

    id: Mapped[int] = pk_column()
    first_name: Mapped[str] = str_column()
    last_name: Mapped[str] = str_column()
    created_at: Mapped[datetime.datetime] = created_at_column()
    updated_at: Mapped[datetime.datetime] = updated_at_column()

    books: Mapped[list["BooksOrm"]] = relationship(
        back_populates="author",
    )

    books_adult: Mapped[list["BooksOrm"]] = relationship(
        back_populates="author",
        primaryjoin="and_(AuthorsOrm.id == BooksOrm.author_id, BooksOrm.reading_level == 'Adult')",
        order_by="BooksOrm.id.desc()",
    )

