from pydantic import BaseModel


class NewBookSchema(BaseModel):
    title: str
    author: str


class BookSchema(NewBookSchema):
    id: int