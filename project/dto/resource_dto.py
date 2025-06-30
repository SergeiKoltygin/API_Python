from pydantic import BaseModel
from typing import List

from .data_user_dto import DataUserDto
from .support_dto import SupportDto

class ResourceDto(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[DataUserDto]
    support: SupportDto