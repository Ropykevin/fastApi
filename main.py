from typing import Union, List
from fastapi import FastAPI, HTTPException
from uuid import UUID
from models import User, Gender, Role, UpdateUser

app = FastAPI()

db: List[User] = [
    User(id=UUID("7db5558a-6e1f-438e-91b9-22b56d656b24"),
         first_name="Kevin)",
         middle_name="me",
         last_name="ropy",
         gender=Gender.male,
         roles=[Role.admin, Role.user]),
    User(id=UUID("f302a4e2-b16b-4786-85b0-831651ed54ef"),
         first_name="edna",
         middle_name="me",
         last_name="Khasoa",
         gender=Gender.female,
         roles=[Role.student])
]


@app.get("/")
async def read_root():
    return {"Hello": "Kevin"}


@app.get("/api/v1/users", response_model=List[User])
async def fetch_user():
    return db


@app.post("/api/v1/users", response_model=User)
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    # looping through users in db
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id:{user_id} does not exists"
    )


@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UpdateUser, user_id: UUID):
    for user in db:
        if user.id == user_id:
            user.first_name = user_update.first_name
            user.middle_name = user_update.middle_name
            user.last_name = user_update.last_name
            user.roles = user_update.roles
            
        return user
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    )
