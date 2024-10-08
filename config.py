from pydantic_settings import SettingsConfigDict, BaseSettings

class Settings(BaseSettings):
    KEY_ID: str
    ACCESS_KEY: str
    
    
    model_config = SettingsConfigDict(env_file=".env")
        
settings = Settings()    

