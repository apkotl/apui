from enum import Enum
from typing import Generic, TypeVar, Optional, List, Dict, Any
from pydantic import BaseModel, ConfigDict, Field, validator

from .models import ReadingLevel



class AuthorBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    first_name: str
    last_name: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int

class AuthorWithBooks(Author):
    books: list["Book"]



class BookGenreBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str

class BookGenreCreate(BookGenreBase):
    pass

class BookGenre(BookGenreBase):
    id: int



class BookBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    isbn: str
    author_id: int
    genre_id: int
    reading_level: ReadingLevel
    title: str
    publication_year: int
    volume: int | None

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

class BookWithObjects(Book):
    author: "Author"
    genre: "BookGenre"



class AuthorOrderBy(str, Enum):
    ID_ASC = "id_asc"
    ID_DESC = "id_desc"
    LAST_NAME_ASC = "last_name_asc"
    LAST_NAME_DESC = "last_name_desc"
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"


class BookGenreOrderBy(str, Enum):
    ID_ASC = "id_asc"
    ID_DESC = "id_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"


class BookOrderBy(str, Enum):
    ID_ASC = "id_asc"
    ID_DESC = "id_desc"
    TITLE_ASC = "title_asc"
    TITLE_DESC = "title_desc"
    AUTHOR_ASC = "author_asc"
    AUTHOR_DESC = "author_desc"
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"


class AuthorListQueryParams(BaseModel):
    """Параметры запроса для получения списка авторов"""
    offset: int = Field(default=0, ge=0, description="Смещение для пагинации")
    limit: int = Field(default=10, ge=1, le=100, description="Количество записей (максимум 100)")
    order_by: BookGenreOrderBy = Field(default=BookOrderBy.ID_ASC, description="Поле и направление сортировки")
    search: Optional[str] = Field(default=None, min_length=1, max_length=255, description="Поиск по имени или фамилии автора")

    @validator('search')
    def validate_search(cls, v):
        if v is not None:
            v = v.strip()
            if len(v) == 0:
                return None
        return v


class BookGenreListQueryParams(BaseModel):
    """Параметры запроса для получения списка жанров книг"""
    offset: int = Field(default=0, ge=0, description="Смещение для пагинации")
    limit: int = Field(default=10, ge=1, le=100, description="Количество записей (максимум 100)")
    order_by: BookGenreOrderBy = Field(default=BookOrderBy.ID_ASC, description="Поле и направление сортировки")
    search: Optional[str] = Field(default=None, min_length=1, max_length=255, description="Поиск по названию")

    @validator('search')
    def validate_search(cls, v):
        if v is not None:
            v = v.strip()
            if len(v) == 0:
                return None
        return v

class BookListQueryParams(BaseModel):
    """Параметры запроса для получения списка книг"""
    offset: int = Field(default=0, ge=0, description="Смещение для пагинации")
    limit: int = Field(default=10, ge=1, le=100, description="Количество записей (максимум 100)")
    order_by: BookGenreOrderBy = Field(default=BookOrderBy.ID_ASC, description="Поле и направление сортировки")
    search: Optional[str] = Field(default=None, min_length=1, max_length=255, description="Поиск по названию или автору")

    @validator('search')
    def validate_search(cls, v):
        if v is not None:
            v = v.strip()
            if len(v) == 0:
                return None
        return v