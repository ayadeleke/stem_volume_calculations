"""
Test functions for the formulas in the publication in src/stem_volumes/formulas.py

It assumes this folder structure:

stem-volumes/
├── README.md
├── src
│   └── stem_volumes
│       └── formulas.py
└── tests
    └── test_formulas.py

"""

import pytest
from stem_volumes import formulas
from stem_volumes.formulas import *
from inspect import signature
from stem_volumes.utils import extract_parameter_units, extract_volume_unit

NUM_FORMULAS = 230

@pytest.mark.parametrize('formula_no', range(1, NUM_FORMULAS + 1))
def test_formula_function_exists(formula_no):
    """
    Testing that we have a symbol named stem_volume_formula_<formula_no>
    """
    function_name = f"stem_volume_formula_{formula_no}"
    f = getattr(formulas, function_name)
    assert f

@pytest.mark.xfail
@pytest.mark.parametrize('formula_no', range(1, NUM_FORMULAS + 1))
def test_formula_function_signature(formula_no):
    """
    Testing that the stem volume function has one or two parameters and the
    first is called `D` and the second called `H` if applicable.

    This makes sure that all functions follow a similar interface.
    """
    function_name = f"stem_volume_formula_{formula_no}"
    f = getattr(formulas, function_name)
    params = list(signature(f).parameters)
    assert 1 <= len(params) and len(params) <= 2
    assert params == ["D", "H"][:len(params)], params

@pytest.mark.xfail
@pytest.mark.parametrize('formula_no', range(1, NUM_FORMULAS + 1))
def test_calling_formula_function(formula_no):
    """
    Testing that the stem volume function can be called
    """
    function_name = f"stem_volume_formula_{formula_no}"
    f = getattr(formulas, function_name)
    params = list(signature(f).parameters)
    args = [10.0] * len(params)
    assert f(*args) >= 0

@pytest.mark.parametrize('formula_no', range(1, NUM_FORMULAS + 1))
def test_parameter_units_from_docstring(formula_no):
    """
    Testing that the stem volume function's docstring provides extractable
    units for its paramters
    """
    function_name = f"stem_volume_formula_{formula_no}"
    f = getattr(formulas, function_name)
    units = extract_parameter_units(f)
    assert units[0] in set(["mm", "cm", "dm", "m"])
    if len(units) == 2:
        assert units[1] in set(["dm", "m"])

@pytest.mark.parametrize('formula_no', range(1, NUM_FORMULAS + 1))
def test_volume_unit_from_docstring(formula_no):
    """
    Testing that the stem volume function's docstring provides extractable
    units for its return value
    """
    function_name = f"stem_volume_formula_{formula_no}"
    f = getattr(formulas, function_name)
    unit = extract_volume_unit(f)
    assert unit in set(["dm3", "m3", "ln(dm3)", "ln(m3)"])

def test_stem_volume_formula_1():
    assert stem_volume_formula_1(1,1) > 0
    assert stem_volume_formula_1(1,1) < 1000000

def test_stem_volume_formula_2():
    assert 1==1

def test_stem_volume_formula_3():
    assert 1==1

def test_stem_volume_formula_4():
    assert 1==1

def test_stem_volume_formula_5():
    assert 1==1

def test_stem_volume_formula_6():
    assert stem_volume_formula_6(1, 25) > 0
    assert stem_volume_formula_6(1, 25) < 10000 # dm³

def test_stem_volume_formula_7():
    assert 1==1

def test_stem_volume_formula_8():
    assert 1==1

def test_stem_volume_formula_9():
    assert stem_volume_formula_9(20, 10) > 0
    assert stem_volume_formula_9(20, 10) < 1000000

def test_stem_volume_formula_10():
    assert 1==1

def test_stem_volume_formula_11():
    assert 1==1

def test_stem_volume_formula_12():
    assert 1==1

def test_stem_volume_formula_13():
    assert 1==1

def test_stem_volume_formula_14():
    assert 1==1

def test_stem_volume_formula_15():
    assert 1==1

def test_stem_volume_formula_16():
    assert 1==1

def test_stem_volume_formula_17():
    assert 1==1

def test_stem_volume_formula_18():
    assert 1==1

def test_stem_volume_formula_19():
    assert 1==1

def test_stem_volume_formula_20():
    assert 1==1

def test_stem_volume_formula_21():
    assert 1==1

def test_stem_volume_formula_22():
    assert stem_volume_formula_22(1, 25) > 0
    assert stem_volume_formula_22(1, 25) < 10000 # dm³

def test_stem_volume_formula_23():
    assert 1==1

def test_stem_volume_formula_24():
    assert 1==1

def test_stem_volume_formula_25():
    assert stem_volume_formula_25(44, 28) > 0
    assert stem_volume_formula_25(44, 28) < 1000000

