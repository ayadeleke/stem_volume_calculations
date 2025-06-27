"""Generate a mapping of genera to their stem volume formula function names."""

import re
import string
from collections import defaultdict

formulas_path = 'src/stem_volumes/formulas.py'
output_path = 'src/stem_volumes/genus_formula_map.py'

# Import the known genera list
from stem_volumes.genus_dict import genus_species_common_dict

KNOWN_GENERA = set(genus_species_common_dict.keys())

genus_to_formulas = defaultdict(set)
species_to_formulas = defaultdict(set)


def normalize_species_name(name):
    """Normalize species names by removing parentheses and converting to lowercase."""
    return re.sub(r'\s*\(.*?\)', '', name).strip().lower()


with open(formulas_path, encoding='utf-8') as f:
    lines = f.readlines()

current_func = None
current_species = None

for i, line in enumerate(lines):
    # Detect function definition
    func_match = re.match(r'def (stem_volume_formula_\d+)\s*\(', line)
    if func_match:
        current_func = func_match.group(1)
        current_species = None
        # Look ahead for Species: in docstring
        for j in range(i + 1, min(i + 20, len(lines))):
            species_match = re.search(r'Species\s*:?\s*([^\n]*)', lines[j])
            if species_match:
                current_species = species_match.group(1).strip()
                break
        if current_species:
            # Some formulas have multiple species, split on common delimiters
            for sp in re.split(r',|;|/| and | & ', current_species):
                sp = sp.strip()
                if not sp:
                    continue
                # Extract genus as the first word before space or parenthesis
                raw_genus = sp.split()[0]
                genus = raw_genus.strip(string.punctuation + ' )(').capitalize()
                # Only add if genus is in the known genera list
                if genus in KNOWN_GENERA:
                    genus_to_formulas[genus].add(current_func)

# Write as Python dictionaries
with open(output_path, 'w', encoding='utf-8') as out:
    out.write('# Auto-generated mapping of genus to formula function names\n')
    out.write('genus_to_formulas = {\n')
    for genus, funcs in sorted(genus_to_formulas.items()):
        out.write(f'    "{genus}": {sorted(list(funcs))},\n')
    out.write('}\n\n')
