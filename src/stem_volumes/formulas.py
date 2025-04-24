"""
This module implements the 230 stem volume formulas from Silva Fennica by
Zianis et al.

The different formulas are based on Appendix B (starting on page 44) and
Appendix C (starting page 52) of the monograph. It can be downloaded at
https://doi.org/10.14214/sf.sfm4.
"""

import math

def stem_volume_formula_1(D, H, a=1.6662, b=3.2394, c=1.9335, d=-1.8997, e=-0.9739): # D should be greater than 5cm
    # Volume calculation formula for Abies alba Silver fir from Norway.
        V = a * H**b * D**c * (H - 1.3)**d * (D + 100)**e
        return V # Calculated volume in dm³

def stem_volume_formula_2(D, H):
    a = 1.89756
    b = 0.97717
    c = -2.94252
    V = (D ** a) * (H ** b) * math.exp(c)
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

def stem_volume_formula_8(D, H):
    
    a=0.00046903
    b=1.807
    c=0.0292
    d=-0.4155
    e=0.5455

    V = a * 10**(b * math.log10(D) + c * math.log10(D)**2 + d * math.log10(H) + e * math.log10(H)**2)
    return V

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

# Linus - Acer pseudoplatanus, Romania
def stem_volume_formula_11(D, H):

    # Reference: Giurgiu, V. 1974. O expresie matematica unica a relatiei diametru – înaltime – volum, pentru majoritatea speciilor forestiere din Romania. Silviculturasi Exploatarea Padurilor 89(4): 173–178.
    # Units: V(m^3), D(cm), H(m)

    # Import the log10 function from the math package
    from math import log10

    # Define the coefficients
    a = 0.00035375
    b = 1.02
    c = 0.3997
    d = 0.666
    e = 0.021
    
    # Calculate the volume according to the formula given by Zianis et al.
    V = a * 10**(b * log10(D) + c * log10(D)**2 + d * log10(H) + e * log10(H)**2)

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

def stem_volume_formula_17(D, H, a=0.0001, b=2.5, c=0.5, d=0.3, e=0.2):
    # Alnus glutinosa (Black alder, Klibbal) in Sweden
    V = a * D**2 + b * D**2 * H + c * D * H**2 + d * D * H + e * D**2 * H**2
    return V # Calculated volume in dm³

def stem_volume_formula_18():
    pass

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

# Linus - Betula spp., Finland
# The calculated volume seems to be unrealistically low,
# however the implementation of the formula is according to the original paper.
def stem_volume_formula_27(D):

    # Reference: Laasasenaho, J. 1982. Taper curve and volume functions for pine, spruce and birch. Communicationes Instituti Forestalis Fenniae 108: 1–74.
    # Units: V(dm^3), D(cm)

    # Import the natural logarithm function from the math package
    from math import log 

    # Raise ValueError if the diameter is out of range
    if D < 1.2 or D > 49.7: 
        raise ValueError("Diameter must be between 1.2 and 49.7 cm.")
    
    # Raise ValueError if the height is out of range
    if H < 2.4 or H > 29.5:
        raise ValueError("Height must be between 2.4 and 29.5 m.")

    # Define the coefficients
    a = -5.41948
    b = 3.57630	
    c = 2
    d = 1.25
    e = -0.0395855

    # Calculate the volume according to the formula given by Zianis et al.
    V = a + b * log(c + d * D) + e * D 
    
    # Return the calculated volume
    return V

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

def stem_volume_formula_33(D, H, a=0.1305, b=0.01338, c=0.01757, d=-0.05606): # D should be between 5cm-34.9cm and H between 5m-26.9m
    # Betula spp. (Birch, Björk, Bjørk, Bouleaux, Mesteacan) in Sweden
    V = a * D**2 + b * D**2 * H + c * D * H**2 + d * H**2
    return V # Calculated volume in dm³

def stem_volume_formula_34():
    pass

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

# Linus - Chamaecyparis lawsoniana, Netherlands
def stem_volume_formula_43(D, H):

    # Reference: Dik, E.J. 1984. Estimating the wood volume of standing trees in forestry practice. Rijksinstituut voor onderzoek in de bos en landschapsbouw de Dorschkamp, Wageningen. Uitvoerige verslagen 19(1): 1–114.
    # Units: V(dm^3), D(cm), H(m)

    # Import the exponential function from the math package
    from math import exp

    # Define the coefficients
    a = 1.85298
    b = 0.86717
    c = -2.33706

    # Calculate the volume according to the formula given by Zianis et al.
    V = D**a * H**b * exp(c)

    # Return the calculated volume
    return V 

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

