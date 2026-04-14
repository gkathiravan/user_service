from fastapi import FastAPI, HTTPException

from db import init_db
from repository import create_new_user, get_user_by_id, list_all_users, search_users_by_name
from schemas import UserCreate

app = FastAPI(title="User Service", version="1.0.0")


@app.on_event("startup")
def startup() -> None:
    init_db()


@app.get("/")
def root() -> dict:
    return {"service": "user-service", "status": "ok"}


@app.get("/users/{user_id}")
def get_user(user_id: int) -> dict:
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get("/users")
def list_users() -> dict:
    return {"users": list_all_users()}


@app.get("/users/search")
def search_users(name: str) -> dict:
    matched_users = search_users_by_name(name)
    return {"users": matched_users, "count": len(matched_users)}


@app.post("/users")
def create_user(payload: UserCreate) -> dict:
    return create_new_user(payload.name)
