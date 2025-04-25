import docstring_parser

def extract_parameter_units(f):
    """
    Extracts the parameter units from the docstring of the given stem volume
    formula

    Parameters:
        f: function to extract units from

    Returns:
        a list of the extracted units as strings, i.e., the last word in the
        description for each parameter
    """
    parsed_docstring = docstring_parser.parse(f.__doc__)
    return [p.description.split(".")[0].split()[-1] for p in parsed_docstring.params]

def extract_volume_unit(f):
    """
    Extracts the volume unit from the docstring of the given stem volume
    formula

    Parameters:
        f: function to extract units from

    Returns:
        the last word in the description of Returns
    """
    parsed_docstring = docstring_parser.parse(f.__doc__)
    return parsed_docstring.returns.description.split(".")[0].split()[-1]
