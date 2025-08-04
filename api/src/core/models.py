import datetime

from sqlalchemy import String, Integer, text, DateTime
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


# OLD
class Base(DeclarativeBase):
    pass


# NEW
def pk_column() -> Mapped[int]:
    return mapped_column(Integer, primary_key=True)

def str_column(length: int = 256) -> Mapped[str]:
    return mapped_column(String(length))

def created_at_column() -> Mapped[datetime.datetime]:
    return mapped_column(
        DateTime(timezone=False),
        server_default=text("TIMEZONE('utc', now())")
    )

def updated_at_column() -> Mapped[datetime.datetime]:
    return mapped_column(
        DateTime(timezone=False),
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.now(datetime.UTC),
    )


class BaseOrm(DeclarativeBase):
    pass
    #type_annotation_map = {
    #    str_64: String(64)
    #}

    #repr_col_num = 3
    #repr_cols = tuple()

    #def __repr__(self):
    #    """Relationships не используются в repr(), т.к. могут вести к неожиданным подгрузкам"""
    #    cols = []
    #    for idx, col in enumerate(self.__table__.columns.keys()):
    #        if col in self.repr_cols or idx < self.repr_cols_num:
    #            cols.append(f"{col}={getattr(self, col)}")
    #
    #    return f"<{self.__class__.__name__} {', '.join(cols)}>"