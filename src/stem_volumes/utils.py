"""Utility functions."""

from math import exp

import docstring_parser


def extract_parameter_units(f):
    """Extracts the parameter units from the docstring of the given stem volume formula.

    Parameters:
        f: function to extract units from

    Returns:
        a list of the extracted units as strings, i.e., the last word in the
        description for each parameter
    """
    parsed_docstring = docstring_parser.parse(f.__doc__)
    return [
        p.description.split('.')[0].split()[-1] for p in parsed_docstring.params
    ]


def extract_volume_unit(f):
    """Extracts the volume unit from the docstring of the given stem volume formula.

    Parameters:
        f: function to extract units from

    Returns:
        the last word in the description of Returns
    """
    parsed_docstring = docstring_parser.parse(f.__doc__)
    return parsed_docstring.returns.description.split('.')[0].split()[-1]


def convert_volume_to_m3(value, value_unit):
    """Converts the given value with given value unit to m3.

    Parameters:
        value: representing the volume in the given unit
        value_unit: unit of the value

    Returns:
        the converted volume in m3
    """
    assert value_unit in set(['dm3', 'm3', 'ln(dm3)', 'ln(m3)'])

    if value_unit.startswith('ln('):
        value = exp(value)
        value_unit = value_unit[3:-1]

    if value_unit == 'dm3':
        value /= 1000

    return value

def get_genus_from_docstring(docstring: str) -> str:
    """Extract genus from the docstring's species information."""
    match = re.search(r"Species:\s*(\w+)", docstring)
    if match:
        return match.group(1)
    return None