from asciiplot._chart import ChartGrid
from asciiplot._config import Config
from .layout_element_adding import layout_element_containing


def render(chart_grid: ChartGrid, config: Config) -> str:
    return layout_element_containing(chart_grid.serialized(), chart_params=chart_grid.params, config=config)
