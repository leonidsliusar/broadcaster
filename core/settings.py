from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='../.env', env_file_encoding='utf-8')

    OWNER_ID: str = 'itsmee_v,sliusar_leonid'
    MONGO_HOST: str = 'localhost'
    MONGO_PORT: int = 27017
    API_ID: int = 23128967
    API_HASH: str = '1768893f3990862c7ec4571227f32743'
    BOT_TOKEN: str = '6342844716:AAFLHrm6JivKEe9bbq4qpyyKTJBMdV_epPs'
    PHONE: str = '37120074619'
    PASSWORD: str = 'LXQp5Da2*'
    INTERFACE_API_TOKEN: str = '5948439917:AAG5yDvdFZtNtBg-TmB3lb7nBcJKZcjamcM'


settings = Settings()
