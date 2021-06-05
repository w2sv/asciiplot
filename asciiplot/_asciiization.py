from typing import List, Sequence, Optional, Union

from asciiplot._config import Config
from asciiplot._sequences import stretched_sequences
from asciiplot._chart import ChartGrid, serialized


_DEFAULT_COLOR = 'WHITE'


def asciiize(
        *sequences: List[float],
        chart_height: int = 5,
        in_between_points_margin: int = 0,

        sequence_colors: Sequence[str] = tuple([_DEFAULT_COLOR]),
        label_color: str = _DEFAULT_COLOR,

        x_labels: Optional[Sequence[Optional[Union[str, float]]]] = None,
        y_label_decimal_places: int = 1,

        x_axis_description: str = '',
        y_axis_description: str = '',
        axis_description_color: str = _DEFAULT_COLOR,

        title: Optional[str] = None,
        title_color: str = _DEFAULT_COLOR,

        chart_indentation: int = 0,
        center_chart: bool = False) -> str:

    _raise_if_colors_exceeding_sequences(len(sequences), n_sequence_colors=len(sequence_colors))
    _raise_if_x_labels_exceeding_domain_of_definition(x_labels, domain_of_definition_length=max(map(len, sequences)))

    if in_between_points_margin:
        sequences = stretched_sequences(sequences, in_between_points_margin)  # type: ignore

    config = Config(
        chart_height,
        in_between_points_margin,
        sequence_colors,
        label_color,
        x_labels,
        y_label_decimal_places,
        x_axis_description,
        y_axis_description,
        axis_description_color,
        title,
        title_color,
        chart_indentation,
        center_chart
    )

    chart_grid = ChartGrid(config, sequences=sequences)
    return serialized.layout_element_containing(chart_grid.serialized(), config=config, chart_params=chart_grid.params)


def _raise_if_colors_exceeding_sequences(n_sequences: int, n_sequence_colors: int):
    if n_sequence_colors > n_sequences:
        raise ValueError('Number of passed sequence colors exceeding number of sequences')


def _raise_if_x_labels_exceeding_domain_of_definition(x_labels, domain_of_definition_length: int):
    if x_labels and len(x_labels) > domain_of_definition_length:
        raise ValueError(
            f"X-labels aren't matching determined domain of definition. Passed sequences comprise "
            f"{domain_of_definition_length} distinct x-values, passed {len(x_labels)} labels"
        )
