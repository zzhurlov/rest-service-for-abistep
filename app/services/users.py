from app.db.repositories.user import UserRepository
from app.exceptions.users import InvalidCredentialsException, NegativeAmountException

from sqlalchemy.ext.asyncio import AsyncSession


class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def validate_credentials(
        self,
        first_name: str,
        last_name: str,
        username: str,
        balance: int,
    ):
        if not isinstance(first_name, str):
            return False

        if not isinstance(last_name, str):
            return False

        if not isinstance(username, str):
            return False

        if not isinstance(balance, int):
            return False

        if balance < 0:
            return False

    def validate_amount(self, amount):
        if amount < 0:
            return False
        return True

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
        # if not self.validate_credentials(first_name, last_name, username, balance):
        #     raise InvalidCredentialsException

        user = await self.repository.create(
            first_name, last_name, username, balance, session
        )

        return user

    async def transfer_to_other_user(
        self, from_user_id: int, to_user_id: int, amount: int
    ):
        if not self.validate_amount(amount):
            raise NegativeAmountException
        await self.repository.transfer(from_user_id, to_user_id, amount)


user_service = UserService()
