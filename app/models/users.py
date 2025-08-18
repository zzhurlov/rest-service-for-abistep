from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer


class User(Base):
    __tablename__ = "users"

    first_name: Mapped[str] = mapped_column(String(50), nullable=True)
    last_name: Mapped[str] = mapped_column(String(50), nullable=True)
    username: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    balance: Mapped[int] = mapped_column(Integer, nullable=False)
