from pydantic import BaseModel

class DataUserDto(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str
