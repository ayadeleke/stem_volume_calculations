def test_all_formulas_in_genus_map():
    from stem_volumes.genus_formula_map import genus_to_formulas

    # Collect all formulas from the mapping
    mapped_formulas = set()
    for formulas in genus_to_formulas.values():
        mapped_formulas.update(formulas)

    # All expected formulas
    expected_formulas = {f'stem_volume_formula_{i}' for i in range(1, 231)}

    missing = expected_formulas - mapped_formulas
    extra = mapped_formulas - expected_formulas

    assert not missing, (
        f'Missing formulas in genus_to_formulas: {sorted(missing)}'
    )
    assert not extra, (
        f'Unexpected formulas in genus_to_formulas: {sorted(extra)}'
    )
