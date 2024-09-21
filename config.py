from pydantic_settings import SettingsConfigDict, BaseSettings

class Settings(BaseSettings):
    
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER:str
    DB_PASSWORD:str
    KEY_ID: str
    ACCESS_KEY: str
    
    @property
    def DATABASE_URL_ASYNC_PSYCOPG(self):
        
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        
    
    
    model_config = SettingsConfigDict(env_file=".env")
        
settings = Settings()    

# print(settings.KEY_ID)
# print(settings.ACCESS_KEY)
