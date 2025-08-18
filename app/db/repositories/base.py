from abc import abstractmethod
from typing import Type, TypeVar, Generic

from app.db.base import Base


ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    @abstractmethod
    async def get(self): ...

    @abstractmethod
    async def create(self): ...
