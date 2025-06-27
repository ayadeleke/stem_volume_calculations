def test_all_common_names_and_formulas_mapped():
    from collections import defaultdict

    from stem_volumes.common_name_formula_map import common_name_to_formulas
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
    expected_common_names = set()
    for genus_info in genus_species_common_dict.values():
        for name in genus_info.get('species', []):
            name = name.strip().lower()
            if name and name not in full_exclusions:
                expected_common_names.add(name)

    # 2. Collect all mapped common names (excluding full exclusions)
    mapped_common_names = {
        name
        for name in common_name_to_formulas.keys()
        if name not in full_exclusions
    }

    # 3. Check for missing and extra common names
    missing_names = expected_common_names - mapped_common_names
    extra_names = mapped_common_names - expected_common_names

    assert not missing_names, (
        f'Missing common names in mapping: {sorted(missing_names)}'
    )
    assert not extra_names, (
        f'Unexpected common names in mapping: {sorted(extra_names)}'
    )

    # 4. Build expected formula sets per common name (accumulating across all genera)
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
        actual = set(common_name_to_formulas.get(name, []))
        assert expected == actual, (
            f"Formulas for '{name}' do not match expected.\n"
            f'Expected: {sorted(expected)}\n'
            f'Got: {sorted(actual)}'
        )
