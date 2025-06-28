from inspect import signature

import pandas as pd

from stem_volumes.__init__ import ALL_FORMULAS, calculate_stem_volumes
from stem_volumes.species_to_formula_map import species_to_formulas


def test_all_applicable_formulas_applied():
    # Build a DataFrame with one row for each species in the mapping
    data = []
    for species, formulas in species_to_formulas.items():
        for func_name in formulas:
            row = {
                'species': species,
                'diameter at breast height [mm]': 300,
                'height [dm]': 100,
            }
            params = None
            if func_name in ALL_FORMULAS:
                params = ALL_FORMULAS[func_name][0]
            else:
                try:
                    from stem_volumes import formulas as formula_mod

                    func = getattr(formula_mod, func_name)
                    params = tuple(signature(func).parameters)
                except Exception:
                    pass
            if params:
                if 'D' not in params:
                    row.pop('diameter at breast height [mm]')
                if 'H' not in params:
                    row.pop('height [dm]')
            data.append(row)
    df = pd.DataFrame(data)

    # Calculate volumes
    result_df = calculate_stem_volumes(df)

    # Check for each species that all mapped formulas have a corresponding column
    for species, formulas in species_to_formulas.items():
        norm_species = species.strip().lower()
        rows = result_df[
            result_df['species'].str.strip().str.lower() == norm_species
        ]
        assert not rows.empty, f"No rows found for species '{species}'"
        for func_name in formulas:
            colname = f'{func_name} [m3]'
            assert colname in result_df.columns, (
                f"Missing column {colname} for species '{species}'"
            )
            # Try vectorized check first, fallback to row-wise if needed
            try:
                # Vectorized: at least one value is not NA
                assert rows[colname].notna().any(), (
                    f"All values NA for {colname} in species '{species}'"
                )
            except Exception:
                # Row-wise fallback: check each row individually
                found = False
                for _, row in rows.iterrows():
                    if pd.notna(row[colname]):
                        found = True
                        break
                assert found, (
                    f"All values NA for {colname} in species '{species}' (row-wise checked)"
                )
