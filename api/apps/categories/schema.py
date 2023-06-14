from typing import Optional
from pydantic import BaseModel

class CategoryCreateUpdate(BaseModel):
    id:Optional[int] = None
    slug:str
    name:str

    class config:
        orm_mode = True


class CategoryInfo(CategoryCreateUpdate):
    id:int