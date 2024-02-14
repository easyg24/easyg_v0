from pydantic import BaseModel


class Configurations(BaseModel):
    title: str = "Title"
    xlabel: str = "x"
    ylabel: str = "y"
    grid: bool = True
    plot_color: str = "blue"

