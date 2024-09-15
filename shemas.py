from pydantic import BaseModel, Field
from utils import create_unique_key


class Qr_code(BaseModel):
    name: str
    first_name: str
    patronymic: str 
    info: str 
    unique_key: str | None = "не заполняйте данную страку"