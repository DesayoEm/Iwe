from fastapi import HTTPException
from typing import Optional
from schemas.users import User, UserCreate, UserUpdate
from data import users

class UserCrud:
    @staticmethod
    def get_users():
        return users

    @staticmethod
    def get_user(value: str) -> User:
        if not value:
            raise HTTPException(status_code=400,detail="Value cannot be empty")
        if value.isnumeric():
            value = int(value)
            user = next((user for user in users if user.id == value), None)
            if not user:
                raise HTTPException(status_code=404,detail=f"User with id {value} not found")
        else:
            value = value.strip().casefold()
            user = next((user for user in users if user.name.casefold() == value), None)
            if not user:
                raise HTTPException(status_code=404,detail=f"User with name '{value.title()}' not found")
        return user


    @staticmethod
    def create_user(user: UserCreate):
        new_user = User(id=len(user_crud.get_users()) + 1, **user.model_dump())
        users.append(new_user)
        return new_user

    @staticmethod
    def update_user(user: Optional[User], data: UserUpdate):
        if not user:
            raise HTTPException(
                status_code=404, detail="User not found"
            )
        user.username = data.username
        user.email = data.email
        user.name = data.name
        return user

    @staticmethod
    def delete_user(value: str):
        user = UserCrud.get_user(value)
        users.remove(user)
        return {"message": "User deleted"}

#
user_crud = UserCrud()
