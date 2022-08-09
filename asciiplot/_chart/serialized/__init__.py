from asciiplot._config import Config
from .layout_element_adding import add_layout_elements
from ..grid import ChartGrid


def render(chart_grid: ChartGrid, config: Config) -> str:
    return add_layout_elements(chart_grid.serialized(), chart_params=chart_grid.params, config=config)
