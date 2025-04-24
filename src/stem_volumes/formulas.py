"""
This module implements the 230 stem volume formulas from Silva Fennica by
Zianis et al.

The different formulas are based on Appendix B (starting on page 44) and
Appendix C (starting page 52) of the monograph. It can be downloaded at
https://doi.org/10.14214/sf.sfm4.
"""

import math

def stem_volume_formula_1(D, H, a=1.6662, b=3.2394, c=1.9335, d=-1.8997, e=-0.9739):
    # Volume calculation formula for Silver fir from Norway.
        V = a * H**b * D**c * (H - 1.3)**d * (D + 100)**e
        return V
# Rogy equation
def stem_volume_formula_2(D, H):
     # Coefficients
    a = 1.77220
    b = 0.96736
    c = -2.45224

    V = (D ** a) * (H ** b) * math.exp(c) # Formula - Abies grandis (Grand fir)(Netherland)
    return V

def stem_volume_formula_3():
    pass

# Theos equation
def stem_volume_formula_4(D):
    # Coefficients
    a = 0.0001316
    b = 2.52
    
    # Formula - Abies sibirica (Germany)
    V = a*D**b 
    return V

def stem_volume_formula_5(D, H):

    # Reference: Pollanschütz, J. 1974. Formzahlfunktionen der Hauptbaumarten Österreichs. Allgemeine Forstzeitung 85: 341–343.
    # for Abies spp. (Fir, Brad), from Austria
    # input: diameter D in dm, height H in dm
    # output: volume in dm³
    
    import math

    # define parameters
    a = 0.580223
    b = -0.0307373
    c = -17.1507
    d = 0.089869
    e = -0.080557
    f = 19.661
    g = -2.4584

    # implement formula
    V = (math.pi/4)*(a*D**2*H+b*D**2*H*math.log(D)**2+c*D**2+d*D*H+e*H+f*D+g)
    return V

def stem_volume_formula_6(D, H):
    
    # Coefficients
    a = 0.560673
    b = 0.15468
    c = -0.65583
    d = 0.033210
    
    # Equation / D[dm], H[dm], V[dm3]
    V = (math.pi/4) * (a * D**2 * H + b * D**2 * H * math.log(D)**2 + c * D**2 + d * D * H)
    
    return V

def stem_volume_formula_7():
    pass

def stem_volume_formula_8():
    pass

def stem_volume_formula_9(D, H):  # V = m3, D = cm, H = m
    a = 0.010343
    b = -0.00450536
    c = 0.0003407
    d = -0.000004042
    e = 0.00077115
    f = 0.000029836
    
    V = a+b*D+c*D**2+d*D**3+e*H+f*D**2*H

    return V # test successful

def stem_volume_formula_10():
    pass

# Acer pseudoplatanus - Romania
def stem_volume_formula_11(D, H):
    # Import math functions for the logarithm
    import math
    a = 0.00035375
    b = 1.02
    c = 0.3997
    d = 0.666
    e = 0.021
    math.exp(c)
    # Calculate the volume according to the formula given by Zianis et al.
    V = a * 10**(b * math.log10(D) + c * math.log10(D)**2 + d * math.log10(H) + e * math.log10(H)**2)
    # Return the calculated volume
    return V

def stem_volume_formula_12():
    pass

def stem_volume_formula_13():
    pass

def stem_volume_formula_14():
    pass

def stem_volume_formula_15():
    pass

def stem_volume_formula_16(D, H):
    
    # coefficients
    a = 0.6716
    b = 0.75708
    c = 0.029679
    d = 0.004341
    
    # equation / D=cm, H=m, 
    V = a + b * D**2 + c * D**2 * H + d + H**2 * D

    # V=dm³
    return V

def stem_volume_formula_17():
    pass

     #rogy equation
def stem_volume_formula_18(D,H):
   
    a=0.05437
    b=1.94505
    c=0.92947
    v = a * (D**b) * (H**c)  #Alnus glutinosa (Black alder, Klibbal)(Sweden)
    return v
def stem_volume_formula_19():
    pass

def stem_volume_formula_20():
    pass

def stem_volume_formula_21():
    pass

def stem_volume_formula_22():
    pass

def stem_volume_formula_23():
    pass

def stem_volume_formula_24():
    pass

def stem_volume_formula_25():
    pass

def stem_volume_formula_26():
    pass

def stem_volume_formula_27():
    pass

def stem_volume_formula_28():
    pass

def stem_volume_formula_29():
    pass

def stem_volume_formula_30():
    pass

def stem_volume_formula_31():
    pass

def stem_volume_formula_32():
    pass

def stem_volume_formula_33():
    pass
    #rogy equation
def stem_volume_formula_34(D,H):
    a=-0.89359
    b=2.27954
    c=-1.18672
    d=7.07362
    e=-5.45175
    v= (10**a)* (D**b)* ((D*20)**c) * (H**d) * ((H-1.3)**e)
    #Betula spp. (Birch, Björk, Bjørk, Bouleaux, Mesteacan)(sweeden)
    return v




