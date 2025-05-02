import argparse
import inspect
import re
import os
import importlib.util

# Function to extract genus from the docstring
def get_genus_from_docstring(docstring: str) -> str:
    """Extract genus from the docstring's species information."""
    match = re.search(r"Species:\s*(\w+)", docstring)
    if match:
        return match.group(1)
    return None

def match_genus_to_functions(genus_list: list, script_path: str) -> dict:
    """Match genus names from a list to functions with corresponding docstrings in the given Python script."""
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

def main(genus_list, script_path):
    # If no genus list is provided, print all functions associated with all genus
    if genus_list:
        species_to_formula = match_genus_to_functions(genus_list, script_path)
    else:
        # If no genus list is provided, print all genus found in the script
        species_to_formula = match_genus_to_functions([], script_path)
    
    # Print the result
    print(species_to_formula)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Match genus names in functions to specific genus list in the script.")
    parser.add_argument('script_path', type=str, help="Path to the Python script file to be examined.")
    parser.add_argument('--genus', type=str, nargs='*', help="List of genus to filter the output (e.g. 'Abies', 'Pinus').")

    args = parser.parse_args()

    # Pass the script path and optional genus list to the main function
    main(args.genus, args.script_path)
