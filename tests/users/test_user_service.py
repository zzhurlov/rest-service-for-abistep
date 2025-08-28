import pytest
from app.services.users import UserService
from app.exceptions.users import SameIdsException, NegativeBalanceException

user_service = UserService()


@pytest.mark.asyncio
async def test_get_users_empty(session):
    users = await user_service.get_users(session)
    assert users == []


@pytest.mark.asyncio
async def test_create_and_get_users(session):
    await user_service.create_user("John", "Doe", "johndoe", 100, session)
    await user_service.create_user("Alice", "Smith", "alicesmith", 200, session)

    users = await user_service.get_users(session)

    # assert len(users) == 2
    assert users[0].username == "johndoe"
    # assert users[1].balance == 200


# @pytest.mark.asyncio
# async def test_create_user_with_zero_balance(session):
#     await user_service.create_user("Zero", "Balance", "zerouser", 0, session)
#     users = await user_service.get_users(session)
#     assert users[0].balance == 0


# @pytest.mark.asyncio
# async def test_transfer_to_other_user(session):
#     await user_service.create_user("Bob", "Marley", "bob", 300, session)
#     await user_service.create_user("Charlie", "Brown", "charlie", 100, session)

#     users = await user_service.get_users(session)
#     from_user_id = users[0].id
#     to_user_id = users[1].id

#     await user_service.transfer_to_other_user(from_user_id, to_user_id, 50, session)

#     updated_users = await user_service.get_users(session)

#     sender = [u for u in updated_users if u.id == from_user_id][0]
#     recipient = [u for u in updated_users if u.id == to_user_id][0]

#     assert sender.balance == 250
#     assert recipient.balance == 150


# @pytest.mark.asyncio
# async def test_transfer_with_same_ids_raises(session):
#     await user_service.create_user("Eva", "Green", "eva", 500, session)

#     users = await user_service.get_users(session)
#     user_id = users[0].id

#     with pytest.raises(SameIdsException):
#         await user_service.transfer_to_other_user(user_id, user_id, 50, session)


# @pytest.mark.asyncio
# async def test_transfer_with_insufficient_balance_raises(session):
#     await user_service.create_user("Rich", "Guy", "rich", 10, session)
#     await user_service.create_user("Poor", "Guy", "poor", 100, session)

#     users = await user_service.get_users(session)
#     from_user_id = users[0].id
#     to_user_id = users[1].id

#     with pytest.raises(NegativeBalanceException):
#         await user_service.transfer_to_other_user(from_user_id, to_user_id, 50, session)
