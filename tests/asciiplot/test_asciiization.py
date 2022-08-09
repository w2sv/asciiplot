from copy import deepcopy

from asciiplot import asciiize


def test_input_sequences_not_being_altered(sequences):
    copy = deepcopy(sequences)
    asciiize(*sequences, inter_points_margin=6)

    assert sequences == copy