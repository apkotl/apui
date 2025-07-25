from pydantic import BaseModel, ConfigDict


class NewBookSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    author: str


class BookSchema(NewBookSchema):
    id: int