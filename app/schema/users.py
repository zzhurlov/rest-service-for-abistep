from pydantic import BaseModel, Field, field_validator

from app.exceptions.users import NegativeAmountException, NegativeBalanceException


class CreateUserSchema(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    username: str = Field(..., min_length=3, max_length=30)
    balance: int

    @field_validator("balance")
    def balance_must_be_positive(cls, value: int):
        if value < 0:
            raise NegativeBalanceException
        return value


class TransferSchema(BaseModel):
    from_user_id: int
    to_user_id: int
    amount: int

    @field_validator("amount")
    def amount_must_be_positive(cls, value: int):
        if value < 0:
            raise NegativeAmountException
        return value
