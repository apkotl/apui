from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import (
    RolesOrm,
    UsersOrm,
    UsersInRolesOrm
)


async def insert_roles(session: AsyncSession):
    role = RolesOrm(name="admin", title="Admin")
    session.add(role)
    role = RolesOrm(name="user", title="User")
    session.add(role)
    role = RolesOrm(name="role_1", title="Role 1")
    session.add(role)
    role = RolesOrm(name="role_2", title="Role 2")
    session.add(role)
    role = RolesOrm(name="role_3", title="Role 3")
    session.add(role)
    await  session.commit()


async def insert_users(session: AsyncSession):
    await insert_roles(session)

    user = UsersOrm(email="apkotl@gmail.com", nickname="apkotl", first_name="Andrey", last_name="Kotlyarov")
    session.add(user)
    await  session.commit()
    users_in_roles = UsersInRolesOrm(user_id=user.id, role_id=1)
    session.add(users_in_roles)
    users_in_roles = UsersInRolesOrm(user_id=user.id, role_id=2)
    session.add(users_in_roles)
    await  session.commit()
    pass