def stem_volume_formula_35():
    pass

def stem_volume_formula_36():
    pass

def stem_volume_formula_37():
    pass

def stem_volume_formula_38():
    pass

def stem_volume_formula_39():
    pass

def stem_volume_formula_40():
    pass

def stem_volume_formula_41():
    pass

def stem_volume_formula_42():
    pass

def stem_volume_formula_43():
    pass

def stem_volume_formula_44():
    pass

def stem_volume_formula_45():
    pass

def stem_volume_formula_46():
    pass

def stem_volume_formula_47():
    pass

def stem_volume_formula_48():
    pass

def stem_volume_formula_49():
    pass
 #rogy equation
def stem_volume_formula_50(D,H):
    a=-15.589e-3
    b=0.01696e-3
    c=0.01883e-3
    v= a * b * D * (H**2) +c * (D**3)
    #BFagus sylvatica (Beech, Rotbuche, Beuk)(Germany)
    return v

def stem_volume_formula_51():
    pass

def stem_volume_formula_52():
    pass

def stem_volume_formula_53():
    pass

def stem_volume_formula_54():
    pass

def stem_volume_formula_55():
    pass

def stem_volume_formula_56():
    pass

def stem_volume_formula_57():
    pass

def stem_volume_formula_58():
    pass

def stem_volume_formula_59():
    pass

def stem_volume_formula_60():
    pass

def stem_volume_formula_61():
    pass

def stem_volume_formula_62():
    pass

def stem_volume_formula_63():
    pass

def stem_volume_formula_64():
    pass

def stem_volume_formula_65():
    pass

#rogy equation
def stem_volume_formula_66(D,H):
    a=-0.03088
    b=0.004676261
    c=-4.8614e-5
    d=-3.8178e-6
    e=-0.0011638
    f=4.0597e-5
    v= a + b*D + c*(D**2) + d*(D**3) + e*H + f*(D**2)*H #Larix decidua (Larch, Mélèzes)(Belgium)
    return v

def stem_volume_formula_67():
    pass

def stem_volume_formula_68():
    pass

def stem_volume_formula_69():
    pass

def stem_volume_formula_70():
    pass

def stem_volume_formula_71():
    pass

def stem_volume_formula_72():
    pass

def stem_volume_formula_73():
    pass

def stem_volume_formula_74():
    pass

def stem_volume_formula_75():
    pass

def stem_volume_formula_76():
    pass

def stem_volume_formula_77():
    pass

def stem_volume_formula_78():
    pass

def stem_volume_formula_79():
    pass

def stem_volume_formula_80():
    pass

def stem_volume_formula_81():
    pass
  #rogy equation
def stem_volume_formula_82(D,H):
    a=0.46818
    b=-0.013919
    c=-28.213
    d=0.37474
    e=-0.28875
    f=28.279
    v= (math.pi / 4) * (
    a * D**2 * H +
    b * D**2 * H * (math.log(D))**2 +
    c * D**2 +
    d * D * H +
    e * H +
    f * D
)
 #Picea abies (Norway spruce, Kuusi, Gran, Epicéa, Fijnspar)(Austria)
    return v

def stem_volume_formula_83():
    pass

def stem_volume_formula_84():
    pass

def stem_volume_formula_85():
    pass

def stem_volume_formula_86():
    pass

def stem_volume_formula_87():
    pass

def stem_volume_formula_88():
    pass

def stem_volume_formula_89():
    pass

def stem_volume_formula_90():
    pass

def stem_volume_formula_91():
    pass

def stem_volume_formula_92():
    pass

def stem_volume_formula_93():
    pass

def stem_volume_formula_94():
    pass

def stem_volume_formula_95():
    pass

def stem_volume_formula_96():
    pass

def stem_volume_formula_97():
    pass
 #rogy equation
def stem_volume_formula_98(D,H):
    a=0.00053238
    b=2.164126647
    c=-0.04670018
    d=0.54879808
    v= a * D**(b + c) * H**d #Picea abies (Norway spruce, Kuusi, Gran, Epicéa, Fijnspar)(Neatherlands)
    return v

def stem_volume_formula_99():
    pass

def stem_volume_formula_100():
    pass

def stem_volume_formula_101():
    pass

def stem_volume_formula_102():
    pass

def stem_volume_formula_103():
    pass

def stem_volume_formula_104():
    pass

def stem_volume_formula_105():
    pass

def stem_volume_formula_106():
    pass

def stem_volume_formula_107():
    pass

def stem_volume_formula_108():
    pass

def stem_volume_formula_109():
    pass

def stem_volume_formula_110():
    pass

def stem_volume_formula_111():
    pass

def stem_volume_formula_112():
    pass

def stem_volume_formula_113():
    pass
 #rogy equation
def stem_volume_formula_114(D,H):
    a=0.666151
    b=0.458507
    v= (math.pi / 40000) * H * D * (a + b * D) #Picea abies (Norway spruce, Kuusi, Gran, Epicéa, Fijnspar)(Poland)
    return v

def stem_volume_formula_115():
    pass

def stem_volume_formula_116():
    pass

