from pytest import approx
from stem_volumes.utils import convert_volume_to_m3
from math import log as ln, exp

def test_convert_volume_to_m3():
    assert convert_volume_to_m3(0.1, "m3") == 0.1
    assert convert_volume_to_m3(1, "m3") == 1
    assert convert_volume_to_m3(1000, "m3") == 1000

    assert convert_volume_to_m3(0.1, "dm3") == 0.1 / 1000
    assert convert_volume_to_m3(1, "dm3") == 1 / 1000
    assert convert_volume_to_m3(1000, "dm3") == 1000 / 1000

    assert convert_volume_to_m3(0.1, "ln(m3)") == exp(0.1)
    assert convert_volume_to_m3(1, "ln(m3)") == exp(1)
    assert convert_volume_to_m3(10, "ln(m3)") == exp(10)

    assert convert_volume_to_m3(ln(0.1), "ln(m3)") == approx(0.1)
    assert convert_volume_to_m3(ln(1), "ln(m3)") == 1
    assert convert_volume_to_m3(ln(1000), "ln(m3)") == approx(1000)

    assert convert_volume_to_m3(0.1, "ln(dm3)") == exp(0.1) / 1000
    assert convert_volume_to_m3(1, "ln(dm3)") == exp(1) / 1000
    assert convert_volume_to_m3(10, "ln(dm3)") == exp(10) / 1000

    assert convert_volume_to_m3(ln(0.1), "ln(dm3)") == approx(0.0001)
    assert convert_volume_to_m3(ln(1), "ln(dm3)") == 0.001
    assert convert_volume_to_m3(ln(1000), "ln(dm3)") == approx(1)
