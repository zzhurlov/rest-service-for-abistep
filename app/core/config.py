from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    api_port: int = 8000

    db_host: str
    db_port: int = 5432
    db_user: str
    db_pass: str
    db_name: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @property
    def db_uri(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"


settings = Settings()
