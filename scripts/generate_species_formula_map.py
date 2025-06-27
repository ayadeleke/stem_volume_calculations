"""Generate a mapping of common names to formula function names."""

from collections import defaultdict

from stem_volumes.genus_dict import genus_species_common_dict
from stem_volumes.genus_formula_map import genus_to_formulas

species_to_formulas = defaultdict(set)

for genus, info in genus_species_common_dict.items():
    formulas = genus_to_formulas.get(genus)
    if not formulas:
        continue  # Skip genera with no formulas
    for common_name in info.get('species', []):
        name = common_name.strip().lower()
        if name:
            species_to_formulas[name].update(formulas)  # Merge formulas

# Save to file
output_path = 'src/stem_volumes/species_to_formula_map.py'
with open(output_path, 'w', encoding='utf-8') as out:
    out.write(
        '# Auto-generated mapping of species names to formula function names\n'
    )
    out.write('species_to_formulas = {\n')
    for name in sorted(species_to_formulas):
        funcs = sorted(
            species_to_formulas[name]
        )  # Sort for readability/stability
        out.write(f'    "{name}": {funcs},\n')
    out.write('}\n')
