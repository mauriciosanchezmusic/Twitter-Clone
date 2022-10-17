"""Repositories module."""

from contextlib import AbstractContextManager
from typing import Callable, Iterator

from sqlalchemy.orm import Session

from ..Model.models import User, Admin
from ..DTO.inputs import UserInput, AdminInput
from ..DTO.outputs import UserOutput, AdminOutput

class UserRepository:

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[UserOutput]:
        with self.session_factory() as session:
            query_user = session.query(User).all() 
            output = []
            for element in query_user: 
                output_user = UserOutput(user_name=element.user_name, age=element.age, name=element.name, gender=element.gender)
                output.append(output_user) 
            return output

    def get_by_id(self, user_id: int) -> UserOutput:
        with self.session_factory() as session:
            query_user = session.query(User).filter(User.id == user_id).first()
            if not query_user:
                raise UserNotFoundError(user_id)
            output_user = UserOutput(user_name=query_user.user_name, age=query_user.age, name=query_user.name, gender=query_user.gender)
            return output_user

    def add(self, user_input: UserInput) -> User:
        with self.session_factory() as session:
            user = User(
                user_name = user_input.user_name,
                hashed_password = user_input.hashed_password,
                is_active = user_input.is_active,
                age = user_input.age,
                name = user_input.name,
                gender = user_input.gender,
                )
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    def delete_by_id(self, user_id: int) -> None:
        with self.session_factory() as session:
            entity: User = session.query(User).filter(User.id == user_id).first()
            if not entity:
                raise UserNotFoundError(user_id)
            session.delete(entity)
            session.commit()

class AdminRepository:

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[AdminOutput]:
        with self.session_factory() as session:
            query_admin = session.query(Admin).all() 
            output= []
            for element in query_admin: 
                output_admin = AdminOutput(user_name=element.user_name)
                output.append(output_admin) 
            return output

    def get_by_id(self, admin_id: int) -> AdminOutput:
        with self.session_factory() as session:
            query_admin = session.query(Admin).filter(Admin.id == admin_id).first()
            if not query_admin:
                raise AdminNotFoundError(admin_id)
            output_admin = AdminOutput(user_name=query_admin.user_name)
            return output_admin

    def add(self, admin_input: AdminInput) -> Admin:
        with self.session_factory() as session:
            admin = Admin(
                user_name = admin_input.user_name,
                hashed_password = admin_input.hashed_password,
                is_active = admin_input.is_active,
                )
            session.add(admin)
            session.commit()
            session.refresh(admin)
            return admin

    def delete_by_id(self, admin_id: int) -> None:
        with self.session_factory() as session:
            entity: Admin = session.query(Admin).filter(Admin.id == admin_id).first()
            if not entity:
                raise AdminNotFoundError(admin_id)
            session.delete(entity)
            session.commit()


class NotFoundError(Exception):

    entity_name: str

    def __init__(self, entity_id):
        super().__init__(f"{self.entity_name} not found, id: {entity_id}")

class UserNotFoundError(NotFoundError):

    entity_name: str = "User"
    
class AdminNotFoundError(NotFoundError):

    entity_name: str = "Admin"
