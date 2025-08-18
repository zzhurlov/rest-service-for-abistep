class ApplicationException(BaseException):
    @property
    def message(self):
        return f"Ошибка приложения"


class ObjectDoesNotExist(ApplicationException):
    @property
    def message(self):
        return f"Обьект не найден"
