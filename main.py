
import fastapi
import uvicorn
from views import home
from api import weather


app = fastapi.FastAPI()


def configure():
    app.include_router(home.router)
    app.include_router(weather.router)


configure()
if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)


