from pydantic_settings import BaseSettings, SettingsConfigDict

# Validate the environment variables (I don't usually do this, but it makes sense)
class Settings(BaseSettings):
    MEMBERS_URL: str
    JOBS_URL:str
    RECOMMENDATION_STRATEGY: str


    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()