def stem_volume_formula_49(D, H, a=-0.015572, b=0.00290013, c=-7.0476*10**(-6), d=2.3935*10**(-6), e=-0.0013528, f=3.9837*10**(-5)):
    # Fagus sylvatica (Beech, Rotbuche, Beuk) in Belgium
    V = a + b * D + c * D**2 + d * D**3 + e * H + f * D**2 * H
    return V # Calculated volume in m³

def stem_volume_formula_50():
    pass

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

# Linus - Fraxinus Excelsior, Sweden
def stem_volume_formula_59(D, H):
    
    # Reference: Eriksson, H. 1973. Volymfunktioner för stående träd av ask, asp, klibbal och contorta-tall. Institutionen för Skogsproduktion, Royal College of Forestry, Stockholm. Research Notes 26: 1–26.
    # Units: V(dm^3), D(cm), H(m)

    # Define the coefficients
    a = 0.03249
    b = 0.02941
    c = 0.03892	

    # Calculate the volume according to the formula given by Zianis et al.
    V = a * D**2 * H + b * D**2 + c * D * H

    # Return the calculated volume
    return V

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

def stem_volume_formula_65(D, H, a=0.487270, b=-2.04291, c=5.9995): # D should be between 0.5cm to 1.04cm
    # Larix decidua (larch, Mélèzes) in Austria
    V = (math.pi / 4) * (a * D **2 * H + b * D**2 + c * D)
    return V # Calculated volume in dm³

def stem_volume_formula_66():
    pass

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

# Linus - Larix sibirica, Norway
def stem_volume_formula_75(D, H):

    # Reference: Øen, S., Bauger, E. & Øyen, B.-H. 2001. Functionar for volumberekning av framande treslag i Vest-Norge. Aktuelt fra Skogforsk 3/01: 18–19.
    # Units: V(dm^3), D(cm), H(m)

    # Raise ValueError if the diameter is out of range
    if D < 5:
        raise ValueError("Diameter must be at least 5 cm.")

    # Define the coefficients
    a = 0.7761
    b = 3.6461
    c = 1.9166
    d = -2.3179
    e = -0.8236
    
    # Calculate the volume according to the formula given by Zianis et al.
    V = a * H**b * D**c * (H - 1.3)**d * (D + 100)**e

    # Return the calculated volume
    return V

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

def stem_volume_formula_81(D, H, a=2.822*10**(-5), b=2.2060, c=-0.1136, d=1.115, e=0.0129):
    # Larix spp. (lehtikuusi, lork, larice) in Romania
    V = a * 10**(b * math.log10(D) + c * math.log10(D)**2 + d * math.log10(H) + e * math.log10(H)**2)
    return V # Calculated volume in m³

def stem_volume_formula_82():
    pass

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

# Linus - Picea abies, Finland
def stem_volume_formula_91(D, H):

    # Reference: Kanninen, K., Uusvaara, O. & Valonen, P. 1977.Kokopuuraaka-aineen mittaus ja ominaisuudet. Folia Forestalia 403: 1–53.
    # Units: V(dm^1), D(cm), H(m)

    # Raise ValueError if the diameter is out of range
    if D < 2 or D > 18: 
        raise ValueError("Diameter must be between 2 and 18 cm.")
    
    # Raise ValueError if the height is out of range
    if H < 2 or H > 18:
        raise ValueError("Height must be between 2 and 18 m.")

    # Define the coefficients
    a = 0.7877 
    b = 1.9302
    c = 0.79465

    # Calculate the volume according to the formula given by Zianis et al.
    V = a * D**b * H**c
    
    # Return the calculated volume
    return V

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

def stem_volume_formula_97(D, H, a=0.00053238, b=2.164126647, c=0.004108377, d=0.54879808):
    # Picea abies (Norway spruce, Kuusi, Gran, Epicéa, Fijnspar) in Netherlands
    V = a*D**(b+c) * H**d
    return V # Calculated volume in dm³

def stem_volume_formula_98():
    pass

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

# Linus - Picea abies, Norway
def stem_volume_formula_107(D, H):

    # Reference: Vestjordet, E. 1967. Funksjoner og tabeller for kubering av stående gran. Meddelelser fra det Norske Skogforsøksvesen 84: 539–574.
    # Units: V(dm^3), D(cm), H(m)

    # Raise ValueError if the diameter is out of range
    if D < 13 or D > 59.4:
        raise ValueError("Diameter must be between 13 and 59.4 cm.")
    # Raise ValueError if the height is out of range
    if H > 39.49:
        raise ValueError("Height may be 39.49 m at max.")

    # Define the coefficients
    a = 10.14
    b = 0.0124
    c = 0.03117
    d = -0.36381
    e = 0.28578

    # Calculate the volume according to the formula given by Zianis et al.
    V = a + b * D**2 * H + c * D * H**2 + d * H**2 + e * D * H

    # Return the calculated volume
    return V

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

