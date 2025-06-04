"""Utility functions."""

from math import exp
import argparse
import inspect
import re
import os
import importlib.util
import pandas as pd
from collections import defaultdict
import numpy as np

import docstring_parser
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
    assert value_unit in set(['dm3', 'm3', 'ln(dm3)', 'ln(m3)'])

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
    df_filtered.ffill(inplace=True)
    df_filtered['species'] = df_filtered['species'].str.capitalize()

    return df_filtered


def extract_species_from_docstring(docstring: str) -> str:
    """
    Extracts the species name from a docstring by searching for the 'Species:' line.
    Returns the species string or an empty string if not found.
    """
    if not docstring:
        return ""
    match = re.search(r"Species\s*:? ?([^\n]+)", docstring)
    if match:
        return match.group(1).strip()
    return ""


def get_genus_from_docstring(docstring: str) -> str:
    """Extract genus from the docstring's species information.

    Args:
        docstring (str): The docstring of the function.

    Returns:
        str: The genus name extracted from the docstring, or None if not found.
    """
    # Use extract_species_from_docstring for matching
    match = re.search(r"Species:\s*(\w+)", docstring)
    if match:
        return match.group(1)
    return None


def match_species_names(df: pd.DataFrame) -> list:
    """
    Matches species names in the DataFrame column to genus_species_common_dict values.

    Returns:
    - list: A list of tuples (genus, species) for each row. If no match, (None, None).
    """
    matched = []
    for name in df['species']:
        found = False
        for genus, v in genus_species_common_dict.items():
            if name.lower() in [s.lower() for s in v["species"]]:
                matched.append((genus, name))
                found = True
                break
        if not found:
            matched.append((None, None))
    return matched


def match_genus_to_functions(genus_list: list, script_path: str) -> dict:
    """
    Match genus names from a list to functions with corresponding docstrings in the given Python script.
    Only include functions whose docstring species matches the 'formulas' list for that genus.

    Args:
        genus_list (list): List of genus names to match.
        script_path (str): Path to the Python script.

    Returns:
    dict: Dictionary with genus names as keys and lists of function names as values.
    """
    import os, importlib.util, inspect
    from .genus_dict import genus_species_common_dict

    script_path = os.path.abspath(script_path)
    module_name = os.path.splitext(os.path.basename(script_path))[0]

    try:
        spec = importlib.util.spec_from_file_location(module_name, script_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    except Exception as e:
        print(f"Error loading script: {e}")
        return {}

    function_dict = {}
    for genus in genus_list:
        allowed_species = set(genus_species_common_dict.get(genus, {}).get("formulas", []))
        function_dict[genus] = []
        for name, obj in inspect.getmembers(module, inspect.isfunction):
            docstring = inspect.getdoc(obj)
            if docstring:
                species = extract_species_from_docstring(docstring)
                if species in allowed_species:
                    function_dict[genus].append(name)
        if not function_dict[genus]:
            del function_dict[genus]
    return function_dict


def get_genus_row_map(genus_column: pd.Series) -> dict[str, np.ndarray]:
    """
    Builds a mapping of genus to the row indices where it occurs (even if in a list).
    Useful for applying formulas by genus without using groupby.
    """
    genus_map = defaultdict(list)
    for i, genus_list in enumerate(genus_column):
        if isinstance(genus_list, list):
            for genus in genus_list:
                genus_map[genus].append(i)
        elif genus_list is not None:
            # Handle single genus case
            genus_map[genus_list].append(i)
    return {g: np.array(idxs) for g, idxs in genus_map.items()}
