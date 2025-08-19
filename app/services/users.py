from app.db.repositories.user import UserRepository

from sqlalchemy.ext.asyncio import AsyncSession


class UserService:
    def __init__(self):
        self.repository = UserRepository()

    async def get_users(self, session: AsyncSession):
        users = await self.repository.get(session)
        return users

    async def create_user(
        self,
        first_name: str,
        last_name: str,
        username: str,
        balance: int,
        session: AsyncSession,
    ):
        await self.repository.create(first_name, last_name, username, balance, session)

    async def transfer_to_other_user(
        self, from_user_id: int, to_user_id: int, amount: int, session: AsyncSession
    ):
        await self.repository.transfer(from_user_id, to_user_id, amount, session)


user_service = UserService()
