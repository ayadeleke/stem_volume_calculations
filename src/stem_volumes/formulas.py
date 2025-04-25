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
    # input: diameter D in dm (range 1 -), height H in dm
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
    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Acacia spp. (Salcim) from Romania. 
    
    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.
        
    Returns:
        V: Stem volume in dm3.
    """
    #coefficients
    a=0.00046903
    b=1.807
    c=0.0292
    d=-0.4155
    e=0.5455

    V = a * 10**(b * math.log10(D) + c * math.log10(D)**2 + d * math.log10(H) + e * math.log10(H)**2)
    return V

def stem_volume_formula_9(D, H):
    # reference: Dagnelie, P., Palm, R., Rondeux, J. & Thill, A. 1999. Tables de cubage des arbres et des peuplements forestiers. Les Presses Agronomiques de Gembloux, Gembloux. 126 p.
    # for Acer pseudoplatanus (Maple, Erable sycomore, Paltin, Sycamore), from Belgium
    # input: diameter D in cm, height H in m
    # output: volume in m3

    # coefficients 
    a = 0.010343
    b = -0.00450536
    c = 0.0003407
    d = -0.000004042
    e = 0.00077115
    f = 0.000029836

    # equation
    V = a+b*D+c*(D**2)+d*(D**3)+e*H+f*(D**2)*H

    return V

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
    
    # Alnus glutinosa - Norway
    # D = cm | H = m | V = dm³
    # D range = 0-12cm 

    # coefficients
    a = 0.6716
    b = 0.75708
    c = 0.029679
    d = 0.004341

    # equation  
    V = a + b * D**2 + c * D**2 * H + d * H**2 * D

    # volume
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

def stem_volume_formula_21(D, H):
    # Reference: Giurgiu, V. 1974. O expresie matematica unica a relatiei diametru – înaltime – volum, pentru majori-tatea speciilor forestiere din Romania. Silvicultura si Exploatarea Padurilor 89(4): 173–178.
    # for Alnus nigra (Anin negru), from Romania
    # input: diameter D in cm, height H in m
    # output: volume in m³

    import math

    # define parameters
    a = 0.00008666
    b = 1.7148
    c = 0.1014
    d = 0.801
    e = 0.0530

    # implement formula
    V =  a*10**(b*math.log10(D)+c*math.log10(D)**2+d*math.log10(H)+e*math.log10(H)**2)
    return V

def stem_volume_formula_22():
    pass

def stem_volume_formula_23():
    pass

def stem_volume_formula_24(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for  Betula pendula (Birch, Berk) from Netherlands. 
    
    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.
        
    Returns:
        V: Stem volume in dm3.
    """
     #coefficients
    a=1.89060
    b=0.26595
    c=-1.07055
    

    V = D**a *H**b *math.exp(c)
    return V

def stem_volume_formula_25(D, H):
    # reference: Dagnelie, P., Palm, R., Rondeux, J. & Thill, A. 1999. Tables de cubage des arbres et des peuplements forestiers. Les Presses Agronomiques de Gembloux, Gembloux. 126 p.
    # Betula spp. (Birch, Björk, Bjørk, Bouleaux, Mesteacan), from Belgium
    # input: diameter D in cm, height H in m
    # output: volume in m3

    # coefficients 
    a = -0.011392
    b = -0.00031447
    c = 0.000279211 
    d = -0.0000057966
    e = -0.00059573
    f = 0.000030409

    # equation 
    V = a+b*D+c*(D**2)+d*(D**3)+e*H+f*(D**2)*H

    return V

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

def stem_volume_formula_32(D, H):
    
    # Betula spp. - Romania
    # D = cm | H = m  | V = m³

    # coefficients
    a = 8.141e-5
    b = 2.248
    c = -0.2062
    d = 0.1946
    e = 0.4147

    # equation  
    V = a * 10**(b * math.log10(D) + c * math.log10(D)**2 + d * math.log10(H) + e * math.log10(H)**2)

    # volume
    return V

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

def stem_volume_formula_37(D, H):
    # Reference: Brandel, G. 1990. Volumfunktioner för enskilda träd. Sveriges lantbruksuniversitet, Institutionen för skogsproduktion, Rapport 6: 1–181.
    # for  Betula spp. (Birch, Björk, Bjørk, Bouleaux, Mesteacan), from Sweden
    # input: diameter D in cm (range 4.5 -), height H in m (range 6 -)
    # output: volume in dm³

    # define parameters
    a = -0.35394
    b = 2.52141
    c = -1.54257
    d = 4.88165
    e = -3.47422

    # implement formula
    V = 10**a * D**b * (D+20)**c * H**d * (H-1.3)**e
    return V

