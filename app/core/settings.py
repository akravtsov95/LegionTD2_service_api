from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "legion-proxy"
    env: str = "local"
    upstream_api_key: str


settings = Settings()