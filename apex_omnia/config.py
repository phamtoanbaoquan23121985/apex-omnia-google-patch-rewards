from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="", case_sensitive=False)
    APEX_MODE: str = "observe_only"
    APEX_TARGET_REPOSITORY: str = "protocolbuffers/protobuf"
    APEX_RESEARCH_ENABLED: bool = False
    PORT: int = 8080

settings = Settings()
