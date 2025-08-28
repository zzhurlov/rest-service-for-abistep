from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
import fastapi

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_async_session
from app.exceptions.base import ApplicationException
from app.schema.users import CreateUserSchema, TransferSchema
from app.services.users import user_service

user_router = APIRouter(tags=["users"])


@user_router.get("/users")
async def get_users_handler(
    session: Annotated[AsyncSession, Depends(get_async_session)],
):
    return await user_service.get_users(session=session)


@user_router.post("/users")
async def create_user_handler(
    schema: CreateUserSchema,
    session: Annotated[AsyncSession, Depends(get_async_session)],
):
    try:
        await user_service.create_user(
            first_name=schema.first_name,
            last_name=schema.last_name,
            username=schema.username,
            balance=schema.balance,
            session=session,
        )
    except ApplicationException as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail={"error": exception.message}
        )

    return {"message": "successful creation"}


@user_router.post("/transfer")
async def transfer_handler(
    schema: TransferSchema,
    session: Annotated[AsyncSession, Depends(get_async_session)],
):
    try:
        await user_service.transfer_to_other_user(
            schema.from_user_id, schema.to_user_id, schema.amount, session
        )
    except ApplicationException as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail={"error": exception.message}
        )

    return {"message": "successful transfer"}
