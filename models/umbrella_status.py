
from pydantic import BaseModel


class UmbrellaStatus(BaseModel):
    weather: str
    description: str
    temp: float
    feels_like: float
    bring_umbrella: bool
