

from fastapi import APIRouter

router = APIRouter()


@router.get("/users")
def get_users():
    users = {
        "users": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"},
            {"id": 3, "name": "Charlie"},
        ]   
    }
    return users


@router.post("/users")
def create_user(name: str):
    new_user = {"id": 4, "name": name}
    return new_user