def stem_volume_formula_113(D, H, a=4.33, b=0.01491, c=0.02606, d=-0.31854, e=0.31106): # D should be between 10cm-59.4cm and H should be <39.49
    # Picea abies (Norway spruce, Kuusi, Gran, Epicéa, Fijnspar) in Norway
    V = a + b * D**2 * H + c * D * H**2 + d * H**2 + e * D * H
    return V # Calculated volume in dm³

def stem_volume_formula_114():
    pass

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

# Linus - Picea abies, Sweden
def stem_volume_formula_123(D, H):

    # Reference: Brandel, G. 1974. Volymfunktioner för tall och gran. Skoghögskolan, Institutionen för skogsproduktion, Rapporter och Uppsatser 33: 178–191.
    # Units: V(dm^3), D(cm), H(m)

    # Raise ValueError if the diameter is out of range
    if D < 2:
        raise ValueError("Diameter must be at least 2 cm.")
    # Raise ValueError if the height is out of range
    if H < 2:
        raise ValueError("Height must be at least 2 m.")

    # Define the coefficients
    a = -1.0342
    b = 1.9683
    c = -0.3850
    d = 2.4018
    e = -1.2075

    # Calculate the volume according to the formula given by Zianis et al.
    V = 10**a * D**b * (D + 20)**c * H**d * (H - 1.3)**e

    # Return the calculated volume
    return V

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

def stem_volume_formula_129(D, H, a=0.00009464, b=1.9341, c=-0.0722, d=0.6365, e=0.172):
    # Picea spp. (Molid) in Romania
    V = a * 10**(b * math.log10(D) + c * math.log10(D)**2 + d * math.log10(H) + e * math.log10(H)**2)
    return V # Calculated volume in m³


def stem_volume_formula_130():
    pass

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

# Linus - Pinus spp., Germany
def stem_volume_formula_139(H):

    # Reference: Hempel, G. 1968. Allometrische studie an Pinus cembra spp. sibirica (Rupr.) Kryl. und Abies sibirica (Ledeb.). Archiv für Forstwesen 17(11):1099–1115.
    # Units: V(m^3), H(m)

    # Define the coefficients
    a = 0.000074
    b = 3.1

    # Calculate the volume according to the formula given by Zianis et al.
    V = a * H**b

    # Return the calculated volume
    return V

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

def stem_volume_formula_145(D, a=0.000244, b=2.32716):
    # Pinus sylvestris (Scots pine, Mänty, Tall, Furu, Grove den, Pin silvestri) in Belgium
    V = a * D**b
    return V # Calculated volume in m³

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

# Linus - Pinus sylvestris, Germany
def stem_volume_formula_155(D, H):

    # Reference: Lockow, K.-W. 1993. Modellbildung und Quantifizierung der Durchmesser- und Volumenstruktur des ausscheidenden Kieferjungbestandes – Holzmeßkundliche Entscheideungshilfen für die Erstdurchforstung. Beiträge für Forstwirtschaft und Landschaftsökologie 27(2): 77–82.
    # Units: V(m^3), D(cm), H(m)

    # Raise ValueError if the diameter is out of range
    if D < 3 or D > 14:
        raise ValueError("Diameter must be between 3 and 14 cm.")
    # Raise ValueError if the height is out of range
    if H < 5.8 or H > 10.7:
        raise ValueError("Height must be between 5.8 and 10.7 m.")

    # Define the coefficients
    a = 5.6537 * 10**-5
    b = 1.960466
    c = 0.894433

    # Calculate the volume according to the formula given by Zianis et al.
    V = a * D**b * H**c

    # Return the calculated volume
    return V

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

def stem_volume_formula_161(D, H, a=0.1424, b=2.0786, c=1.9028, d=-1.0259, e=-0.2640):
    # Pinus sylvestris (Scots pine, Mänty, Tall, Furu, Grove den, Pin silvestri) in Norway
    V = a * H**b * D**c * (H-1.3)**d * (D+100)**e
    return V # Calculated volume in dm³

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

