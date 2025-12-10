from sorter import Sorter, SorterParametersError
from pytest import mark, raises


class TestSorter:
    @mark.parametrize(
        "width, height, length, mass, result",
        [
            (1, 1, 1, 1, "STANDARD"),
            (1_000_000, 1, 1, 1, "BULKY"),
            (1, 1_000_000, 1, 1, "BULKY"),
            (1, 1, 1_000_000, 1, "BULKY"),
            (100, 100, 100, 1, "BULKY"),
            (1, 1, 1, 20, "HEAVY"),
            (1, 1, 1, 50, "HEAVY"),
            (1, 1, 1, 19, "STANDARD"),
            (150, 1, 1, 1, "BULKY"),
            (1, 150, 1, 1, "BULKY"),
            (1, 1, 150, 1, "BULKY"),
            (149, 149, 1, 19, "STANDARD"),
            (1, 149, 149, 19, "STANDARD"),
            (149, 1, 149, 19, "STANDARD"),
            (100, 100, 100, 20, "REJECTED"),
            (1_000_000, 1, 1, 50, "REJECTED"),
            (1, 1_000_000, 1, 20, "REJECTED"),
            (1, 1, 1_000_000, 19, "BULKY"),
            (100, 100, 100, 21, "REJECTED"),
            (150, 1, 1, 20, "REJECTED"),
            (1, 150, 1, 30, "REJECTED"),
            (1, 1, 150, 50, "REJECTED"),
            (1.0, 1.0, 1.0, 1.0, "STANDARD"),
            (150.0, 1.0, 1.0, 1.0, "BULKY"),
            (1.0, 150.0, 1.0, 1.0, "BULKY"),
            (1.0, 1.0, 150.0, 1.0, "BULKY"),
            (1.0, 1.0, 1.0, 20.0, "HEAVY"),
            (100.5, 100.5, 100.5, 20.5, "REJECTED"),
        ],
    )
    def test_sorter(self, width, height, length, mass, result):
        sorter = Sorter()

        stack = sorter.sort(width, height, length, mass)

        assert stack == result

    @mark.parametrize(
        "width, height, length, mass",
        [
            (0, 1, 1, 1),
            (1, -1, 1, 1),
            (1, 1, 0, 1),
            (1, 1, 1, -5),
            ("a", 1, 1, 1),
            (1, None, 1, 1),
            (1, 1, "length", 1),
            (1, 1, 1, [20]),
        ],
    )
    def test_sorter_invalid_parameters(self, width, height, length, mass):
        sorter = Sorter()

        with raises(SorterParametersError) as e:
            sorter.sort(width, height, length, mass)

        assert str(e.value) == "All parameters must be positive numbers."
