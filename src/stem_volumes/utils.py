"""Utility functions."""

import argparse
import functools  # Added for caching
import importlib.util
import inspect
import os
import re
from math import exp

import docstring_parser
import numpy as np
import pandas as pd

from stem_volumes.genus_dict import genus_species_common_dict


# --- Changed: cache parsed docstrings to avoid repeated parsing for the same function ---
@functools.lru_cache(maxsize=None)
def parse_docstring_cached(f):
    """Parses the docstring of the given function and caches the result."""
    return docstring_parser.parse(f.__doc__)


def extract_parameter_units(f):
    """Extracts the parameter units from the docstring of the given stem volume formula."""
    # Use cached docstring parse
    parsed_docstring = parse_docstring_cached(f)
    return [
        p.description.split('.')[0].split()[-1] for p in parsed_docstring.params
    ]


def extract_volume_unit(f):
    """Extracts the volume unit from the docstring of the given stem volume formula."""
    # Use cached docstring parse
    parsed_docstring = parse_docstring_cached(f)
    return parsed_docstring.returns.description.split('.')[0].split()[-1]


def convert_volume_to_m3(value, value_unit):
    """Converts the given value with given value unit to m3."""
    assert value_unit in set(['dm3', 'm3', 'ln(dm3)', 'ln(m3)'])

    if value_unit.startswith('ln('):
        value = np.exp(value)
        value_unit = value_unit[3:-1]

    if value_unit == 'dm3':
        value /= 1000

    return value


def clean_data(raw_df: pd.DataFrame):
    """Load and clean the dataset."""
    df_filtered = raw_df.copy()
    df_filtered.drop_duplicates(inplace=True)
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


def get_genus_row_map(genus_series):
    """Returns a dict mapping genus to list of row indices in the DataFrame."""
    genus_to_indices = {}
    for idx, genus in genus_series.items():
        if pd.isna(genus):
            continue
        genus_to_indices.setdefault(genus, []).append(idx)
    return genus_to_indices


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
