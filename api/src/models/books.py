from sqlalchemy.orm import Mapped, mapped_column
from src.models.base import Base



class BookModel(Base):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[str]