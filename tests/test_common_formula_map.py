def test_all_species_and_formulas_mapped():
    from collections import defaultdict

    from stem_volumes.species_to_formula_map import species_to_formulas
    from stem_volumes.genus_dict import genus_species_common_dict
    from stem_volumes.genus_formula_map import genus_to_formulas

    # Common names to fully exclude (mapping + formula checks)
    full_exclusions = {
        'chestnut',
        'european crab apple',
        'european wild pear',
        'european yew',
    }

    # 1. Collect all expected common names (excluding full exclusions)
    expected_species = set()
    for genus_info in genus_species_common_dict.values():
        for name in genus_info.get('species', []):
            name = name.strip().lower()
            if name and name not in full_exclusions:
                expected_species.add(name)

    # 2. Collect all mapped species names (excluding full exclusions)
    mapped_species = {
        name
        for name in species_to_formulas.keys()
        if name not in full_exclusions
    }

    # 3. Check for missing and extra species names
    missing_names = expected_species - mapped_species
    extra_names = mapped_species - expected_species

    assert not missing_names, (
        f'Missing species names in mapping: {sorted(missing_names)}'
    )
    assert not extra_names, (
        f'Unexpected species names in mapping: {sorted(extra_names)}'
    )

    # 4. Build expected formula sets per species name (accumulating across all genera)
    expected_formula_map = defaultdict(set)
    for genus, genus_info in genus_species_common_dict.items():
        formulas = genus_to_formulas.get(genus, [])
        for name in genus_info.get('species', []):
            name = name.strip().lower()
            if name and name not in full_exclusions:
                expected_formula_map[name].update(formulas)

    # 5. Compare expected formulas with actual formulas
    for name in expected_formula_map:
        expected = expected_formula_map[name]
        actual = set(species_to_formulas.get(name, []))
        assert expected == actual, (
            f"Formulas for '{name}' do not match expected.\n"
            f'Expected: {sorted(expected)}\n'
            f'Got: {sorted(actual)}'
        )
