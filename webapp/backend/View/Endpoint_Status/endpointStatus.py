"""Status Endpoints module."""

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from ...containers import Container
from ...Controller.repositories import NotFoundError
from pydantic import BaseModel

router = APIRouter()

@router.get("/status")
def get_status():
    return {"status": "OK"}