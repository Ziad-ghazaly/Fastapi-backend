from pydantic_settings import BaseSettings, SettingsConfigDict # type: ignore


class DataBaseSettings(BaseSettings):
    POSTGRESQL_USER : str 
    POSTGRESQL_PASSWORD : str
    POSTGRESQL_SERVER : str
    POSTGRESQL_PORT : str
    POSTGRESQL_DB : str
    
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True, extra="ignore")
    
settings = DataBaseSettings()

print(settings.POSTGRESQL_USER)
print(settings.POSTGRESQL_PASSWORD)


    
