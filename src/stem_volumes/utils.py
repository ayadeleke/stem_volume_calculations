"""Utility functions."""

import importlib.util
import inspect
import os
import re
from collections import defaultdict
from math import exp

import docstring_parser
import numpy as np
import pandas as pd

from stem_volumes.genus_dict import genus_species_common_dict


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
    assert value_unit in {'dm3', 'm3', 'ln(dm3)', 'ln(m3)'}

    if value_unit.startswith('ln('):
        value = exp(value)
        value_unit = value_unit[3:-1]

    if value_unit == 'dm3':
        value /= 1000

    return value


def clean_data(raw_df: pd.DataFrame):
    """Load and clean the dataset.

    Args:
        raw_df (pd.DataFrame): Raw DataFrame to be cleaned.

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    df_filtered = raw_df.copy()
    df_filtered.drop_duplicates(inplace=True)
    # df_filtered.ffill(inplace=True)
    df_filtered['species'] = df_filtered['species'].str.capitalize()
    return df_filtered


def extract_species_from_docstring(docstring: str) -> str:
    """Extracts the species name from a docstring by searching for the 'Species:' line.

    Returns the species string or an empty string if not found.
    """
    if not docstring:
        return ''
    match = re.search(r'Species\s*:? ?([^\n]+)', docstring)
    return match.group(1).strip() if match else ''


def match_species_names(df: pd.DataFrame) -> list:
    """Matches species names in the DataFrame column to genus_species_common_dict values.

    Returns:
    - list: A list of tuples (genus, species) for each row. If no match, (None, None).
    """
    matched = []
    lowercase_species_dict = {
        genus: {s.lower() for s in data['species']}
        for genus, data in genus_species_common_dict.items()
    }

    for name in df['species']:
        lname = name.lower()
        match = next(
            (
                (genus, name)
                for genus, species_set in lowercase_species_dict.items()
                if lname in species_set
            ),
            None,
        )
        matched.append(match if match else (None, None))

    return matched