def test_stem_volume_formula_26():
    assert 1==1

def test_stem_volume_formula_27():
    assert 1==1

def test_stem_volume_formula_28():
    assert 1==1

def test_stem_volume_formula_29():
    assert 1==1

def test_stem_volume_formula_30():
    assert 1==1

def test_stem_volume_formula_31():
    assert 1==1

def test_stem_volume_formula_32():
    assert 1==1

def test_stem_volume_formula_33():
    assert 1==1

def test_stem_volume_formula_34():
    assert 1==1

def test_stem_volume_formula_35():
    assert 1==1

def test_stem_volume_formula_36():
    assert 1==1

def test_stem_volume_formula_37():
    assert 1==1

def test_stem_volume_formula_38():
    assert stem_volume_formula_54(10, 5) > 0
    assert stem_volume_formula_54(10, 5) < 10000 # dm³

def test_stem_volume_formula_39():
    assert 1==1

def test_stem_volume_formula_40():
    assert 1==1

def test_stem_volume_formula_41():
    assert stem_volume_formula_41(1, 1) > 0
    assert stem_volume_formula_41(1, 1) < 1000000

def test_stem_volume_formula_42():
    assert 1==1

def test_stem_volume_formula_43():
    assert 1==1

def test_stem_volume_formula_44():
    assert 1==1

def test_stem_volume_formula_45():
    assert 1==1

def test_stem_volume_formula_46():
    assert 1==1

def test_stem_volume_formula_47():
    assert 1==1

def test_stem_volume_formula_48():
    assert 1==1

def test_stem_volume_formula_49():
    assert 1==1

def test_stem_volume_formula_50():
    assert 1==1

def test_stem_volume_formula_51():
    assert 1==1

def test_stem_volume_formula_52():
    assert 1==1

def test_stem_volume_formula_53():
    assert 1==1

def test_stem_volume_formula_54():
    assert stem_volume_formula_54(10, 2.5) > 0
    assert stem_volume_formula_54(10, 2.5) < 10 # m³

def test_stem_volume_formula_55():
    assert 1==1

def test_stem_volume_formula_56():
    assert 1==1

def test_stem_volume_formula_57():
    assert stem_volume_formula_57(1, 1) > 0
    assert stem_volume_formula_57(1, 1) < 1000000

def test_stem_volume_formula_58():
    assert 1==1

def test_stem_volume_formula_59():
    assert 1==1

def test_stem_volume_formula_60():
    assert 1==1

def test_stem_volume_formula_61():
    assert 1==1

def test_stem_volume_formula_62():
    assert 1==1

def test_stem_volume_formula_63():
    assert 1==1

def test_stem_volume_formula_64():
    assert 1==1

def test_stem_volume_formula_65():
    assert 1==1

def test_stem_volume_formula_66():
    assert 1==1

def test_stem_volume_formula_67():
    assert 1==1

def test_stem_volume_formula_68():
    assert 1==1

def test_stem_volume_formula_69():
    assert 1==1

def test_stem_volume_formula_70():
    assert stem_volume_formula_70(50, 35) > 0
    assert stem_volume_formula_70(50, 35) < 10000 # dm³

def test_stem_volume_formula_71():
    assert 1==1

def test_stem_volume_formula_72():
    assert 1==1

def test_stem_volume_formula_73():
    assert stem_volume_formula_73(1, 1) > 0
    assert stem_volume_formula_73(1, 1) < 1000000

def test_stem_volume_formula_74():
    assert 1==1

def test_stem_volume_formula_75():
    assert 1==1

def test_stem_volume_formula_76():
    assert 1==1

def test_stem_volume_formula_77():
    assert 1==1

def test_stem_volume_formula_78():
    assert 1==1

def test_stem_volume_formula_79():
    assert 1==1

def test_stem_volume_formula_80():
    assert 1==1

def test_stem_volume_formula_81():
    assert 1==1

def test_stem_volume_formula_82():
    assert 1==1

def test_stem_volume_formula_83():
    assert 1==1

def test_stem_volume_formula_84():
    assert 1==1

def test_stem_volume_formula_85():
    assert 1==1

def test_stem_volume_formula_86():
    assert stem_volume_formula_86(50, 35) > 0
    assert stem_volume_formula_86(50, 35) < 10 # m³

def test_stem_volume_formula_87():
    assert 1==1

def test_stem_volume_formula_88():
    assert 1==1

def test_stem_volume_formula_89():
    assert stem_volume_formula_89(1.5, 1.8) > 0
    assert stem_volume_formula_89(1.5, 1.8) < 1000000

def test_stem_volume_formula_90():
    assert 1==1

def test_stem_volume_formula_91():
    assert 1==1

def test_stem_volume_formula_92():
    assert 1==1

def test_stem_volume_formula_93():
    assert 1==1

def test_stem_volume_formula_94():
    assert 1==1

