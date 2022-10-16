"""Services module."""

from uuid import uuid4
from typing import Iterator

from .repositories import UserRepository, AdminRepository
from ..Model.models import User, Admin
from ..DTO.inputs import UserInput, AdminInput

class UserService:

    def __init__(self, user_repository: UserRepository) -> None:
        self._repository: UserRepository = user_repository

    def get_users(self) -> Iterator[User]:
        return self._repository.get_all()

    def get_user_by_id(self, user_id: int) -> User:
        return self._repository.get_by_id(user_id)

    def create_user(self,user_input : UserInput) -> User:
        return self._repository.add(user_input)

    def delete_user_by_id(self, user_id: int) -> None:
        return self._repository.delete_by_id(user_id)

class AdminService:

    def __init__(self, admin_repository: AdminRepository) -> None:
        self._repository: AdminRepository = admin_repository

    def get_admins(self) -> Iterator[Admin]:
        return self._repository.get_all()

    def get_admin_by_id(self, admin_id: int) -> Admin:
        return self._repository.get_by_id(admin_id)

    def create_admin(self,admin_input : AdminInput) -> Admin:
        return self._repository.add(admin_input)

    def delete_admin_by_id(self, admin_id: int) -> None:
        return self._repository.delete_by_id(admin_id)
