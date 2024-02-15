import io
import sys

import uvicorn
import PIL.Image as Image
from decouple import config
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse

sys.path.append("..\\services")
from plotter.plotter import build_graph
from plotter.models import Configurations


app = FastAPI()


@app.post("/", responses = {200:{"content": {"image/png": {}}}})
async def plot_request(
    file: UploadFile = File(...), 
    configs: Configurations = Configurations()):
    
    response = build_graph(file, configs)

    image = Image.open(io.BytesIO(response))
    image.save('.\\plotter\\tmp\\test.png')

    return FileResponse('.\\plotter\\tmp\\test.png')


def run():
    host = config("SERVER_HOST")
    port = config("SERVER_PORT", cast=int)
    log_level = config("SERVER_LOG_LEVEL")
    uvicorn.run("server:app", host=host, port=port, log_level=log_level, reload=True)


if __name__ == "__main__":
    run()
