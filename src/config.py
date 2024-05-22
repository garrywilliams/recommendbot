from pydantic_settings import BaseSettings, SettingsConfigDict

# Validate the environment variables
class Settings(BaseSettings):
    MEMBERS_URL: str
    JOBS_URL:str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()