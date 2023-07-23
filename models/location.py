from pydantic import BaseModel
from typing import Optional


class Location(BaseModel):
    city: str
    country: str = "us"
    state: Optional[str] = None
