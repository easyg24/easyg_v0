import uvicorn

from pydantic import Json

from decouple import config
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import Response


def app():
    app = FastAPI()

    @app.post(
        "",
        responses={200: {"content": {"image/png": {}}}},
        response_class=Response,
    )
    async def plot_request(
        rawData: UploadFile = File(...),
    ):
        return {"message":"Hello World!"}

    return app


def run():
    host = config("SERVER_HOST")
    port = config("SERVER_PORT", cast=int)
    log_level = config("SERVER_LOG_LEVEL")
    uvicorn.run("server:app", host=host, port=port, log_level=log_level, reload=True)


if __name__ == "__main__":
    run()