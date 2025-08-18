from app.exceptions.base import ApplicationException


class NegativeBalanceException(ApplicationException):
    @property
    def message(self):
        return f"Отсутствует достаточное кол-во денег"
