from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """Configuration environment variables"""
    mongo_url: str
    mongo_db_name: str
    mongo_collection_name: str

    model_config = SettingsConfigDict(env_file=".env")


config = Config()
