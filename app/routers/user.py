

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_users():
    return {"message": "Welcome to the User API"}


@router.get("/users")
def get_users():
    return {"message": "List of users"}