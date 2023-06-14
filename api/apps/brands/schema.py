from typing import Optional
from pydantic import BaseModel

class BrandCreateUpdate(BaseModel):
    id:Optional[int] = None
    slug:str
    name:str

    class config:
        orm_mode = True


class BrandInfo(BrandCreateUpdate):
    id:int