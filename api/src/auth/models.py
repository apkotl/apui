import datetime
import enum
from typing import List

from sqlalchemy import ForeignKey, Enum, Table, Column, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship


from src.core.models import (
    BaseOrm,
    pk_column,
    str_column,
    created_at_column,
    updated_at_column
)



class UsersOrm(BaseOrm):
    __tablename__ = "users"
    __table_args__ = {'schema': 'auth'}

    id: Mapped[int] = pk_column()
    email: Mapped[str] = str_column(128, unique=True)
    nickname: Mapped[str] = str_column(64, unique=True)
    is_active: Mapped[bool] = mapped_column(default=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    created_at: Mapped[datetime.datetime] = created_at_column()
    updated_at: Mapped[datetime.datetime] = updated_at_column()

    roles: Mapped[List["RolesOrm"]] = relationship(
        "RolesOrm",
        secondary=lambda: UsersInRolesOrm.__table__,
        primaryjoin=lambda: UsersOrm.id == UsersInRolesOrm.user_id,
        secondaryjoin=lambda: RolesOrm.id == UsersInRolesOrm.role_id,
        back_populates="users"
    )

    user_roles: Mapped[List["UsersInRolesOrm"]] = relationship(
        foreign_keys="UsersInRolesOrm.user_id",
        back_populates="user"
    )
    #user_roles: Mapped[List["UsersInRolesOrm"]] = relationship(
    #    back_populates="user",
    #    overlaps="roles"
    #)


class RolesOrm(BaseOrm):
    __tablename__ = "roles"
    __table_args__ = {'schema': 'auth'}

    id: Mapped[int] = pk_column()
    name: Mapped[str] = str_column(64, unique=True)
    title: Mapped[str]
    created_at: Mapped[datetime.datetime] = created_at_column()
    updated_at: Mapped[datetime.datetime] = updated_at_column()

    users: Mapped[List["UsersOrm"]] = relationship(
        "UsersOrm",
        secondary=lambda: UsersInRolesOrm.__table__,
        primaryjoin=lambda: RolesOrm.id == UsersInRolesOrm.role_id,
        secondaryjoin=lambda: UsersOrm.id == UsersInRolesOrm.user_id,
        back_populates="roles"
    )

    role_users: Mapped[List["UsersInRolesOrm"]] = relationship(
        foreign_keys="UsersInRolesOrm.role_id",
        back_populates="role"
    )
    #role_users: Mapped[List["UsersInRolesOrm"]] = relationship(
    #    back_populates="role",
    #    overlaps="users"
    #)


class UsersInRolesOrm(BaseOrm):
    __tablename__ = "users_in_roles"
    __table_args__ = {'schema': 'auth'}

    user_id: Mapped[int] = mapped_column(
        ForeignKey("auth.users.id"),
        primary_key=True
    )
    role_id: Mapped[int] = mapped_column(
        ForeignKey("auth.roles.id"),
        primary_key=True
    )

    #assigned_at: Mapped[datetime] = mapped_column(default=func.now())
    created_at: Mapped[datetime.datetime] = created_at_column()
    updated_at: Mapped[datetime.datetime] = updated_at_column()
    assigned_by: Mapped[int | None] = mapped_column(
        ForeignKey("auth.users.id"),
        nullable=True,
        default=None
    )


    assigner: Mapped["UsersOrm"] = relationship(
        foreign_keys=[assigned_by]
    )

    user: Mapped["UsersOrm"] = relationship(
        "UsersOrm",
        foreign_keys=[user_id],
        back_populates="user_roles"
    )
    role: Mapped["RolesOrm"] = relationship(
        "RolesOrm",
        foreign_keys=[role_id],
        back_populates="role_users"
    )