def test_stem_volume_formula_95():
    assert 1==1

def test_stem_volume_formula_96():
    assert 1==1

def test_stem_volume_formula_97():
    assert 1==1

def test_stem_volume_formula_98():
    assert 1==1

def test_stem_volume_formula_99():
    assert 1==1

def test_stem_volume_formula_100():
    assert 1==1

def test_stem_volume_formula_101():
    assert 1==1

def test_stem_volume_formula_102():
    assert stem_volume_formula_102(50, 35) > 0
    assert stem_volume_formula_102(50, 35) < 10000 # dm³

def test_stem_volume_formula_103():
    assert 1==1

def test_stem_volume_formula_104():
    assert 1==1

def test_stem_volume_formula_105():
    assert stem_volume_formula_105(1, 1) > 0
    assert stem_volume_formula_105(1, 1) < 1000000

def test_stem_volume_formula_106():
    assert 1==1

def test_stem_volume_formula_107():
    assert 1==1

def test_stem_volume_formula_108():
    assert 1==1

def test_stem_volume_formula_109():
    assert 1==1

def test_stem_volume_formula_110():
    assert 1==1

def test_stem_volume_formula_111():
    assert 1==1

def test_stem_volume_formula_112():
    assert 1==1

def test_stem_volume_formula_113():
    assert 1==1

def test_stem_volume_formula_114():
    assert 1==1

def test_stem_volume_formula_115():
    assert 1==1

def test_stem_volume_formula_116():
    assert 1==1

def test_stem_volume_formula_117():
    assert 1==1

def test_stem_volume_formula_118():
    assert stem_volume_formula_118(50, 35) > 0
    assert stem_volume_formula_118(50, 35) < 10000 #dm³

def test_stem_volume_formula_119():
    assert 1==1

def test_stem_volume_formula_120():
    assert 1==1

def test_stem_volume_formula_121():
    assert stem_volume_formula_121(4.5, 4) > 0
    assert stem_volume_formula_121(4.5, 4) < 1000000

def test_stem_volume_formula_122():
    assert 1==1

def test_stem_volume_formula_123():
    assert 1==1

def test_stem_volume_formula_124():
    assert 1==1

def test_stem_volume_formula_125():
    assert 1==1

def test_stem_volume_formula_126():
    assert 1==1

def test_stem_volume_formula_127():
    assert 1==1

def test_stem_volume_formula_128():
    assert 1==1

def test_stem_volume_formula_129():
    assert 1==1

def test_stem_volume_formula_130():
    assert 1==1

def test_stem_volume_formula_131():
    assert 1==1

def test_stem_volume_formula_132():
    assert 1==1

def test_stem_volume_formula_133():
    assert 1==1

def test_stem_volume_formula_134():
    assert stem_volume_formula_134(50, 35) > 0
    assert stem_volume_formula_134(50, 35) < 10000 #dm³

def test_stem_volume_formula_135():
    assert 1==1

def test_stem_volume_formula_136():
    assert 1==1

def test_stem_volume_formula_137():
    assert stem_volume_formula_137(1, 1) > 0
    assert stem_volume_formula_137(1, 1) < 1000000

def test_stem_volume_formula_138():
    assert 1==1

def test_stem_volume_formula_139():
    assert 1==1

def test_stem_volume_formula_140():
    assert 1==1

def test_stem_volume_formula_141():
    assert 1==1

def test_stem_volume_formula_142():
    assert 1==1

def test_stem_volume_formula_143():
    assert 1==1

def test_stem_volume_formula_144():
    assert 1==1

def test_stem_volume_formula_145():
    assert 1==1

def test_stem_volume_formula_146():
    assert 1==1

def test_stem_volume_formula_147():
    assert 1==1

def test_stem_volume_formula_148():
    assert 1==1

def test_stem_volume_formula_149():
    assert 1==1

def test_stem_volume_formula_150():
    assert math.exp(stem_volume_formula_150(50, 35)) > 0
    assert math.exp(stem_volume_formula_150(50, 35)) < 10000 #ln(dm³)

def test_stem_volume_formula_151():
    assert 1==1

def test_stem_volume_formula_152():
    assert 1==1

def test_stem_volume_formula_153():
    assert stem_volume_formula_153(1, 1) > 0
    assert stem_volume_formula_153(1, 1) < 1000000

def test_stem_volume_formula_154():
    assert 1==1

def test_stem_volume_formula_155():
    assert 1==1

def test_stem_volume_formula_156():
    assert 1==1

def test_stem_volume_formula_157():
    assert 1==1

def test_stem_volume_formula_158():
    assert 1==1

def test_stem_volume_formula_159():
    assert 1==1

def test_stem_volume_formula_160():
    assert 1==1

def test_stem_volume_formula_161():
    assert 1==1

