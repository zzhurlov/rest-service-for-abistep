from app.exceptions.base import ApplicationException


class NegativeBalanceException(ApplicationException):
    @property
    def message(self):
        return f"Отсутствует достаточное кол-во денег"


class AttributeMustBeStrException(ApplicationException):
    @property
    def message(self):
        return f"Атрибут должен быть строкой"


class AttributeMustBeIntException(ApplicationException):
    @property
    def message(self):
        return f"Атрибут должен быть целым числом"


class NegativeAmountException(ApplicationException):
    @property
    def message(self):
        return f"Перевод должен быть положительным"


class InvalidCredentialsException(ApplicationException):
    @property
    def message(self):
        return f"Неверные данные создания пользователя"
