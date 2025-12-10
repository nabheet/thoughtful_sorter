class SorterParametersError(ValueError):
    def __init__(self, message="All parameters must be positive numbers."):
        super().__init__(message)


class Sorter:
    def sort(self, width, height, length, mass):
        self._validate_parameters(width, height, length, mass)
        volume = width * height * length
        bulky = (
            True
            if volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
            else False
        )
        heavy = True if mass >= 20 else False
        if bulky and heavy:
            return "REJECTED"
        elif bulky:
            return "BULKY"
        elif heavy:
            return "HEAVY"
        else:
            return "STANDARD"

    def _validate_parameters(self, width, height, length, mass):
        if not all(
            isinstance(param, (int, float)) and param > 0
            for param in [width, height, length, mass]
        ):
            raise SorterParametersError("All parameters must be positive numbers.")