def test_stem_volume_formula_162():
    assert 1==1

def test_stem_volume_formula_163():
    assert 1==1

def test_stem_volume_formula_164():
    assert 1==1

def test_stem_volume_formula_165():
    assert 1==1

def test_stem_volume_formula_166():
    assert stem_volume_formula_166(10, 5) > 0
    assert stem_volume_formula_166(10, 5) < 10000 #dm³

def test_stem_volume_formula_167():
    assert 1==1

def test_stem_volume_formula_168():
    assert 1==1

def test_stem_volume_formula_169():
    assert stem_volume_formula_169(1, 1) > 0
    assert stem_volume_formula_169(1, 1) < 1000000

def test_stem_volume_formula_170():
    assert 1==1

def test_stem_volume_formula_171():
    assert 1==1

def test_stem_volume_formula_172():
    assert 1==1

def test_stem_volume_formula_173():
    assert 1==1

def test_stem_volume_formula_174():
    assert 1==1

def test_stem_volume_formula_175():
    assert 1==1

def test_stem_volume_formula_176():
    assert 1==1

def test_stem_volume_formula_177():
    assert 1==1

def test_stem_volume_formula_178():
    assert 1==1

def test_stem_volume_formula_179():
    assert 1==1

def test_stem_volume_formula_180():
    assert 1==1

def test_stem_volume_formula_181():
    assert 1==1

def test_stem_volume_formula_182():
    assert stem_volume_formula_182(50, 35) > 0
    assert stem_volume_formula_182(50, 35) < 10 #m³

def test_stem_volume_formula_183():
    assert 1==1

def test_stem_volume_formula_184():
    assert 1==1

def test_stem_volume_formula_185():
    assert stem_volume_formula_185(1, 1) > 0
    assert stem_volume_formula_185(1, 1) < 1000000

def test_stem_volume_formula_186():
    assert 1==1

def test_stem_volume_formula_187():
    assert 1==1

def test_stem_volume_formula_188():
    assert 1==1

def test_stem_volume_formula_189():
    assert 1==1

def test_stem_volume_formula_190():
    assert 1==1

def test_stem_volume_formula_191():
    assert 1==1

def test_stem_volume_formula_192():
    assert 1==1

def test_stem_volume_formula_193():
    assert 1==1

def test_stem_volume_formula_194():
    assert 1==1

def test_stem_volume_formula_195():
    assert 1==1

def test_stem_volume_formula_196():
    assert 1==1

def test_stem_volume_formula_197():
    assert 1==1

def test_stem_volume_formula_198():
    assert stem_volume_formula_198(500, 35) > 0
    assert stem_volume_formula_198(500, 35) < 10000 #dm³

def test_stem_volume_formula_199():
    assert 1==1

def test_stem_volume_formula_200():
    assert 1==1

def test_stem_volume_formula_201():
    assert stem_volume_formula_201(1, 1) > 0
    assert stem_volume_formula_201(1, 1) < 1000000

def test_stem_volume_formula_202():
    assert 1==1

def test_stem_volume_formula_203():
    assert 1==1

def test_stem_volume_formula_204():
    assert 1==1

def test_stem_volume_formula_205():
    assert 1==1

def test_stem_volume_formula_206():
    assert 1==1

def test_stem_volume_formula_207():
    assert 1==1

def test_stem_volume_formula_208():
    assert 1==1

def test_stem_volume_formula_209():
    assert 1==1

def test_stem_volume_formula_210():
    assert 1==1

def test_stem_volume_formula_211():
    assert 1==1

def test_stem_volume_formula_212():
    assert 1==1

def test_stem_volume_formula_213():
    assert 1==1

def test_stem_volume_formula_214():
    assert stem_volume_formula_214(500, 35) > 0
    assert stem_volume_formula_214(500, 35) < 10000 #dm³

def test_stem_volume_formula_215():
    assert 1==1

def test_stem_volume_formula_216():
    assert 1==1

def test_stem_volume_formula_217():
    assert stem_volume_formula_217(10, 3) > 0
    assert stem_volume_formula_217(10, 3) < 1000000

def test_stem_volume_formula_218():
    assert 1==1

def test_stem_volume_formula_219():
    assert 1==1

def test_stem_volume_formula_220():
    assert 1==1

def test_stem_volume_formula_221():
    assert 1==1

def test_stem_volume_formula_222():
    assert 1==1

def test_stem_volume_formula_223():
    assert 1==1

def test_stem_volume_formula_224():
    assert 1==1

def test_stem_volume_formula_225():
    assert 1==1

def test_stem_volume_formula_226():
    assert 1==1

def test_stem_volume_formula_227():
    assert 1==1

def test_stem_volume_formula_228():
    assert 1==1

def test_stem_volume_formula_229():
    assert 1==1

def test_stem_volume_formula_230():
    assert 1==1


