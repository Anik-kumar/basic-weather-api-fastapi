
import fastapi
from models.location import Location
from models.umbrella_status import UmbrellaStatus
from services import live_weather_service


router = fastapi.APIRouter()


@router.get("/api/weather", response_model=UmbrellaStatus)
async def do_i_need_an_umbrella(location: Location = fastapi.Depends()):

    result = await live_weather_service.get_live_weather(location)

    weather = result.get('weather', {})
    category = weather.get('category', 'None')
    description = weather.get('description', 'None')
    bring_umbrella = category.lower().strip() in {"rain", "haze"}

    forecast = result.get('forecast', {})
    temp = forecast.get('temp', 0.0)
    feels_like = forecast.get('feels_like', 0.0)

    # print(result)
    umbrella = UmbrellaStatus(
        bring_umbrella=bring_umbrella,
        temp=temp,
        weather=category,
        feels_like=feels_like,
        description=description
    )

    return umbrella
