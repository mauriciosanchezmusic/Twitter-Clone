"""Admin Endpoints module."""

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from ...containers import Container
from ...Controller.services import AdminService
from ...Controller.repositories import NotFoundError
from ...DTO.inputs import AdminInput
from pydantic import BaseModel

router = APIRouter()


########## Admins ########## ########## ########## ########## ########## ########## ########## ########## ########## 

@router.get("/admins")
@inject
def get_list(
        admin_service: AdminService = Depends(Provide[Container.admin_service]),
):
    return admin_service.get_admins()


@router.get("/admins/{admin_id}")
@inject
def get_by_id(
        admin_id: int,
        admin_service: AdminService = Depends(Provide[Container.admin_service]),
):
    try:
        return admin_service.get_admin_by_id(admin_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/admins", status_code=status.HTTP_201_CREATED)
@inject
def add(
        admin_input: AdminInput,
        admin_service: AdminService = Depends(Provide[Container.admin_service])
):
    return admin_service.create_admin(admin_input)


@router.delete("/admins/{admin_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def remove(
        admin_id: int,
        admin_service: AdminService = Depends(Provide[Container.admin_service]),
):
    try:
        admin_service.delete_admin_by_id(admin_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)