from pydantic import BaseModel

class SupportDto(BaseModel):
    url: str
    text: str