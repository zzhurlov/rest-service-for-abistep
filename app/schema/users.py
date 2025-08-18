from pydantic import BaseModel

from app.models.users import User


class CreateUserSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    balance: int

    @classmethod
    def from_model(cls, user: User) -> "CreateUserSchema":
        return CreateUserSchema(
            first_name=user.first_name,
            last_name=user.last_name,
            username=user.username,
            balance=user.balance,
        )
