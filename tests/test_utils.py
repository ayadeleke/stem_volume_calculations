from math import exp
from math import log as ln

from pytest import approx

from stem_volumes.utils import (
    convert_volume_to_m3,
    extract_species_from_docstring,
)


def test_convert_volume_to_m3():
    assert convert_volume_to_m3(0.1, 'm3') == 0.1
    assert convert_volume_to_m3(1, 'm3') == 1
    assert convert_volume_to_m3(1000, 'm3') == 1000

    assert convert_volume_to_m3(0.1, 'dm3') == 0.1 / 1000
    assert convert_volume_to_m3(1, 'dm3') == 1 / 1000
    assert convert_volume_to_m3(1000, 'dm3') == 1000 / 1000

    assert convert_volume_to_m3(0.1, 'ln(m3)') == exp(0.1)
    assert convert_volume_to_m3(1, 'ln(m3)') == exp(1)
    assert convert_volume_to_m3(10, 'ln(m3)') == exp(10)

    assert convert_volume_to_m3(ln(0.1), 'ln(m3)') == approx(0.1)
    assert convert_volume_to_m3(ln(1), 'ln(m3)') == 1
    assert convert_volume_to_m3(ln(1000), 'ln(m3)') == approx(1000)

    assert convert_volume_to_m3(0.1, 'ln(dm3)') == exp(0.1) / 1000
    assert convert_volume_to_m3(1, 'ln(dm3)') == exp(1) / 1000
    assert convert_volume_to_m3(10, 'ln(dm3)') == exp(10) / 1000

    assert convert_volume_to_m3(ln(0.1), 'ln(dm3)') == approx(0.0001)
    assert convert_volume_to_m3(ln(1), 'ln(dm3)') == 0.001
    assert convert_volume_to_m3(ln(1000), 'ln(dm3)') == approx(1)


def test_extract_species_from_docstring():
    docstring1 = """
    Calculates the volume of the stem of a standing tree.

    Species: Picea abies (Norway spruce, Kuusi, Gran, Epicéa, Fijnspar)
    Country: Finland

    Args:
        D: Diameter at breast height in cm.

    Returns:
        V: The calculated stem volume in ln(dm3).
    """
    docstring2 = """
    Some intro text.

    Species : Abies alba
    Country: Germany
    """
    docstring3 = """
    No species line here.
    """
    assert (
        extract_species_from_docstring(docstring1)
        == 'Picea abies (Norway spruce, Kuusi, Gran, Epicéa, Fijnspar)'
    )
    assert extract_species_from_docstring(docstring2) == 'Abies alba'
    assert extract_species_from_docstring(docstring3) == ''