# Linus - Pinus sylvestris, Sweden 
def stem_volume_formula_171(D, H):

    # Reference: Brandel, G. 1974. Volymfunktioner för tall och gran.Skoghögskolan, Institutionen för skogsproduktion, Rapporter och Uppsatser 33: 178–191.
    # Units: V(dm^3), D(cm), H(m)

    # Raise ValueError if the diameter is out of range
    if D < 2:
        raise ValueError("Diameter must be at least 2 cm.")
    # Raise ValueError if the height is out of range
    if H < 2:
        raise ValueError("Height must be at least 2 m.")

    # Define the coefficients
    a = -1.1226
    b = 2.0180
    c = -0.2135
    d = 1.8271
    e = -0.8297

    # Calculate the volume according to the formula given by Zianis et al.
    V = 10**a * D**b * (D + 20)**c * H**d * (H - 1.3)**e

    # Return the calculated volume
    return V

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

def stem_volume_formula_177(D, H, a=-1.2605, b=1.9322, c=-0.0897, d=2.1795, e=-1.1676): # D should be >2cm and H should be >2m
    # Pinus sylvestris (Scots pine, Mänty, Tall, Furu, Grove den, Pin silvestri) in Sweden
    V = 10**a * D**b * (D + 20)**c * H**d * (H + 1.3)**e
    return V # Calculated volume in dm³

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

# Linus - Populus tremulus, Romania
def stem_volume_formula_187(D, H):

    # Giurgiu, V. 1974. O expresie matematica unica a relatiei diametru – înaltime – volum, pentru majoritatea speciilor forestiere din Romania. Silviculturasi Exploatarea Padurilor 89(4): 173–178.
    # Units: V(m^3), D(cm), H(m)

    # Import the log10 function from the math package
    from math import log10

    # Define the coefficients
    a = 0.00007604
    b = 1.7812
    c = 0.0528
    d = 0.8533
    e = 0.0654

    # Calculate the volume according to the formula given by Zianis et al.
    V = a * 10**(b * log10(D) + c * log10(D)**2 + d * log10(H) + e * log10(H)**2)

    # Return the calculated volume
    return V

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

def stem_volume_formula_193(D, H, a=-0.019911, b=0.001871101, c=0.000127328, d=-5.7631*10**(-6), e=0.00071591, f=3.9371*10**(-5)):
    # Pseudotsuga menziesii (Douglas fir, Duglas) in Belgium
    V = a + b * D + c * D**2 + d * D**3 + e * H + f * D**2 * H
    return V # Calculated volume in m³

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

# Linus - Quercus laevis, Romania
def stem_volume_formula_203(D, H):

    # Giurgiu, V. 1974. O expresie matematica unica a relatiei diametru – înaltime – volum, pentru majoritatea speciilor forestiere din Romania. Silviculturasi Exploatarea Padurilor 89(4): 173–178.
    # Units: V(m^3), D(cm), H(m)

    # Import the log10 function from the math package
    from math import log10

    # Define the coefficients
    a = 0.0001992
    b = 2.014
    c = -0.0602	
    d = -0.1108
    e = 0.4811

    # Calculate the volume according to the formula given by Zianis et al.
    V = a * 10**(b * log10(D) + c * log10(D)**2 + d * log10(H) + e * log10(H)**2)

    # Return the calculated volume
    return V

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

def stem_volume_formula_209(D, H, a=1.83932, b=0.9724, c=-2.71877):
    #  Quercus rubra (Red oak, chêne rouge) in Netherlands
    V = D**a * H**b * math.exp(c)
    return V # Calculated volume in dm³

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

# Linus - Salix caprea, Romania
def stem_volume_formula_219(D, H):

    # Giurgiu, V. 1974. O expresie matematica unica a relatiei diametru – înaltime – volum, pentru majoritatea speciilor forestiere din Romania. Silviculturasi Exploatarea Padurilor 89(4): 173–178.
    # Units: V(m^3), D(cm), H(m)

    # Import the log10 function from the math package
    from math import log10

    # Define the coefficients
    a = 0.00011585
    b = 1.6688
    c = 0.1090
    d = 0.7781
    e = 0.0269

    # Calculate the volume according to the formula given by Zianis et al.
    V = a * 10**(b * log10(D) + c * log10(D)**2 + d * log10(H) + e * log10(H)**2)

    # Return the calculated volume
    return V

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

def stem_volume_formula_225(D, H, a=0.00004124, b=1.9302, c=0.0209, d=0.129, e=-0.1903):
    # Tilia cordata (Tei) in Romania
    V = a * 10**(b * math.log10(D) + c * math.log10(D)**2 + d * math.log10(H) + e * math.log10(H)**2)
    return V # Calculated volume in m³

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
