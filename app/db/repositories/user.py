from sqlalchemy import insert, select, update
from app.db.repositories.base import BaseRepository
from app.exceptions.users import NegativeBalanceException
from app.models.users import User

from sqlalchemy.ext.asyncio import AsyncSession


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)

    async def get(self, session: AsyncSession):
        users = await session.scalars(select(User))
        return users.all()

    async def create(
        self,
        first_name: str,
        last_name: str,
        username: str,
        balance: int,
        session: AsyncSession,
    ):
        await session.execute(
            insert(User).values(
                first_name=first_name,
                last_name=last_name,
                username=username,
                balance=balance,
            )
        )
        await session.commit()

    def __validate_balance(self, sender_balance, amount):
        if amount > sender_balance:
            return False
        return True

    async def transfer(
        self, from_user_id: int, to_user_id: int, amount: int, session: AsyncSession
    ):
        sender = await session.scalar(select(User).where(User.id == from_user_id))
        recipient = await session.scalar(select(User).where(User.id == to_user_id))

        if not self.__validate_balance(sender.balance, amount):
            raise NegativeBalanceException

        async with session.begin():
            new_sender_balance = sender.balance - amount
            new_recipient_balance = recipient.balance + amount

            await session.execute(
                update(User)
                .where(User.id == from_user_id)
                .values(balance=new_sender_balance)
            )
            await session.execute(
                update(User)
                .where(User.id == to_user_id)
                .values(balance=new_recipient_balance)
            )