def stem_volume_formula_38():
    pass

def stem_volume_formula_39():
    pass

def stem_volume_formula_40(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for  Carpinus spp. from Netherlands. 
    
    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.
        
    Returns:
        V: Stem volume in dm3.
    """
    #coefficients
    a=0.00021491
    b=2.258957614
    c=0.001411006
    d=0.60291075
    

    V = a*D**(b+c)*H**d
    return V

def stem_volume_formula_41(D, H):
    # reference: 1 Schelhaas, M.J., Nabuurs, G.J., Jans, W.W.P.,Moors, E.J., Sabaté, S. & Daamen, W.P. 2002. Converging estimates of the forest carbon sink. Alterra-rapport 631: 1–44. 
    # Carpinus spp., from Netherlands
    # input: diameter D in mm, height H in m
    # output: volume in dm3

    # coefficients 
    a = 0.00021491
    b = 2.258957614
    c = -0.01120638
    d = 0.60291075

    # equation 
    V = a*(D**(b+c))*(H**d)

    return V

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

def stem_volume_formula_48(D,H):

    # Fagus spp. - UK
    # D = cm | H = m  | V = m³

    # coefficients
    a = -0.014306
    b = 0.0000748
    c = 0.75

    # equation  
    V = a + b * D**2 * H**c

    # volume
    return V

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

def stem_volume_formula_53(D, H):
    # Reference: De Vries, P.G. 1961. The principle of nomograms applied to the stem volume functions of the volume tables for forest trees grown in the Netherlands. Nederlands Bosbouw Tijdschrift 33(5): 114–1 1.
    # for  Fagus sylvatica (Beech, Rotbuche, Beuk), from the Netherlands
    # input: diameter D in cm, height H in m
    # output: volume in dm³

    # define parameters
    a = 0.049
    b = 1.78189
    c = 1.08345

    # implement formula
    V = a * D**b * H**c
    return V

def stem_volume_formula_54():
    pass

def stem_volume_formula_55():
    pass

def stem_volume_formula_56(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for  Fraxinus exselsior (Ash, Frêne, Es)
  from Sweden. 
    
    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.
        
    Returns:
        V: Stem volume in dm3.
    """
    #coefficients
    a=0.03246
    b=0.03310
    c=0.04127
    
    

    V = a*D**2*H+b*D**2+c*D*H
    return V

def stem_volume_formula_57(D, H):
    # reference: Eriksson, H. 1973. Volymfunktioner för ståendeträd av ask, asp, klibbal och contorta-tall. Institutionen för Skogsproduktion, Royal College of Forestry, Stockholm. Research Notes 26: 1–26.
    # Fraxinus exselsior (Ash, Frêne, Es), from Sweden
    # input: diameter D in cm, height H in m
    # output: volume in dm3

    # coefficients 
    a = 0.03593
    b = 0.03310
    c = 0.04127

    # equation 
    V = a * (D**2) * H + b * (D**2) + c * D * H

    return V
    
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

def stem_volume_formula_64(D,H):

    # Larix decidua - Austria
    # D = dm | H = dm  | V = dm³

    # coefficients
    a = 0.609443
    b = -0.0455748
    c = -18.6631
    d = -0.248736
    e = 0.126594
    f = 36.9783
    g = -14.204

    # equation  
    V = (math.pi / 4) * (a * D**2 * H + b * D**2 * H * math.log(D)**2 + c * D**2 + d * D * H + e * H + f * D + g)

    # volume
    return V

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

def stem_volume_formula_69(D, H):
    # Reference: Øen, S., Bauger, E. & Øyen, B.-H. 001. Functionar for volumberekning av framande treslag i Vest-Norge. Aktuelt fra Skogforsk 3/01: 18–19.
    # for  Larix hybrid (Hyprid larix), from Norway
    # input: diameter D in cm (range 5 -), height H in m
    # output: volume in dm³

    # define parameters
    a = 0.7761
    b = 3.6461
    c = 1.9166
    d = -2.3179
    e = -0.8236

    # implement formula
    V =  a * H**b * D**c * (H-1.3)**d * (D+100)**e
    return V

def stem_volume_formula_70():
    pass

def stem_volume_formula_71():
    pass

def stem_volume_formula_72(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Larix sibirica (Siberian larix)
  from Iceland. The range of valid values for D is 4 cm and above. 
    
    Args:
        D: Diameter at breast height in cm. Recommendend range: 4 cm and above.
        H: Tree height in m.
        
    Returns:
        V: Stem volume in dm3.
    """
    #coefficients
    a=-2.5079
    b=1.7574
    c=0.9808
    
    

    V = math.exp(a)*D**b*H**c
    return V

def stem_volume_formula_73(D, H):
    # reference: Norrby, M. 1990. Volym- och formtalsfunktioner for Larix sukaczewii och Larix sibirica på Island.Institutionen för skogsskötsel. Series Volym- ochformtalsfunktioner for Larix sukaczewii och Larix sibirica på Island. Sveriges Lantbruksuniversitet, Umeå.
    # Larix sibirica (Siberian larix), from Iceland
    # input: diameter D in cm, height H in m
    # output: volume in m3

    # coefficients 
    a = -2.9946
    b = 1.8105
    c = 0.9908 

    # equation 
    V = math.exp(a) * (D**b) * (H**c)

    return V

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

def stem_volume_formula_80(D,H):
    
    # Larix spp. - Netherlands
    # D = mm | H = m  | V = dm³

    # coefficients
    a = 0.00035217
    b = 2.12841828
    c = -0.0026067	
    d = 0.76283925

    # equation  
    V = a * D**(b + c) * H**d

    # volume
    return V

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

def stem_volume_formula_85(D):
    # Reference: Cerný, M. 1990. Biomass of Picea abies (l.) Karst. in midwestern Bohemia. Scandinavian Journal of Forest Research 5: 83–95.
    # for Picea abies (Norway spruce, Kuusi, Gran, Epicéa, Fijnspar), from Czech Republic
    # input: diameter D in cm
    # output: volume in m³

    # define parameters
    a = 0.00059707
    b = 2.1286

    # implement formula
    V =  a * D**b
    return V

def stem_volume_formula_86():
    pass

def stem_volume_formula_87():
    pass

def stem_volume_formula_88(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Picea abies (Norway spruce, Kuusi, Gran, Epicéa, Fijnspar) from Finland. The range of valid values for D is 1.5 cm and above. 
    
    Args:
        D: Diameter at breast height in cm. Recommendend range: 1.5 cm and above.
        H: Tree height in m.
        
    Returns:
        V: Stem volume in dm3.
    """
     #coefficients
    a=-5.39934
    b=3.46468
    c=2
    d=1.25
    e=-0.073199
    
    

    V = a+b*math.log(c+d*D)+e*D
    return V

def stem_volume_formula_89(D, H):
    # reference:  Laasasenaho, J. 1982. Taper curve and volume functions for pine, spruce and birch. Communicationes Instituti Forestalis Fenniae 108: 1–74.
    # Picea abies (Norway spruce, Kuusi, Gran, Epicéa, Fijnspar), from Finland
    # input: diameter D in cm, height H in m
    # output: volume in dm3

    # coefficients 
    a = 0.022927
    b = 1.91505
    c = 0.99146 
    d = 2.82541
    e = -1.53547

    # equation 
    V = a * (D**b) * (c**D) * (H**d) * ((H-1.3)**e)

    return V

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

def stem_volume_formula_96(D,H):

    # RESULTS TOO HIGH | checked original source: eq, coeff and units correct
    # Picea abies - Iceland
    # D = cm | H = m  | V = m³

    # coefficients
    a = 0.1299		
    b = 1.6834
    c = 0.8598

    # equation  
    V = a * D**b * H**c

    # volume
    return V

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

def stem_volume_formula_101(D, H):
    # Reference: De Vries, P.G. 1961. The principle of nomograms applied to the stem volume functions of the volume tables for forest trees grown in the Netherlands. Nederlands Bosbouw Tijdschrift 33(5): 114–1 1.
    # for Picea abies (Norway spruce, Kuusi, Gran, Epicéa, Fijnspar), from the Netherlands
    # input: diameter D in cm, height H in m
    # output: volume in dm³

    # define parameters
    a = 0.04143
    b = 1.6704
    c = 1.3337

    # implement formula
    V =  a * D**b * H**c
    return V

def stem_volume_formula_102():
    pass

def stem_volume_formula_103():
    pass

def stem_volume_formula_104(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Picea abies (Norway spruce, Kuusi, Gran, Epicéa, Fijnspar) from Norway. 
    
    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.
        
    Returns:
        V: Stem volume in dm3.
    """
      #coefficients
    a=0.5824
    b=1.1987
    c=1.9339
    d=-0.0594
    e=-0.7442
    
    

    V = a*H**b*D**c*(H-1.3)**d*(D+40)**e
    return V

def stem_volume_formula_105(D, H):
    # reference:  Vestjordet, E. 1967. Funksjoner og tabeller for kubering av stående gran. Meddelelser fra det Norske Skogforsøksvesen 84: 539–574.
    # Picea abies (Norway spruce, Kuusi, Gran, Epicéa, Fijnspar), from Norway
    # input: diameter D in cm, height H in m
    # output: volume in dm3

    # coefficients 
    a = 0.52
    b = 0.02403
    c = 0.01463 
    d = -0.10983
    e = 0.15195

    # equation 
    V = a + b * (D**2) * H + c * D * (H**2) + d * (H**2) + e * D * H
    
    return V

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

def stem_volume_formula_112(D,H):
    
    # Picea abies - Norway
    # D = cm | H = m  | V = dm³

    # coefficients
    a = 0.3				
    b = 0.02593
    c = 0.01268
    d = -0.0977
    e = 0.14586

    # equation  
    V = a + b * D**2 * H + c * D * H**2 + d * H**2 + e * D * H

    # volume
    return V

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

def stem_volume_formula_117(D, H):
    # Reference: Brandel, G. 1974. Volymfunktioner för tall och gran. Skoghögskolan, Institutionen för skogsproduktion, Rapporter och Uppsatser 33: 178–191.
    # for Picea abies (Norway spruce, Kuusi, Gran, Epicéa, Fijnspar), from Sweden
    # input: diameter D in cm (range 2 -), height H in m (range 2 -)
    # output: volume in dm³

    # define parameters
    a = -0.9513
    b = 1.9781
    c = -0.5254
    d = 2.7604
    e = -1.4684

    # implement formula
    V = 10**a * D**b * (D+20)**c * H**d * (H-1.3)**e
    return V

def stem_volume_formula_118():
    pass

def stem_volume_formula_119():
    pass

def stem_volume_formula_120(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Picea abies (Norway spruce, Kuusi, Gran, Epicéa, Fijnspar) from Sweden. The range of valid values for D is 4.5 cm and above. 
    
    Args:
        D: Diameter at breast height in cm. Recommendend range: 4.5 cm and above.
        H: Tree height in m.
        
    Returns:
        V: Stem volume in dm3.
    """
       #coefficients
    a=-0.82249
    b=2.11094
    c=-0.89626
    d=3.51812
    e=-2.05567
    
    

    V = 10**a*D**b*(D+20)**c*H**d*(H-1.3)**e
    return V

def stem_volume_formula_121(D, H):
    # reference: Brandel, G. 1990. Volumfunktioner för enskildaträd. Sveriges lantbruksuniversitet, Institutionen för skogsproduktion, Rapport 26: 1–181.
    # Picea abies (Norway spruce, Kuusi, Gran, Epicéa, Fijnspar), from Sweden
    # input: diameter D in cm, height H in m
    # output: volume in dm3

    # coefficients
    a = -1.06019
    b = 2.04239
    c = -0.54292
    d = 2.80843
    e = -1.52110

    # equation
    V = (10 ** a) * (D ** b) * ((D + 20) ** c) * (H ** d) * ((H - 1.3) ** e)

    return V

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

def stem_volume_formula_128(D,H):
    
    # Picea sitchensis - Norway
    # D = cm | H = m  | V = dm³

    # coefficients
    a = 0.2101			
    b = 1.892
    c = 1.1095
    d = -0.3895

    # equation  
    V = a * D**b * (H - 1.3)**c * (D + 40)**d

    # volume
    return V

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

def stem_volume_formula_133(D, H):
    # Reference: Eriksson, H. 1973. Volymfunktioner för stående träd av ask, asp, klibbal och contorta-tall. Institutionen för Skogsproduktion, Royal college of Forestry, Stockholm. Research Notes 6: 1– 6. 
    # for Pinus contorta (contorta tall), from Sweden
    # input: diameter D in cm, height H in m
    # output: volume in dm³

    # define parameters
    a = 0.1121
    b = 0.02870
    c = -0.000061
    d = 0.09176
    e = 0.01249

    # implement formula
    V = a*D**2+b*D**2*H+c*D**2*H**2-d*D*H+e*D*H**2
    return V

def stem_volume_formula_134():
    pass

def stem_volume_formula_135():
    pass

def stem_volume_formula_136(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Pinus nigra var maritima (Black pine) from Netherlands.
    
    Args:
        D: Diameter at breast height in cm. 
        H: Tree height in m.
        
    Returns:
        V: Stem volume in dm3.
    """
        #coefficients
    a=1.89192
    b=0.95374
    c=-2.72505

    
    

    V = D**a*H**b*math.exp(c)
    return V

def stem_volume_formula_137(D, H):
    # reference: Dik, E.J. 1984. Estimating the wood volume of standing trees in forestry practice. Rijksinstituut voor onderzoek in de bos en landschapsbouw de Dorschkamp, Wageningen. Uitvoerige verslagen 19(1): 1–114.
    # Pinus nigra var nigra (Black pine, Pin negru), from Netherlands
    # input: diameter D in cm, height H in m
    # output: volume in dm3

    # coefficients
    a = 1.95645
    b = 0.88671
    c = -2.7675
 
    # equation
    V = (D ** a) * (H ** b) * math.exp(c)
   
    return V

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

def stem_volume_formula_144(D,H):
    
    # Pinus sylvestris - Austria
    # D = dm | H = dm  | V = dm³

    # coefficients
    a = 0.435949	
    b = -0.0149083
    c = 5.21091
    d = 0.028702

    # equation  
    V = (math.pi / 4) * (a * D**2 * H + b * D**2 * H * math.log(D)**2 + c * D**2 + d * H)

    # volume
    return V

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

def stem_volume_formula_149(D, H):
    # Reference: Laasasenaho, J. 198 . Taper curve and volume functions for pine, spruce and birch. communicationes Instituti Forestalis Fenniae 108: 1–74.  
    # for Pinus sylvestris (Scots pine, Mänty, Tall, Furu, Grove den, Pin silvestri), from Finland
    # input: diameter D in cm (range 0.9-50.6), height H in m (1.5-28.3)
    # output: volume in dm³

    # define parameters
    a = 0.036089
    b = 2.01395
    c = 0.99676
    d = 2.07025
    e = -1.07209

    # implement formula
    V = a*(D**b)*(c**D)*(H**d)*(H-1.3)**e
    return V

def stem_volume_formula_150():
    pass

def stem_volume_formula_151():
    pass

def stem_volume_formula_152(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Pinus sylvestris (Scots pine, Mänty, Tall, Furu, Grove den, Pin silvestri) from Finland. The range of valid values for D is 2 cm and above. 
    
    Args:
        D: Diameter at breast height in cm. Recommendend range: 2 cm and above.
        H: Tree height in m.
        
    Returns:
        V: Stem volume in dm3.
    """
       #coefficients
    a=0.095
    b=1.9185
    c=0.7381


    V = a*D**b*H**c
    return V

def stem_volume_formula_153(D, H):
    # reference: Vuokila, Y. 1965. Functions for variable density yield tables of pine based on temporary sample plots. Communicationes Instituti Forestalis Fenniae 60(4): 1–86.
    # Pinus sylvestris (Scots pine, Mänty, Tall, Furu, Grove den, Pin silvestri), from Finland
    # input: diameter D in cm, height H in m
    # output: volume in dm3

    # coefficients 
    a = 0.05782
    b = 0.11632
    c = -0.01092
    d = -0.01317

    # equation 
    V = a * H * D**2 + b * D * H + c * D**3 + d * D * H**2
    return V

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

def stem_volume_formula_160(D,H):
    
    # Pinus sylvestris - Netherlands
    # D = cm | H = m  | V = dm³

    # coefficients
    a = 1.82075
    b = 1.07427
    c = -2.8885

    # equation  
    V = D ** a * H ** b * math.exp(c)

    # volume
    return V

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

def stem_volume_formula_165(D, H):
    # Reference: Brantseg, A. 1967. Furu sønnafjells: kubering av stående skog, funksjoner og tabeller. Meddelelser fra det Norske Skogforsøksvesen 84: 689–739. 
    # for Pinus sylvestris (Scots pine, Mänty, Tall, Furu, Grove den, Pin silvestri), from Norway
    # input: diameter D in cm (range - 12), height H in m
    # output: volume in dm³

    # define parameters
    a = 0.6716
    b = 0.075708
    c = 0.029679
    d = 0.004341

    # implement formula
    V = a+b*D**2+c*D**2*H+d*D*H**2
    return V

def stem_volume_formula_166():
    pass

def stem_volume_formula_167():
    pass

def stem_volume_formula_168(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Pinus sylvestris (Scots pine, Mänty, Tall, Furu, Grove den, Pin silvestri) from Norway. The range of valid values for D is 0 cm and above. 
    
    Args:
        D: Diameter at breast height in cm. Recommendend range: 0 cm and above.
        H: Tree height in m.
        
    Returns:
        V: Stem volume in dm3.
    """
       #coefficients
    a=2.9361
    b=0.038906
    
    
    V = a+b*D**2*H
    return V

def stem_volume_formula_169(D, H):
    # reference: Giurgiu, V. 1974. O expresie matematica unica a relatiei diametru – înaltime – volum, pentru majoritatea speciilor forestiere din Romania. Silvicultura si Exploatarea Padurilor 89(4): 173–178
    # Pinus sylvestris (Scots pine, Mänty, Tall, Furu, Grove den, Pin silvestri), Romania
    # input: diameter D in cm, height H in m
    # output: volume in m3
    
    # coefficients 
    a = 0.00014808
    b = 1.8341
    c = -0.0448
    d = 0.3115
    e = 0.3525

    # equation 
    V = a * 10**(b * math.log10(D) + c * math.log10(D)**2 + d * math.log10(H) + e * math.log10(H)**2)

    return V

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

def stem_volume_formula_176(D,H):
    
    # Pinus sylvestric - Sweden
    # D = cm | H = m  | V = dm³

    # coefficients
    a = 0.1072		
    b = 0.02427
    c = 0.007315

    # equation  
    V = a * D**2 + b * D**2 * H + c * D * H**2

    # volume
    return V

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

def stem_volume_formula_181(D, H):
    # Reference: Schelhaas, M.J., Nabuurs, G.J., Jans, W.W.P., Moors, E.J., Sabaté, S. & Daamen, W.P. 00 . Converging estimates of the forest carbon sink. Alterra-rapport 631: 1–44. 
    # for Populus spp. (Poplar, Plop), from the Netherlands
    # input: diameter D in mm, height H in m (seed trees)
    # output: volume in dm³

    # define parameters
    a = 0.0009507
    b = 1.895629295
    c = -0.00773694
    d = 0.8392146

    # implement formula
    V = a*D**(b+c)*H**d
    return V

def stem_volume_formula_182():
    pass

def stem_volume_formula_183():
    pass

def stem_volume_formula_184(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Populus spp. (Poplar, Plop) from UK. 
    
    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.
        
    Returns:
        V: Stem volume in dm3.
    """
       #coefficients
    a=-0.004298
    b=0.0000435
    c=0.89


    V = a+b*D**2*H**c
    return V

def stem_volume_formula_185(D, H):
    # reference: 1 Børset, O. 1954. Kubering av osp på rot. Meddelelser fra det norske Skogforsøksvesen 12: 391–447
    # Populus tremula (Aspen, Plop tremulator), Norway
    # input: diameter D in cm, height H in m
    # output: volume in dm3

    # coefficients
    a = 9.69
    b = 0.0365

    # equation
    V = a + b * (D**2) * H

    return V

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

def stem_volume_formula_192(D,H):
    
    # Prunus avium - Belgium
    # D = cm | H = m | V = m³

    # coefficients
    a = -0.002311
    b = -0.00117728
    c = 0.000149061
    d = -7.8058e-6
    e = 3.3282e-4
    f = 3.1526e-5

    # equation  
    V = a + b * D + c * D**2 + d * D**3 + e * H + f * D**2 * H 

    # volume
    return V

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

def stem_volume_formula_197(D, H):
    # Reference: Schelhaas, M.J., Nabuurs, G.J., Jans, W.W.P., Moors, E.J., Sabaté, S. & Daamen, W.P. 00 . Converging estimates of the forest carbon sink. Alterra-rapport 631: 1–44. 
    # for Pseudotsuga spp., from the Netherlands
    # input: diameter D in mm, height H in m
    # output: volume in dm³

    # define parameters
    a = 0.00095916
    b = 2.092560524
    c = 0.000297255
    d = 0.48824344

    # implement formula
    V = a*D**(b+c)*H**d
    return V

def stem_volume_formula_198():
    pass

def stem_volume_formula_199():
    pass

def stem_volume_formula_200(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Quercus grisea (Gray oak, Stejar brumariu) from Romania. 
    
    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.
        
    Returns:
        V: Stem volume in dm3.
    """
       #coefficients
    a=0.00007188
    b=1.4486
    c=0.0204
    d=1.4084
    e=0.0409

    

    V = a*10**(b*math.log10**(D)+c*math.log10**(D)**2+d*math.log10**(H)+e*math.log10**(H)**2)
    return V

def stem_volume_formula_201(D, H):
    # reference: Brandini, P. & Tabacchi, G. 1996. Biomass and volume equations for holm oak and straberry-tree in coppice stands of Southern Sardinia. ISAFA Communicazioni di Ricerca 96(1): 59–69.
    # Quercus ilex (Holm oak), Italy
    # input: diameter D in cm, height H in m
    # output: volume in dm3

    # coefficients
    a = 1.1909
    b = 0.038639

    # equation 
    V = a + b * (D**2) * H

    return V

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

def stem_volume_formula_208(D,H):
    
    # Quercus rubra - Belgium
    # D = cm | H = m | V = m³

    # coefficients
    a = -0.02149
    b = 0.002986681
    c = -4.2506e-5
    d = -2.1806e-6
    e = -0.000743
    f = 3.7473e-5

    # equation  
    V = a + b * D + c * D**2 + d * D**3 + e * H + f * D**2 * H

    # volume
    return V

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

def stem_volume_formula_213(D, H):
    # Reference: Schelhaas, M.J., Nabuurs, G.J., Jans, W.W.P., Moors, E.J., Sabaté, S. & Daamen, W.P. 00 . Converging estimates of the forest carbon sink. Alterra-rapport 631: 1–44. 
    # for  Quercus spp. (Oak, chênes, Stejar), from the Netherlands
    # input: diameter D in mm, height H in m
    # output: volume in dm³

    # define parameters
    a = 0.00095853
    b = 2.040672356
    c = 0.001965013
    d = 0.56366437

    # implement formula
    V = a*D**(b+c)*H**d
    return V

def stem_volume_formula_214():
    pass

def stem_volume_formula_215():
    pass

def stem_volume_formula_216(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for  Quercus spp. (Oak, chênes, Stejar) from Romania. 
    
    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.
        
    Returns:
        V: Stem volume in dm3.
    """
       #coefficients
    a=0.00008839
    b=1.8905
    c=0.0469
    d=0.8059
    e=-0.0045

    V = a*10**(b*math.log10**(D)+c*math.log10**(D)**2+d*math.log10**(H)+e*math.log10**(H)**2)
    return V

def stem_volume_formula_217(D, H):
    # reference: Broadmeadow, M. & Matthews, R. 2004. Survey methods for Kyoto Protocol monitoring and verification of UK forest carbon stocks. UK Emissions by Sources and Removals by Sinks due to Land Use, Land Use Change and Forestry Activities, Report (June 2004). CEH, Edinburgh.
    # Quercus spp. (Oak, Chênes, Stejar), UK
    # input: diameter D in cm, height H in m
    # output: volume in m3
    
    # coefficients
    a = -0.011724
    b = 0.0000765
    c = 0.75

    # equation 
    V =  a + b * (D**2) * (H**c)

    return V

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

def stem_volume_formula_224(D,H):
    
    # Thuja pilicata - Norway
    # D = cm | H = m | V = dm³

    # coefficients
    a = 1.3057
    b = 3.9075
    c = 1.9832
    d = -2.3337
    e = -1.3024

    # equation  
    V = a * H**b * D**c * (H - 1.3)**d * (D + 40)**e

    # volume
    return V

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

def stem_volume_formula_229(D, H):
    # Reference: Dik, E.J. 1984. Estimating the wood volume of standing trees in forestry practice. Rijksinstituut voor onderzoek in de bos en landschapsbouw de Dorschkamp, Wageningen. Uitvoerige verslagen 19(1): 1–114. 
    # for Ulmus spp. (Elm, Orme, Ulm), from the Netherlands
    # input: diameter D in cm, height H in m
    # output: volume in dm³

    # define parameters
    a = 1.94295
    b = 1.29229
    c = -4.20064

    import math

    # implement formula
    V = D**a*H**b*math.exp(c)
    return V

def stem_volume_formula_230():
    pass

