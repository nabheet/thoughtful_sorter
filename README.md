# thoughtful_sorter

Sorting library for Thoughtful's robot factory

The sort function implementation is in `sorter.py` file as the `sort` function of the `Sorter` class. This
function raises a custom exception `SorterParametersError` if the input paramters are not valid positive integers or floats.

Unit tests are in the `test_sorter.py` class.

## Run unit tests

This requires installation of two very popular python tools: `pyenv` and `pipenv`

```bash
pyenv install 3.13
pipenv install
pipenv run pytest
```
