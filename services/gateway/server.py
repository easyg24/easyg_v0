import uvicorn

from decouple import config
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import Response


app = FastAPI()


@app.post("/")
async def plot_request(upload_file: UploadFile = File(...),
):
    return {"message": "test"}


def run():
    host = config("SERVER_HOST")
    port = config("SERVER_PORT", cast=int)
    log_level = config("SERVER_LOG_LEVEL")
    uvicorn.run("server:app", host=host, port=port, log_level=log_level, reload=True)


if __name__ == "__main__":
    run()