def stem_volume_formula_117():
    pass

def stem_volume_formula_118():
    pass

def stem_volume_formula_119():
    pass

def stem_volume_formula_120():
    pass

def stem_volume_formula_121():
    pass

def stem_volume_formula_122():
    pass

def stem_volume_formula_123():
    pass

def stem_volume_formula_124():
    pass

def stem_volume_formula_125():
    pass

def stem_volume_formula_126():
    pass

def stem_volume_formula_127():
    pass

def stem_volume_formula_128():
    pass

def stem_volume_formula_129():
    pass
 #rogy equation
def stem_volume_formula_130(D,H):
    a=0.0739
    b=1.7508
    c=1.0228
    v= a * D**b * H**c #Picea spp. (Molid)(Iceland)
    return v
def stem_volume_formula_131():
    pass

def stem_volume_formula_132():
    pass

def stem_volume_formula_133():
    pass

def stem_volume_formula_134():
    pass

def stem_volume_formula_135():
    pass

def stem_volume_formula_136():
    pass

def stem_volume_formula_137():
    pass

def stem_volume_formula_138():
    pass

def stem_volume_formula_139():
    pass

def stem_volume_formula_140():
    pass

def stem_volume_formula_141():
    pass

def stem_volume_formula_142():
    pass

def stem_volume_formula_143():
    pass

def stem_volume_formula_144():
    pass

def stem_volume_formula_145():
    pass

def stem_volume_formula_146():
    pass

def stem_volume_formula_147():
    pass

def stem_volume_formula_148():
    pass

def stem_volume_formula_149():
    pass

def stem_volume_formula_150():
    pass

def stem_volume_formula_151():
    pass

def stem_volume_formula_152():
    pass

def stem_volume_formula_153():
    pass

def stem_volume_formula_154():
    pass

def stem_volume_formula_155():
    pass

def stem_volume_formula_156():
    pass

def stem_volume_formula_157():
    pass

def stem_volume_formula_158():
    pass

def stem_volume_formula_159():
    pass

def stem_volume_formula_160():
    pass

def stem_volume_formula_161():
    pass

def stem_volume_formula_162():
    pass

def stem_volume_formula_163():
    pass

def stem_volume_formula_164():
    pass

def stem_volume_formula_165():
    pass

def stem_volume_formula_166():
    pass

def stem_volume_formula_167():
    pass

def stem_volume_formula_168():
    pass

def stem_volume_formula_169():
    pass

def stem_volume_formula_170():
    pass

def stem_volume_formula_171():
    pass

def stem_volume_formula_172():
    pass

def stem_volume_formula_173():
    pass

def stem_volume_formula_174():
    pass

def stem_volume_formula_175():
    pass

def stem_volume_formula_176():
    pass

def stem_volume_formula_177():
    pass

def stem_volume_formula_178():
    pass

def stem_volume_formula_179():
    pass

def stem_volume_formula_180():
    pass

def stem_volume_formula_181():
    pass

def stem_volume_formula_182():
    pass

def stem_volume_formula_183():
    pass

def stem_volume_formula_184():
    pass

def stem_volume_formula_185():
    pass

def stem_volume_formula_186():
    pass

def stem_volume_formula_187():
    pass

def stem_volume_formula_188():
    pass

def stem_volume_formula_189():
    pass

def stem_volume_formula_190():
    pass

def stem_volume_formula_191():
    pass

def stem_volume_formula_192():
    pass

def stem_volume_formula_193():
    pass

def stem_volume_formula_194():
    pass

def stem_volume_formula_195():
    pass

def stem_volume_formula_196():
    pass

def stem_volume_formula_197():
    pass

def stem_volume_formula_198():
    pass

def stem_volume_formula_199():
    pass

def stem_volume_formula_200():
    pass

def stem_volume_formula_201():
    pass

def stem_volume_formula_202():
    pass

def stem_volume_formula_203():
    pass

def stem_volume_formula_204():
    pass

def stem_volume_formula_205():
    pass

def stem_volume_formula_206():
    pass

def stem_volume_formula_207():
    pass

def stem_volume_formula_208():
    pass

def stem_volume_formula_209():
    pass

def stem_volume_formula_210():
    pass

def stem_volume_formula_211():
    pass

def stem_volume_formula_212():
    pass

def stem_volume_formula_213():
    pass

def stem_volume_formula_214():
    pass

def stem_volume_formula_215():
    pass

def stem_volume_formula_216():
    pass

def stem_volume_formula_217():
    pass

def stem_volume_formula_218():
    pass

def stem_volume_formula_219():
    pass

def stem_volume_formula_220():
    pass

def stem_volume_formula_221():
    pass

def stem_volume_formula_222():
    pass

def stem_volume_formula_223():
    pass

def stem_volume_formula_224():
    pass

def stem_volume_formula_225():
    pass

def stem_volume_formula_226():
    pass

def stem_volume_formula_227():
    pass

def stem_volume_formula_228():
    pass

def stem_volume_formula_229():
    pass

def stem_volume_formula_230():
    pass
