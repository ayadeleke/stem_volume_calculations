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

def get_genus_from_docstring(docstring: str) -> str:
    """Extract genus from the docstring's species information.
    
    Args:
        docstring (str): The docstring of the function.

    Returns:
        str: The genus name extracted from the docstring, or None if not found.    
    """
    match = re.search(r"Species:\s*(\w+)", docstring)
    if match:
        return match.group(1)
    return None

def match_species_names(df: pd.DataFrame) -> list:    
    """
    Matches species names in the DataFrame column to species_dict values.
    
    Parameters:
    - df (pd.DataFrame): The DataFrame containing species names.
    
    Returns:
    - list: A list of matched species_dict keys (species codes). If no match, None is returned.
    """
    genus_species_common_dict = {

        "Abies": ["Abies alba", "Silver fir", "Abies grandis", "Grand fir", "Abies sibirica", "Fir", "Abies spp.", "Fir, Brad"],
        "Picea": ["Picea abies", "Norway spruce", "Picea sitchensis", "Sitka spruce", "Picea spp.", "Other spruces"],
        "Pinus": ["Pinus sylvestris", "Scots pine", "Pinus mugo", "Mountain pine", "Pinus nigra", "European black pine",
                  "Pinus cembra", "Swiss stone pine", "Pinus strobus", "Eastern white pine", "Pinus spp.", "Other pines"],
        "Pseudotsuga": ["Pseudotsuga menziesii", "Douglas fir"],
        "Larix": ["Larix decidua", "European larch", "Larix kaempferi", "Japanese larch"],
        "Taxus": ["Taxus baccata", "European yew"],
        "Chamaecyparis": ["Chamaecyparis lawsoniana", "Other coniferous trees"],
        "Thuja": ["Thuja plicata", "Other coniferous trees"],
        "Tsuga": ["Tsuga heterophylla", "Other coniferous trees"],
        "Fagus": ["Fagus sylvatica", "Beech", "Fagus spp.", "Misc. deciduous trees with long life expectancy"],
        "Quercus": ["Quercus robur", "English oak", "Quercus petraea", "Sessile oak", "Quercus rubra", "Northern red oak", "Misc. deciduous trees with long life expectancy"],
        "Fraxinus": ["Fraxinus excelsior", "Common ash", "Misc. deciduous trees with long life expectancy"],
        "Carpinus": ["Carpinus betulus", "Hornbeam", "Misc. deciduous trees with long life expectancy"],
        "Acer": ["Acer pseudoplatanus", "Sycamore maple", "Acer platanoides", "Norway maple", "Acer campestre", "Field maple", "Misc. deciduous trees with long life expectancy"],
        "Tilia": ["Tilia cordata", "Linden tree", "Tilia spp.", "Misc. deciduous trees with long life expectancy"],
        "Robinia": ["Robinia pseudoacacia", "Black locust", "Misc. deciduous trees with short life expectancy"],
        "Ulmus": ["Ulmus spp.", "Elm, native species", "Misc. deciduous trees with long life expectancy"],
        "Castanea": ["Castanea sativa", "Chestnut", "Castanea spp.", "Misc. deciduous trees with long life expectancy"],
        "Sorbus": ["Sorbus domestica", "Service tree", "Sorbus spp.", "Sorbus aria", "Common whitebeam", 
                "Sorbus aucuparia", "European rowan", "Sorbus torminalis", "Wild service tree", "Misc. deciduous trees with long life expectancy"],
        "Betula": ["Betula pendula", "Silver birch", "Betula pubescens", "Downy birch", "Misc. deciduous trees with short life expectancy"],
        "Alnus": ["Alnus glutinosa", "Black alder", "Alnus incana", "Grey alder"],
        "Populus": ["Populus tremula", "Common aspen", "Populus nigra", "European black poplar",
                    "Populus × canescens", "Grey poplar", "Populus alba", "Silver poplar", 
                    "Populus balsamifera", "Balsam poplar", "Misc. deciduous trees with short life expectancy"],
        "Salix": ["Salix spp.", "Willow", "Misc. deciduous trees with short life expectancy"],
        "Prunus": ["Prunus padus", "Bird cherry", "Prunus avium", "Wild cherry", "Prunus serotina", "Black cherry", "Misc. deciduous trees with short life expectancy"],
        "Malus": ["Malus sylvestris", "European crab apple", "Misc. deciduous trees with short life expectancy"],
        "Pyrus": ["Pyrus pyraster", "European wild pear", "Misc. deciduous trees with short life expectancy"],
        "Corylus": ["Corylus avellana", "Hazel", "Misc. deciduous trees with short life expectancy"]
    }

    matched_keys = []
    for name in df['species']:
        matched_genera = [
            genus for genus, species_list in genus_species_common_dict.items()
            if name in species_list
        ]
        matched_keys.append(matched_genera if matched_genera else None)

    return matched_keys



def match_genus_to_functions(genus_list: list, script_path: str) -> dict:
    """Match genus names from a list to functions with corresponding docstrings in the given Python script.
    
    Args:
        genus_list (list): List of genus names to match.
        script_path (str): Path to the Python script.
        
    Returns:
    dict: Dictionary with genus names as keys and lists of function names as values.
    """
    function_names = []
    genus_values = []

    # Ensure the absolute path to the script is used
    script_path = os.path.abspath(script_path)

    # Load the script as a module using importlib
    module_name = os.path.splitext(os.path.basename(script_path))[0]

    try:
        # Import the script dynamically as a module
        spec = importlib.util.spec_from_file_location(module_name, script_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Extract functions from the dynamically loaded module
        for name, obj in inspect.getmembers(module, inspect.isfunction):
            # Get the docstring
            docstring = inspect.getdoc(obj)
            if docstring:
                genus = get_genus_from_docstring(docstring)
                if genus:
                    function_names.append(name)
                    genus_values.append(genus)

    except Exception as e:
        print(f"Error loading script: {e}")
        return {}

    # Apply boolean indexing to filter functions by genus in genus_list
    function_dict = {}
    for genus, name in zip(genus_values, function_names):
        if genus in genus_list:
            if genus not in function_dict:
                function_dict[genus] = []
            function_dict[genus].append(name)
    
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
    return {g: np.array(idxs) for g, idxs in genus_map.items()}
