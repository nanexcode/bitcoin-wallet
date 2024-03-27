import plotext as plt
from textual.widgets import Static


class Graph(Static):


    def __init__(self) -> None:
        super().__init__()


    def render(self):
        plt.clf()
        plt.date_form("d/m/y H:M:S")
        plt.canvas_color((10, 14, 27))
        plt.axes_color((10, 14, 27))
        plt.ticks_color((133, 159, 213))
        plt.plotsize(self.size.width, self.size.height)