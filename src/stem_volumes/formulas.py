"""
This module implements the 230 stem volume formulas from Silva Fennica by
Zianis et al.

The different formulas are based on Appendix B (starting on page 44) and
Appendix C (starting page 52) of the monograph. It can be downloaded at
https://doi.org/10.14214/sf.sfm4. An Excel file covering Appendix B and C is
avaiable at https://jukuri.luke.fi/handle/10024/512732.
"""

import math

def stem_volume_formula_1(D, H):
    """
    Calculate the stem volume for a standing tree.

    This formula is implemented from Zianis et al. (2005) and is recommended for Silver fir from Norway. 
    The diameter should be 5 cm or greater.

    Args:
        D (float): Diameter of the tree in cm.
        H (float): Height of the tree in m.

    Returns:
        V (float): The calculated stem volume in dm3.
    """

    # Define parameters
    a=1.6662
    b=3.2394
    c=1.9335
    d=-1.8997
    e=-0.9739

    # Implement formula
    V = a * H**b * D**c * (H - 1.3)**d * (D + 100)**e
    return V

def stem_volume_formula_2(D, H):
    """
    This formula is implemented from Zianis et al. (2005).
    Calculate the stem volume of a tree based on diameter and height.

    Species: Abies grandis (Grand fir)  
    Country: Netherlands

    Args:
        D (float): Diameter at breast height in cm.
        H (float): Tree height in m.

    Returns:
        float: Stem volume in dm3.
    """
     # Define parameters
    a = 1.77220
    b = 0.96736
    c = -2.45224
     # Implement formula
    V = (D ** a) * (H ** b) * math.exp(c) # Formula - Abies grandis (Grand fir)(Netherland)
    return V

def stem_volume_formula_3(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.

    Returns:
        V: Stem volume in dm3.
    """

    # Coefficients
    a = 1.6662
    b = 3.2394
    c = 1.9334
    d = -1.8997
    e = -0.9739

    # Formula implementation
    V = a * H ** b * D ** c * (H - 1.3) ** d * (D + 100) ** e
    return V

def stem_volume_formula_4(D):
    """
    Species:    Abies sibirica
    Location:   Germany 

    Args:
        D: Diameter at breast height in cm. Recommendend range: 10-48cm.

    Returns:
        V: Stem volume in m3.
    """

    a = 0.0001316
    b = 2.52
     
    V = a*D**b 
    return V

def stem_volume_formula_5(D, H):

    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Abies spp. (Fir) from Austria. The range of valid values for D is 0.1 dm and above. 
    It was originally published in Pollanschütz, J. 1974. Formzahlfunktionen der Hauptbaumarten Österreichs. Allgemeine Forstzeitung 85: 341–343.
    
    Args:
        D: Diameter at breast height in dm. Recommendend range: 0.1 dm and above.
        H: Tree height in dm.
        
    Returns:
        V: Stem volume in dm3.
    """
    
    import math

    a = 0.580223


    
    b = -0.0307373
    c = -17.1507
    d = 0.089869
    e = -0.080557
    f = 19.661
    g = -2.4584

    V = (math.pi/4)*(a*D**2*H+b*D**2*H*math.log(D)**2+c*D**2+d*D*H+e*H+f*D+g)
    return V

def stem_volume_formula_6(D: float, H: float) -> float:
    """Calculate the stem volume of a tree based on diameter and height.

    Species: Abies spp. (Fir, Brad)  
    Country: Austria

    n = unknown, r2 = 0.848
    
    Original source: Schieler, K. 1988. Diploma thesis, Institute for Forest growth and Yield Research,
    University for Agricultural Sciences, Vienna.

    Args:
        D (float): Diameter at breast height in dm. Recommended range: 0.5-1.04 cm.
        H (float): Tree height in dm.

    Returns:
        float: Stem volume in dm3.
    """

    # Coefficients
    a = 0.560673
    b = 0.15468
    c = -0.65583
    d = 0.033210
    
    # Calculate volume
    V = (math.pi/4) * (a * D**2 * H + b * D**2 * H * math.log(D)**2 + c * D**2 + d * D * H)
    
    return V

def stem_volume_formula_7(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 4.52e-05
    b = 2.1554
    c = -0.1067
    d = 0.938
    e = 0.0228
    V = a * 10 ** (b * math.log10(D) + c * math.log10(D) ** 2 + d * math.log10(H) + e * math.log10(H) ** 2)
    return V

def stem_volume_formula_8(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Acacia spp. (Salcim) from Romania. 
    
    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.
        
    Returns:
        V: Stem volume in m3.
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
    """
    Calculate the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis et al., (2005) and is recommended for Acer pseudoplatanus (Maple), from Belgium.
    No valid range for D and H is given. 

    Args:
        D: Diameter at breast height in cm.
        H: Tree Height in m.
    
    Returns:
        V: Stem volume in m3
    
    
    """

    a = 0.010343
    b = -0.00450536
    c = 0.0003407
    d = -0.000004042
    e = 0.00077115
    f = 0.000029836

    V = a+b*D+c*(D**2)+d*(D**3)+e*H+f*(D**2)*H
    return V

def stem_volume_formula_10(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 1.89756
    b = 0.97716
    c = -2.94253
    V = D ** a * H ** b * math.exp(c)
    return V

def stem_volume_formula_11(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    Species: Acer pseudoplatanus
    Location: Romania

    Reference: Giurgiu, V. 1974. O expresie matematica unica a relatiei diametru - înaltime - volum, pentru majoritatea speciilor forestiere din Romania. Silviculturasi Exploatarea Padurilor 89(4): 173-178.

    Args:
        D: Diameter at breast height in cm. 
        H: Tree height in m.
    
    Returns:
        V: Volume in m3.
    """

    # # Import the log10 function from the math package
    # from math import log10

    # Define the coefficients
    a = 0.00035375
    b = 1.02
    c = 0.3997
    d = 0.666
    e = 0.021
    
    # Calculate the volume according to the formula given by Zianis et al.
    V = a * 10**(b * math.log10(D) + c * math.log10(D)**2 + d * math.log10(H) + e * math.log10(H)**2)

    # Return the calculated volume
    return V

def stem_volume_formula_12(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in m3.
    """

    a = -0.012668
    b = 7.37e-05
    c = 0.75
    V = a + b * D ** 2 * H ** c
    return V

def stem_volume_formula_13(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in m3.
    """

    a = 0.00065013
    b = 1.675
    c = 0.1001
    d = -0.499
    e = 0.5902
    V = a * 10 ** (b * math.log10(D) + c * math.log10(D) ** 2 + d * math.log10(H) + e * math.log10(H) ** 2)
    return V

def stem_volume_formula_14(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 1.85749
    b = 0.88675
    c = -2.5222
    V = D ** a * H ** b * math.exp(c)
    return V

def stem_volume_formula_15(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 8.6524
    b = 0.076844
    c = 0.031573
    V = a + b * D ** 2 + c * D ** 2 * H
    return V

def stem_volume_formula_16(D, H):
    """
    Calculates the volume of the stem of a standing tree.
        
    This formula is implemented from Zianis and is recommended for Alnus glutinosa from Norway. The range of valid values for D is 0-12 cm. 
    Original source is Brantseg (1967) - https://hdl.handle.net/11250/2988649.

    Args:
        D: Diameter at breast height in cm. Recommendend range: 0-12 cm.
        H: Tree height in m.
            
    Returns:
        V: Stem volume in dm3.
    """    
    a = 0.6716
    b = 0.75708
    c = 0.029679
    d = 0.004341
 
    V = a + b * D**2 + c * D**2 * H + d * H**2 * D
    return V

def stem_volume_formula_17(D, H):
    # Alnus glutinosa (Black alder, Klibbal) in Sweden

    """
    Calculate the stem volume for a standing tree of Alnus glutinosa (Black alder, Klibbal) in Sweden.

    Original source: Eriksson, H. 1973. Volymfunktioner för stående
    träd av ask, asp, klibbal och contorta-tall. Institutionen för Skogsproduktion, 
    Royal college of Forestry, Stockholm. Research Notes 6: 1– 6.

    Args:
        D (float): Diameter of the tree in cm.
        H (float): Height of the tree in m.

    Returns:
        V (float): The calculated stem volume in dm3.
    """

    # Define parameters
    a=0.1926
    b=0.01631
    c=0.003755
    d=-0.02756
    e=0.000499

    # implement formula
    V = a * D**2 + b * D**2 * H + c * D * H**2 + d * D * H + e * D**2 * H**2
    return V

def stem_volume_formula_18(D,H):
 
    """
    Calculate the stem volume for a standing tree.

    This formula is implemented from Zianis et al. (2005) and is recommended for Alnus glutinosa (Black alder, Klibbal)from sweden. 
    The diameter should be 5 cm or greater.

    Args:
        D (float): Diameter of the tree in cm.
        H (float): Height of the tree in m.

    Returns:
        V (float): The calculated stem volume in dm3.
    """
    # implement formula
    a=0.05437
    b=1.94505
    c=0.92947
    v = a * (D**b) * (H**c)  #Alnus glutinosa (Black alder, Klibbal)(Sweden)
    return v

def stem_volume_formula_19(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.2264
    b = 0.01347
    c = 0.007665
    d = -0.06669
    e = 0.000428
    V = a * D ** 2 + b * D ** 2 * H + c * D * H ** 2 + d * D * H + e * D ** 2 * H ** 2
    return V

def stem_volume_formula_20(D, H):
    """
    Species:    Alnus incana
    Location:   Norway

    Args:
        D: Diameter at breast height in cm. Recommendend range: 5cm or above.
        H: Tree height in m.

    Returns:
        V: Stem volume in dm3.
    """
    
    a = -1.86827
    b = 0.21461
    c = 0.01283
    d = 0.0138
    e = -0.06311

    V = a + b*D**2 + c*D**2 * H + d*H**2 * D + e*H**2
    return V

def stem_volume_formula_21(D, H):

    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Alnus nigra from Romania.
    It was originally published in Giurgiu, V. 1974. O expresie matematica unica a relatiei diametru – înaltime – volum, pentru majoritatea speciilor forestiere din Romania. Silvicultura si Exploatarea Padurilor 89(4): 173–178.
    
    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.
        
    Returns:
        V: Stem volume in m3.
    """

    import math

    a = 0.00008666
    b = 1.7148
    c = 0.1014
    d = 0.801
    e = 0.0530

    V =  a*10**(b*math.log10(D)+c*math.log10(D)**2+d*math.log10(H)+e*math.log10(H)**2)
    return V    

def stem_volume_formula_22(D: float, H: float) -> float:
    """Calculate the stem volume of a tree based on diameter and height.

    Species: Alnus spp. (Alder)  
    Country: Austria

    n = unknown, r2 = 0.583
    
    Original source: Schieler, K. 1988. Diploma thesis, Institute for Forest growth and Yield Research, 
    University for Agricultural Sciences, Vienna.

    Args:
        D (float): Diameter at breast height in dm. Recommendend range: 0.5-1.04 cm.
        H (float): Tree height in dm.

    Returns:
        float: Stem volume in dm3.
    """

    # Define coefficients
    a = 0.387399
    b = 7.17123
    c = 0.04407
    
    # Calculate volume
    V = (math.pi/4) * (a * D**2 * H + b * D**2 + c * D)
    
    return V

def stem_volume_formula_23(D):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = -0.5547
    b = 0.3757
    V = a+b*D**2
    return V

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
    """
    Calculate the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis et al., (2005) and is recommended for Betula spp. (Birch), from Belgium.
    No valid range for D and H is given. 

    Args:
        D: Diameter at breast height in cm.
        H: Tree Height in m.
    
    Returns:
        V: Stem volume in m3
    """

    a = -0.011392
    b = -0.00031447
    c = 0.000279211 
    d = -0.0000057966
    e = -0.00059573
    f = 0.000030409

    V = a+b*D+c*(D**2)+d*(D**3)+e*H+f*(D**2)*H
    return V

def stem_volume_formula_26(D):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.

    Returns:
        V: The calculated stem volume in ln(dm3).
    """

    # Coefficients
    a = -2.09787
    b = 2.55058

    # Formula implementation
    V = a + b * math.log(D)
    return V

def stem_volume_formula_27(D):
    """
    Calculates the volume of the stem of a standing tree.
    
    Species: Betula spp.
    Location: Finland
    
    Reference: Laasasenaho, J. 1982. Taper curve and volume functions for pine, spruce and birch. Communicationes Instituti Forestalis Fenniae 108: 1-74.

    Args:
        D: Diameter at breast height in cm. Recommended range: 1.2-49.7 cm.
    
    Returns:
        V: Volume in dm3.
    """

    # # Import the natural logarithm function from the math package
    # from math import log 

    # # Raise ValueError if the diameter is out of range
    # if D < 1.2 or D > 49.7: 
    #     raise ValueError("Diameter must be between 1.2 and 49.7 cm.")

    # Define the coefficients
    a = -5.41948
    b = 3.57630	
    c = 2
    d = 1.25
    e = -0.0395855

    # Calculate the volume according to the formula given by Zianis et al.
    V = a + b * math.log(c + d * D) + e * D 
    # The calculated volume seems to be unrealistically low, however the implementation of the formula is according to the original paper. Furthermore, D values below 2.13 result in negative volumes, which is not possible. This contradicts the recommended range of 1.2-49.7 cm.
   
    # Return the calculated volume
    return V

def stem_volume_formula_28(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.011197
    b = 2.10253
    c = 0.986
    d = 3.98519
    e = -2.659
    V = a * D**b * c**D * H**d * (H - 1.3)**e
    return V

def stem_volume_formula_29(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Original Source: Hakkila, P. 1979. Wood density survey and dry weight tables for pine, spruce and birch stems in Finland. communicationes Instituti Forestalis Fenniae 96(3): 1–59.
    Link (pdf): https://jukuri.luke.fi/bitstream/handle/10024/522505/951-40-0470-1.pdf?sequence=1&isAllowed=y
    NOTE: the unit of volume was wrong in Zianis et al., the formula gives the volume in ln(dm3) according to the original publication (see pdf pp. 138).
    
    Species: Betula spp. (Birch) 
    Country: Finland

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in ln(dm3).
    """

    a = -4.4759
    b = 2.0851
    c = 4.0691
    d = -2.7375
    e = -0.013311
    V = a + b * math.log(D) + c * math.log(H) + d * math.log(H - 1.3) + e * D
    return V

def stem_volume_formula_30(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Issue resulted from the V unit of measure stated from Ziania et al. (2005). The original paper (Braastad, H., 1966) used dm3 instead of m3 for Volume. 

    Species: Betula spp. (Birch)  
    Country: Norway

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = -1.86827
    b = 0.21461
    c = 0.01283
    d = 0.01380
    e = 0.06311
    V = a + b * D**2 + c * D**2 * H + d * D * H**2 + e * H**2
    return V

def stem_volume_formula_31(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    The unit of the volume as presented in the original paper is dm3, indicating an error from the
    Zianis et al. (2005) paper computation. The original parer from Braastad, H. 1966. Volumtabeller for bjørk. Med
    delelser fra det Norske Skogforsøksvesen 1(1): 3–78. Especifically from table in page 75 and the explanation in
    page 76 confirmed that the volume is in dm3. link: https://shorturl.at/G3PYR .

    Species: Betula spp. (Birch, Björk, Bjørk, Bouleaux, Mesteacan)
    Country: Norway

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.99983
    b = 0.006325
    c = 0.02849
    d = 0.00885
    e = -0.00799
    V = a + b * D**2 + c * D**2 * H + d * D * H**2 + e * H**2
    return V

def stem_volume_formula_32(D, H):
    """
    Calculates the volume of the stem of a standing tree.
        
    This formula is implemented from Zianis and is recommended for Betula spp from Romania.
        
    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.
            
    Returns:
        V: Stem volume in m3.
    """    
    a = 8.141e-5
    b = 2.248
    c = -0.2062
    d = 0.1946
    e = 0.4147

    V = a * 10**(b * math.log10(D) + c * math.log10(D)**2 + d * math.log10(H) + e * math.log10(H)**2)
    return V

def stem_volume_formula_33(D, H):

    """
    Calculate the stem volume for a standing tree of Betula spp. (Birch, Björk, Bjørk, Bouleaux, Mesteacan)
    in Sweden.

    Original source: Näslund, M. 1947. Funktioner och tabeller för kubering av stående träd.
    Meddelanden från Statens skogsforskningsinstitutet 36(3): 1–81.

    Args:
        D (float): Diameter of the tree in cm. Recommended range: 5 cm - 34.9 cm.
        H (float): Height of the tree in m. Recommended range: 5 m - 26.9 m.

    Returns:
        V (float): The calculated stem volume in dm3.
    """

    # Define parameters
    a=0.1305
    b=0.01338
    c=0.01757
    d=-0.05606

    # Implement formula
    V = a * D**2 + b * D**2 * H + c * D * H**2 + d * H**2
    return V

def stem_volume_formula_34(D,H):  
    """
    Calculate the stem volume for a standing tree git of Betula spp. (Birch) from Sweden.
    This formula is implemented from Zianis et al. (2005).The Diameter should be biger than 4.5 and the height should be bigger than 6. 
        Args:
        D (float): Diameter of the tree in cm.
        H (float): Height of the tree in m.

    Returns:
        float: The calculated stem volume in dm3
    """
    # Define parameters
    a=-0.89359
    b=2.27954
    c=-1.18672
    d=7.07362
    e=-5.45175
    V = (10**a)* (D**b)* ((D*20)**c) * (H**d) * ((H-1.3)**e)
    #Betula spp. (Birch, Björk, Bjørk, Bouleaux, Mesteacan)(sweeden)
    return V

def stem_volume_formula_35(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = -0.93631
    b = 2.30212
    c = -1.40378
    d = 8.01817
    e = -6.18825
    V = 10 ** a * (D ** b) * ((D + 20) ** c) * (H ** d) * (H - 1.3) ** e
    return V

def stem_volume_formula_36(D, H):
    """
    Species:    Betula spp.
    Location:   Sweden

    Args:
        D: Diameter at breast height in cm. Recommendend range: 4.5cm or above.
        H: Tree height in m. Recommendend range: 6m or above.

    Returns:
        V: Stem volume in dm3.
    """

    a = -0.44224
    b = 2.47580
    c = -1.40854
    d = 5.16863
    e = -3.77147

    V = 10**a * D**b * (D+20)**c * H**d * (H-1.3)**e
    return V

def stem_volume_formula_37(D, H):
    
    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Betula spp. (Birch) from Sweden. The range of valid values for D is 4.5 cm and above; for H it is 6 m and above. 
    It was originally published in Brandel, G. 1990. Volumfunktioner för enskilda träd. Sveriges lantbruksuniversitet, Institutionen för skogsproduktion, Rapport 6: 1–181.
    
    Args:
        D: Diameter at breast height in cm. Recommendend range: 4.5 cm and above.
        H: Tree height in m. Recommendend range: 6 m and above.
        
    Returns:
        V: Stem volume in dm3.
    """

    a = -0.35394
    b = 2.52141
    c = -1.54257
    d = 4.88165
    e = -3.47422

    V = 10**a * D**b * (D+20)**c * H**d * (H-1.3)**e
    return V

def stem_volume_formula_38(D: float, H: float) -> float:
    """Calculate the stem volume of a tree based on diameter and height.

    Species: Betula spp. (Birch, Björk, Bjørk, Bouleaux, Mesteacan)  
    Country: Sweden

    n=1363, r2 = unknown
    
    Original source: Näslund, M. 1947. Funktioner och tabeller för kubering av stående träd. 
    Meddelanden från Statens skogsforskningsinstitutet 36(3): 1-81.
    
    Args:
        D (float): Diameter at breast height in cm. Recommendend range: 5-34.9 cm.
        H (float): Tree height in m. Recommendend range: 5-26.9 m.

    Returns:
        float: Stem volume in dm3.
    """

    # Define coefficients
    a = 0.1432
    b = 0.008561
    c = 0.02180
    d = -0.06630

    # Calculate volume
    V = a * D**2 + b * D**2 * H + c * D * H**2 + d * H

    return V

def stem_volume_formula_39(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in m3.
    """

    a = -0.009184
    b = 6.73e-05
    c = 0.75
    V = a + b * D**2 * H**c
    return V

def stem_volume_formula_40(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for  Carpinus spp. from Netherlands. 
    
    Args:
        D: Diameter at breast height in mm.
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
    """
    Calculate the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis et al., (2005) and is recommended for Carpinus spp, from Netherlands.
    No valid range for D and H is given. 

    Args:
        D: Diameter at breast height in mm.
        H: Tree Height in m.
    
    Returns:
        V: Stem volume in dm3
    """

    a = 0.00021491
    b = 2.258957614
    c = -0.01120638
    d = 0.60291075

    V = a*(D**(b+c))*(H**d)
    return V

def stem_volume_formula_42(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in mm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.00021491
    b = 2.258957614
    c = -0.00956695
    d = 0.60291075
    V = a * D**(b + c) * H**d
    return V

def stem_volume_formula_43(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    Species: Chamaecyparis lawsoniana
    Location: Netherlands
    
    Reference: Dik, E.J. 1984. Estimating the wood volume of standing trees in forestry practice. Rijksinstituut voor onderzoek in de bos en landschapsbouw de Dorschkamp, Wageningen. Uitvoerige verslagen 19(1): 1-114.

    Args:
        D: Diameter at breast height in cm. Recommended range: 5 cm or more.
        H: Tree height in m.
    
    Returns:
        V: Volume in dm3.
    """

    # # Import the exponential function from the math package
    # from math import exp

    # Define the coefficients
    a = 1.85298
    b = 0.86717
    c = -2.33706

    # Calculate the volume according to the formula given by Zianis et al.
    V = D**a * H**b * math.exp(c)

    # Return the calculated volume
    return V 

def stem_volume_formula_44(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = -1.86827
    b = 0.21461
    c = 0.01283
    d = 0.0138
    e = -0.06311
    V = a + b * D ** 2 + c * D ** 2 * H + d * D * H ** 2 + e * H ** 2
    return V

def stem_volume_formula_45(D,H):
    """
    Calculates the volume of the stem of a standing tree. This formula is implemented from Zianis and is recommended for Fagus spp. (Beech, Fag) from Austria  

    Args:
        D: Diameter at breast height in dm. The Recommended range is 1 and above
        H: Height of the tree in dm.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.989253
    b = -0.0371508
    c = -31.0674
    d = -0.386321
    e = 0.219462
    f = 49.6136
    g = -22.372
    V = (math.pi/4)*(a*D**2*H+b*D**2*H*math.log(D)**2+c*D**2+d*D*H+e*H+f*D+g)
    return V


def stem_volume_formula_46(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in dm.
        H: Height of the tree in dm.

    Returns:
        V: The calculated stem volume in dm3.
    """

    # Coefficients
    a = 0.5173
    b = -13.62144
    c = 9.9888

    V = (math.pi / 4) * (a * D**2 * H + b * D**2 + c * D)
    return V 

def stem_volume_formula_47(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Fagus spp.  
    Country: Romania

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in m3.
    """

    a = 0.0000757
    b = 1.3791
    c = 0.2127
    d = 1.1992	
    e = -0.0584
    V = a * 10 ** (b * math.log10(D) + c * math.log10(D)**2 + d * math.log10(H) + e * (math.log10(H) ** 2))
    return V

def stem_volume_formula_48(D,H):
    """
    Calculates the volume of the stem of a standing tree.
        
    This formula is implemented from Zianis and is recommended for Fagus spp from UK.  
    Original source is Broadmeadow et al (2004) - https://nora.nerc.ac.uk/id/eprint/8644/1/N008644CR.pdf

    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.
        
    Returns:
        V: Stem volume in m3.
    """

    a = -0.014306
    b = 0.0000748
    c = 0.75

    V = a + b * D**2 * H**c
    return V

def stem_volume_formula_49(D, H):

    """
    Calculate the stem volume for a standing tree of Fagus sylvatica (Beech, Rotbuche, Beuk) in Belgium.

    Original Source: Dagnelie, P., Palm, R., Rondeux, J. & Thill, A. 1999.
    Tables de cubage des arbres et des peuplements forestiers. les Presses Agronomiques de
    Gembloux, Gembloux. 1 6 p.

    Args:
        D (float): Diameter of the tree in cm.
        H (float): Height of the tree in m.

    Returns:
        V (float): The calculated stem volume in m3.
    """

    # Define parameters
    a=-0.015572
    b=0.00290013
    c=-7.0476*10**(-6)
    d=2.3935*10**(-6)
    e=-0.0013528
    f=3.9837*10**(-5)

    # Implement formula
    V = a + b * D + c * D**2 + d * D**3 + e * H + f * D**2 * H
    return V

def stem_volume_formula_50(D,H):
    """
    Calculate the stem volume for a standing tree of Fagus sylvatica (Beech, Rotbuche, Beuk) in Germany.
    This formula is implemented from Zianis et al. (2005). The recommended range for diameter is between 10.7 and 61.8. The recommended range for the height is between 10.2 and 34.6.
    Args:
        D (float): Diameter of the tree in cm.
        H (float): Height of the tree in m.

    Returns:
        V (float): The calculated stem volume in m3.
    """
    # Define parameters
    a=-0.015589
    b=0.00001696
    c=0.00001883
    # Implement formula
    V= a * b * D * (H**2) +c * (D**3)
    return V

def stem_volume_formula_51(D,H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in dm.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a=0.016641
    b=0.00072179
    c=2.52e-06
    
    V = a + b * D * H ** 2 + c * D ** 3
    return V

def stem_volume_formula_52(D, H):
    """
    Species:    Fagus sylvatica
    Location:   Netherlands

    Args:
        D: Diameter at breast height in cm. Recommendend range: NA
        H: Tree height in m. Recommendend range: NA

    Returns:
        V: Stem volume in dm3.
    """

    a = 1.55448
    b = 1.55880
    c = -3.57875

    V = D**a * H**b * math.exp(c)
    return V

def stem_volume_formula_53(D, H):

    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Fagus sylvatica (Beech) from the Netherlands.
    It was originally published in De Vries, P.G. 1961. The principle of nomograms applied to the stem volume functions of the volume tables for forest trees grown in the Netherlands. Nederlands Bosbouw Tijdschrift 33(5): 114–1 1.
    
    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.
        
    Returns:
        V: Stem volume in dm3.
    """

    a = 0.049
    b = 1.78189
    c = 1.08345

    V = a * D**b * H**c
    return V

def stem_volume_formula_54(D: float, H: float) -> float:
    """Calculate the stem volume of a tree based on diameter and height.

    Species: Betula spp. Fraxinus exselsior (Ash, Frêne, Es)  
    Country: Belgium

    n = 534, r2 = unknown

    Original source: Dagnelie, P., Palm, R., Rondeux, J. & Thill, A. 1999. 
    Tables de cubage des arbres et des peuplements forestiers. les Presses Agronomiques de Gembloux, Gembloux. 126 p.

    Args:
        D (float): Diameter at breast height in cm.
        H (float): Tree height in m.

    Returns:
        float: Stem volume in m3.
    """

    # Define coefficients
    a = -0.039836
    b = 0.006262765
    c = -0.00015937
    d = -1.9902 * 10**-7
    e = -0.0009834
    f = 3.7872 * 10**-5

    # Calculate volume
    V = a + b * D + c * D**2 + d * D**3 + e * H + f * D**2 * H

    return V

def stem_volume_formula_55(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 1.9577
    b = 0.7706
    c = -2.48079
    
    V = D ** a * H ** b * math.exp(c)
    return V

def stem_volume_formula_56(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for  Fraxinus exselsior (Ash, Frêne, Es) from Sweden. 
    
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
    # reference: Eriksson, H. 1973. Volymfunktioner för ståendeträd av ask, asp, klibbal och contorta-tall. Institutionen för Skogsproduktion, Royal College of Forestry, Stockholm. Research Notes 26: 1-26.
    # Fraxinus exselsior (Ash, Frêne, Es), from Sweden
    # input: diameter D in cm, height H in m
    # output: volume in dm3
    """
    Calculate the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis et al., (2005) and is recommended for Fraxinus exselsior (Ash), from Sweden.
    No valid range for D and H is given. 

    Args:
        D: Diameter at breast height in cm.
        H: Tree Height in m.
    
    Returns:
        V: Stem volume in dm3
    """

    a = 0.03593
    b = 0.03310
    c = 0.04127
 
    V = a * (D**2) * H + b * (D**2) + c * D * H
    return V
    
def stem_volume_formula_58(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.06328
    b = 1.92428
    c = 0.8869
    V = a * D ** b * H ** c
    return V 

def stem_volume_formula_59(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    Species: Fraxinus Excelsior
    Location: Sweden
    
    Reference: Eriksson, H. 1973. Volymfunktioner för stående träd av ask, asp, klibbal och contorta-tall. Institutionen för Skogsproduktion, Royal College of Forestry, Stockholm. Research Notes 26: 1-26.

    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.
    
    Returns:
        V: Volume in dm3.
    """

    # Define the coefficients
    a = 0.03249
    b = 0.02941
    c = 0.03892	

    # Calculate the volume according to the formula given by Zianis et al.
    V = a * D**2 * H + b * D**2 + c * D * H

    # Return the calculated volume
    return V

def stem_volume_formula_60(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.03453
    b = 0.02941
    c = 0.03892
    V = a * D ** 2 * H + b * D ** 2 + c * D * H
    return V

def stem_volume_formula_61(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = -1.86827
    b = 0.21461
    c = 0.01283
    d = 0.0138
    e = -0.06311
    V = a + b * D ** 2 + c * D ** 2 * H + d * D * H ** 2 + e * H ** 2
    return V

def stem_volume_formula_62(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in m3.
    """

    a = 0.00030648
    b = 1.2676
    c = 0.3102
    d = 0.4929
    e = 0.0962
    
    V = a * 10**( b*math.log10(D) + c*math.log10(D)**2 + d*math.log10(H) + e*math.log10(H)**2 )
    return V

def stem_volume_formula_63(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in m3.
    """

    a=-0.012107
    b=7.77e-05
    c=0.75
    V = a + b * D ** 2 * H ** c
    return V

def stem_volume_formula_64(D,H):
    """
    Calculates the volume of the stem of a standing tree.
        
    This formula is implemented from Zianis and is recommended for Larix decidua from Austria. The range of valid values for D is 1 cm and above.
    
    Args:
        D: Diameter at breast height in dm. Recommendend range: 1 cm and above.
        H: Tree height in dm.
            
    Returns:
        V: Stem volume in dm3.
    """

    a = 0.609443
    b = -0.0455748
    c = -18.6631
    d = -0.248736
    e = 0.126594
    f = 36.9783
    g = -14.204
 
    V = (math.pi / 4) * (a * D**2 * H + b * D**2 * H * math.log(D)**2 + c * D**2 + d * D * H + e * H + f * D + g)
    return V

def stem_volume_formula_65(D, H):

    """
    Calculate the stem volume for a standing tree of Larix decidua (larch, Mélèzes) in Austria.

    Original source: Schieler, K. 1988. Diploma thesis, Institute for Forest growth and
    Yield Reserch, University for Agricultural Sciences, Vienna.

    Args:
        D (float): Diameter of the tree in dm. Recommended range: 0.5 dm - 1.04 dm.
        H (float): Height of the tree in dm.

    Returns:
        (float): The calculated stem volume in dm3.
    """

    # Define parameters
    a=0.487270
    b=-2.04291
    c=5.9995

    # Implement formula
    V = (math.pi / 4) * (a * D **2 * H + b * D**2 + c * D)
    return V


def stem_volume_formula_66(D,H):
    
    """
    Calculate the stem volume for a standing tree of Larix decidua (larch, Mélèzes) in Belgium.
    This formula is implemented from Zianis et al. (2005).
    

    Args:
        D (float): Diameter of the tree in cm.
        H (float): Height of the tree in m.

    Returns:
        (float): The calculated stem volume in m3.
    """
    a=-0.03088
    b=0.004676261
    c=-4.8614e-5
    d=-3.8178e-6
    e=-0.0011638
    f=4.0597e-5
    V= a + b*D + c*(D**2) + d*(D**3) + e*H + f*(D**2)*H
    return V

def stem_volume_formula_67(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 1.8667
    b = 1.08118
    c = -3.0488

    return D ** a * H ** b * math.exp(c)

def stem_volume_formula_68(D, H):
    """
    Species:    Larix decidua
    Location:   Norway

    Args:
        D: Diameter at breast height in cm. Recommendend range: 5cm or above.
        H: Tree height in m. Recommendend range: 6m or above.

    Returns:
        V: Stem volume in dm3.
    """
    
    a = 0.7761
    b = 3.6461
    c = 1.9166
    d = -2.3179
    e = -0.8236

    V = a*H**b * D**c * (H-1.3)**d * (D+100)**e
    return V

def stem_volume_formula_69(D, H):

    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Larix hybrid from Norway. The range of valid values for D is 5 cm and above.
    It was originally published in Øen, S., Bauger, E. & Øyen, B.-H. 001. Functionar for volumberekning av framande treslag i Vest-Norge. Aktuelt fra Skogforsk 3/01: 18–19.
    
    Args:
        D: Diameter at breast height in cm. Recommendend range: 5 cm and above.
        H: Tree height in m.
        
    Returns:
        V: Stem volume in dm3.
    """

    a = 0.7761
    b = 3.6461
    c = 1.9166
    d = -2.3179
    e = -0.8236

    V =  a * H**b * D**c * (H-1.3)**d * (D+100)**e
    return V

def stem_volume_formula_70(D: float, H: float) -> float:
    """Calculate the stem volume of a tree based on diameter and height.

    Species: Larix kaempferi (Japanese larch)  
    Country: Netherlands

    n = 1023, r2 = 0.996

    Original source: Dik, E.J. 1984. Estimating the wood volume of standing trees in forestry practice. 
    Rijksinstituut voor onderzoek in de bos en landschapsbouw de Dorschkamp, Wageningen. Uitvoerige verslagen 19(1): 1-114.

    Args:
        D (float): Diameter at breast height in cm.
        H (float): Tree height in m.

    Returns:
        float: Stem volume in dm3.
    """

    # Define coefficients
    a = 1.87077
    b = 1.00616
    c = -2.8748

    # Calculate volume
    V = D**a * H**b * math.exp(c)

    return V

def stem_volume_formula_71(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.7606
    b = 3.5377
    c = 1.9741
    d = -2.1902	
    e = -0.8459
    V = a * H**b * D**c * (H - 1.3)**d * (D + 100)**e
    return V

def stem_volume_formula_72(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Larix sibirica (Siberian larix) from Iceland. The range of valid values for D is 4 cm and above. 
    
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
    """
    Calculate the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis et al., (2005) and is recommended for Larix sibirica (Siberian larix), from Iceland.
    Issue resulted from the V unit of measure stated from Ziania et al. (2005). We were unable to find the original paper, but several papers (inc. Bjarnadoottir B and Signurdsson B, 2007) used dm3 instead of m3 for Volume. 

    The range of valid values for D is 4-34cm, and for H is 4-16m.

    Args:
        D: Diameter at breast height in cm. Recommended range: 4-34cm
        H: Tree Height in m. Recommended range: 4-16m
    
    Returns:
        V: Stem volume in dm3
    """

    a = -2.9946
    b = 1.8105
    c = 0.9908 

    V = math.exp(a) * (D**b) * (H**c)
    return V

def stem_volume_formula_74(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    The formula is given in "Single-tree biomass and stem volume functions for
    eleven tree species used in Icelandic forestry" by Snorrason et al. The
    paper can be found at
    http://ias.is/wp-content/uploads/Single-tree-biomass-and-stem-volume-functions-for.pdf.
    The volume formula is given in Table 1 (see Volume for Siberian larch).
    The volume unit of m3 in Zianis et al. is not properly copied. In the paper
    after equation 1 on page 18 you can verify that the formula reports the
    volume in dm3.

    Species: Larix sibirica (Siberian larch)
    Country: Iceland

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.0983
    b = 1.551
    c = 1.1483
    V = a * D ** b * H ** c
    return V


def stem_volume_formula_75(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    Species: Larix sibirica
    Location: Norway
    
    Reference: Øen, S., Bauger, E. & Øyen, B.-H. 2001. Functionar for volumberekning av framande treslag i Vest-Norge. Aktuelt fra Skogforsk 3/01: 18-19.

    Args:
        D: Diameter at breast height in cm. Recommended range: 5 cm or more.
        H: Tree height in m.
    
    Returns:
        V: Volume in dm3.
    """

    # Raise ValueError if the diameter is out of range
    # if D < 5:
    #     raise ValueError("Diameter must be at least 5 cm.")

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

def stem_volume_formula_76(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.5
    b = 0.0753
    c = 0.03345
    d = -0.00243
    V = a + b * D ** 2 + c * D ** 2 * H + d * H ** 2 * D
    return V

def stem_volume_formula_77(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.4
    b = -0.01
    c = 0.03355
    d = -0.00359
    V =  a + b * D**2 + c * D**2 * H + d * H**2 * D
    return V

def stem_volume_formula_78(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in mm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.00035217
    b = 2.12841828
    c = 0.003292718
    d = 0.76283925

    V = a * D ** (b + c) * H ** d
    return V

def stem_volume_formula_79(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in mm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.00035217
    b = 2.12841828
    c = -0.1054168
    d = 0.76283925

    V = a * D ** (b + c) * H ** d
    return V

def stem_volume_formula_80(D,H):
    """
    Calculates the volume of the stem of a standing tree.
        
    This formula is implemented from Zianis and is recommended for Larix spp from Netherlands. 
    Original source is Schelhaas et al (2002) - https://library.wur.nl/WebQuery/wurpubs/reports/320536
    Args:
        D: Diameter at breast height in mm.
        H: Tree height in m.
            
    Returns:
        V: Stem volume in dm3.
    """    
    a = 0.00035217
    b = 2.12841828
    c = -0.0026067	
    d = 0.76283925

    V = a * D**(b + c) * H**d
    return V

def stem_volume_formula_81(D, H):

    """
    Calculate the stem volume for a standing tree of Larix spp. (lehtikuusi, lork, larice) in Romania.

    Original source: Giurgiu, V. 1974. O expresie matematica unica a relatiei diametru – înaltime – volum, 
    pentru majoritatea speciilor forestiere din Romania. Silvicultura si Exploatarea Padurilor 
    89(4): 173–178.

    Args:
        D (float): Diameter of the tree in cm.
        H (float): Height of the tree in m.

    Returns:
        V (float): The calculated stem volume in m3.
    """

    # Define parameters
    a=2.822*10**(-5)
    b=2.2060
    c=-0.1136
    d=1.115
    e=0.0129

    # Implement formula
    V = a * 10**(b * math.log10(D) + c * math.log10(D)**2 + d * math.log10(H) + e * math.log10(H)**2)
    return V

def stem_volume_formula_82(D,H):

    """
    Calculate the stem volume of a tree based on diameter and height.
    This formula is implemented from Zianis et al. (2005). The Diameter should be biger than 1.
    

    Species: picea abies (Norway spruce, Kuusi, Gran, Epicéa, Fijnspar) from Austria.
    Country: Netherlands

    Args:
        D (float): Diameter at breast height in dm.
        H (float): Tree height in dm.

    Returns:
        float: Stem volume in dm3.
    """
    # Define parameters
    a=0.46818
    b=-0.013919
    c=-28.213
    d=0.37474
    e=-0.28875
    f=28.279
    # Implement formula
    v= (math.pi / 4) * (
    a * D**2 * H +
    b * D**2 * H * (math.log(D))**2 +
    c * D**2 +
    d * D * H +
    e * H +
    f * D
)
 
    return v
     

def stem_volume_formula_83(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in dm.
        H: Height of the tree in dm.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.563443
    b = -0.12731
    c = -8.55022
    d = 7.6331
    V = (math.pi / 4) * (a * D**2 * H + b * D**2 * H * (math.log(D)**2) + c * D**2 + d * D)
    return V

def stem_volume_formula_84(D, H):
    """
    Species:    Picea abies
    Location:   Belgium

    Args:
        D: Diameter at breast height in cm. Recommendend range: NA.
        H: Tree height in m. Recommendend range: NA.

    Returns:
        V: Stem volume in m3.
    """
    
    a = -0.010929       
    b = 0.004380951     
    c = -0.000094713    
    d = -0.0000078024   
    e = -0.0027922      
    f = 0.00004834610   

    V = a + b*D + c*D**2 + d*D**3 + e*H + f*D**2 * H
    return V 

def stem_volume_formula_85(D):

    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Picea abies (Norway spruce) from Czech Republic.
    It was originally published in Cerný, M. 1990. Biomass of Picea abies (l.) Karst. in midwestern Bohemia. Scandinavian Journal of Forest Research 5: 83–95.
    
    Args:
        D: Diameter at breast height in cm.
        
    Returns:
        V: Stem volume in m3.
    """

    a = 0.00059707
    b = 2.1286

    V =  a * D**b
    return V

def stem_volume_formula_86(D: float, H: float) -> float:
    """Calculate the stem volume of a tree based on diameter and height.

    Species: Picea abies (Norway spruce, Kuusi, Gran, Epicéa, Fijnspar)  
    Country: Czech Republic

    n = 26, r2 = 0.98
    
    Original source: Cerný, M. 1990. Biomass of Picea abies (l.) Karst. in midwestern Bohemia. 
    Scandinavian Journal of Forest Research 5: 83-95.
    
    Args:
        D (float): Diameter at breast height in cm.
        H (float): Tree height in m.

    Returns:
        float: Stem volume in m3.
    """

    # Define coefficients
    a = 0.00011261 
    b = 0.87852
    
    # Calculate volume
    V = a * (H * D**2)**b
    
    return V

def stem_volume_formula_87(D):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.

    Returns:
        V: The calculated stem volume in ln(dm3).
    """

    a=-2.41218
    b=2.62463

    V = a + b * math.log(D)
    return V

def stem_volume_formula_88(D):
    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Picea abies (Norway spruce, Kuusi, Gran, Epicéa, Fijnspar) from Finland. The range of valid values for D is 1.5 cm and above. 
    
    Args:
        D: Diameter at breast height in cm. Recommendend range: 1.5 cm and above.

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
    """
    Calculate the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis et al., (2005) and is recommended for Picea abies (Norway spruce), from Finland.
    The range of valid values for D is 1.5-61.9cm, and for H is 1.8-32.7m.

    Args:
        D: Diameter at breast height in cm. Recommended range: 1.5-61.9cm
        H: Tree Height in m. Recommended range: 1.8-32.7m
    
    Returns:
        V: Stem volume in dm3
    """

    a = 0.022927
    b = 1.91505
    c = 0.99146 
    d = 2.82541
    e = -1.53547

    V = a * (D**b) * (c**D) * (H**d) * ((H-1.3)**e)
    return V

def stem_volume_formula_90(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in ln(dm3).
    """

    a = -3.7544
    b = 1.896
    c = 2.8979
    d = -1.602
    e = -0.007827
    V = a + b * math.log(D) + c * math.log(H) + d * math.log(H - 1.3) + e * (D)
    return V


def stem_volume_formula_91(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    Species: Picea abies
    Location: Finland
    
    Reference: Kanninen, K., Uusvaara, O. & Valonen, P. 1977.Kokopuuraaka-aineen mittaus ja ominaisuudet. Folia Forestalia 403: 1-53.

    Args:
        D: Diameter at breast height in cm. Recommended range: 2-18 cm.
        H: Tree height in m. Recommended range: 2-18 m.
    
    Returns:
        V: Volume in dm3.
    """

    # # Raise ValueError if the diameter is out of range
    # if D < 2 or D > 18: 
    #     raise ValueError("Diameter must be between 2 and 18 cm.")
    
    # # Raise ValueError if the height is out of range
    # if H < 2 or H > 18:
    #     raise ValueError("Height must be between 2 and 18 m.")

    # Define the coefficients
    a = 0.7877 
    b = 1.9302
    c = 0.79465

    # Calculate the volume according to the formula given by Zianis et al.
    V = a * D**b * H**c
    # Volume tests might be failing because formula is only valid for a dimater range of 2-18 cm and a height range of 2-18 m.

    # Return the calculated volume
    return V

def stem_volume_formula_92(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.10838
    b = 1.8202
    c = 0.77154
    V = a * D ** b * H ** c
    return V

def stem_volume_formula_93(D):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.

    Returns:
        V: The calculated stem volume in ln(dm3).
    """

    a=-2.59385
    b=2.71757
    c=-9.7e-05
    V = a + b * math.log(D) + c * (D) ** 2
    return V

def stem_volume_formula_94(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in m.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in m3.
    """

    a = 0.502
    V = a * H * D ** 2
    return V

def stem_volume_formula_95(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in m.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in m3.
    """

    a = 0.418
    V = a * H * D ** 2
    return V

def stem_volume_formula_96(D,H):
    """
    Calculates the volume of the stem of a standing tree.
        
    This formula is implemented from Zianis and is recommended for Picea abies from Iceland. The range of valid values for D is 2.7-27.9 cm. 
    Original source is Snorrason & Einarsson (2006) - https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=6668a0d8e81f7c32c0a0926d99b3451c9c69c160

    Volume unit different from Zianis! changed from m3 to dm3

    Args:
        D: Diameter at breast height in cm. Recommendend range: 2.7-27.9 cm.
        H: Tree height in m. Recommended range 2.7-12 m.
            
    Returns:
        V: Stem volume in dm3.
    """    
    a = 0.1299
    b = 1.6834
    c = 0.8598

    V = a * D**b * H**c
    return V

def stem_volume_formula_97(D, H):

    """
    Calculate the stem volume for a standing tree of Picea abies (Norway spruce, Kuusi, Gran, Epicéa, Fijnspar) in the Netherlands.

    Original source: De Vries, P.G. 1961. The principle of nomograms applied to the stem volume functions of the volume tables for forest trees grown in the Netherlands. Nederlands Bosbouw Tijdschrift 33(5): 114–1 1.

    Args:
        D (float): Diameter of the tree in mm.
        H (float): Height of the tree in m.

    Returns:
        V (float): The calculated stem volume in dm3.
    """

    # Define parameters
    a=0.00053238
    b=2.164126647
    c=0.004108377
    d=0.54879808

    # Implement formula
    V = a*D**(b+c) * H**d
    return V

def stem_volume_formula_98(D,H):
    
    """
    Calculate the stem volume for a standing tree of Picea abies (Norway spruce, Kuusi, Gran, Epicéa, Fijnspar) in the Netherlands.
    This formula is implemented from Zianis et al. (2005).
    Args:
        D (float): Diameter of the tree in mm.
        H (float): Height of the tree in m.

    Returns:
        V (float): The calculated stem volume in dm3.
    """
    # Define parameters
    a=0.00053238
    b=2.164126647
    c=-0.04670018
    d=0.54879808
    # Implement formula
    V= a * D**(b + c) * H**d #Picea abies (Norway spruce, Kuusi, Gran, Epicéa, Fijnspar)(Neatherlands)
    return V

def stem_volume_formula_99(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in mm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a=0.00053238
    b=2.164126647
    c=-0.0102582
    d=0.54879808
    V = a * D ** (b + c) * H ** d
    return V

def stem_volume_formula_100(D, H):
    """
    Species:    Picea abies
    Location:   Netherlands

    Args:
        D: Diameter at breast height in cm. Recommendend range: NA.
        H: Tree height in m. Recommendend range: NA.

    Returns:
        V: Stem volume in dm3.
    """
    
    a = 1.75055
    b = 1.10897
    c = -2.75863

    V = D**a * H**b * math.exp(c)
    return V  

def stem_volume_formula_101(D, H):

    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Picea abies (Norway spruce) from the Netherlands.
    It was originally published in De Vries, P.G. 1961. The principle of nomograms applied to the stem volume functions of the volume tables for forest trees grown in the Netherlands. Nederlands Bosbouw Tijdschrift 33(5): 114–1 1.
    
    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.
        
    Returns:
        V: Stem volume in dm3.
    """

    a = 0.04143
    b = 1.6704
    c = 1.3337

    V =  a * D**b * H**c
    return V

def stem_volume_formula_102(D: float, H: float) -> float:
    """Calculate the stem volume of a tree based on diameter and height.

    Species: Picea abies (Norway spruce, Kuusi, Gran, Epicéa, Fijnspar)  
    Country: Norway

    n = 2621, r2 = 0.998
    
    Original source: Bauger, E. 1995. Funksjoner og tabeller for kubering av stående trær. 
    Rapport fra Skogforsk(16): 1-26.
    
    Args:
        D (float): Diameter at breast height in cm.
        H (float): Tree height in m.

    Returns:
        float: Stem volume in dm3.
    """

    # Define coefficients
    a = 0.6844
    b = 3.0296
    c = 2.0560
    d = -1.7377
    e = -0.9756

    # Calculate volume
    V = a * H**b * D**c * (H - 1.3)**d * (D + 40)**e

    return V

def stem_volume_formula_103(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a=0.7464
    b=2.496
    c=2.0714
    d=-1.4175
    e=-0.9601
    V = a * H ** b * (D) ** c * (H - 1.3) ** d * (D + 40) ** e
    return V

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
    """
    Calculate the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis et al., (2005) and is recommended for Picea abies (Norway spruce), from Norway.
    The range of valid values for D is 10cm and below, and for H is 39.49m and below.

    Args:
        D: Diameter at breast height in cm. Recommended range: 10cm and below
        H: Tree Height in m. Recommended range: 39.49m and below
    
    Returns:
        V: Stem volume in dm3
    """

    a = 0.52
    b = 0.02403
    c = 0.01463 
    d = -0.10983
    e = 0.15195

    V = a + b * (D**2) * H + c * D * (H**2) + d * (H**2) + e * D * H
    return V

def stem_volume_formula_106(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a=-31.57
    b=0.0016
    c=0.0186
    d=0.63
    e=-2.34
    f=3.2
    V = a + b * (D) * H ** 2 + c * H ** 2 + d * (D) * H + e * H + f * (D)
    return V


def stem_volume_formula_107(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    Species: Picea abies
    Location: Norway
    
    Reference: Vestjordet, E. 1967. Funksjoner og tabeller for kubering av stående gran. Meddelelser fra det Norske Skogforsøksvesen 84: 539-574.

    Args:
        D: Diameter at breast height in cm. Recommended range: 13-59.4 cm.
        H: Tree height in m. Recommended range: Up to 39.49 m.
    
    Returns:
        V: Volume in dm3.
    """

    # # Raise ValueError if the diameter is out of range
    # if D < 13 or D > 59.4:
    #     raise ValueError("Diameter must be between 13 and 59.4 cm.")
    # # Raise ValueError if the height is out of range
    # if H > 39.49:
    #     raise ValueError("Height may be 39.49 m at max.")

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

def stem_volume_formula_108(D,H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a=6.69
    b=0.01308
    c=0.02853
    d=-0.31956
    e=0.28969
    V = a + b * D ** 2 * H + c * D * H ** 2 + d * H ** 2 + e * D * H
    return V

def stem_volume_formula_109(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a=0.46
    b=0.02427
    c=0.01521
    d=-0.18254
    e=0.20994
    V = a + b * D ** 2 * H + c * D * H ** 2 + d * H ** 2 + e * D * H
    return V

def stem_volume_formula_110(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a=0.67
    b=0.03023
    c=0.00712
    d=0.04175
    V = a + b * D ** 2 * H + c * D * H ** 2 + d * D ** 2
    return V

def stem_volume_formula_111(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a=0.28
    b=0.00815
    c=0.03053
    d=-0.50725
    e=0.51643
    V = a + b * D ** 2 * H + c * D * H ** 2 + d * H ** 2 + e * D * H
    return V

def stem_volume_formula_112(D,H):
    """
    Calculates the volume of the stem of a standing tree.
        
    This formula is implemented from Zianis and is recommended for Picea abies from Norway. The range of valid values for D is 0-15 cm and above. 
    Original source is Vestjordet (1967) - https://hdl.handle.net/11250/2988611

    Args:
        D: Diameter at breast height in cm. Recommendend range: 0-15 cm and above.
        H: Tree height in m. Recommended range: 0-39.49 m.
            
    Returns:
        V: Stem volume in dm3.
    """    
    a = 0.3
    b = 0.02593
    c = 0.01268
    d = -0.0977
    e = 0.14586

    V = a + b * D**2 * H + c * D * H**2 + d * H**2 + e * D * H
    return V

def stem_volume_formula_113(D, H):

    """
    Calculate the stem volume for a standing tree of Picea abies (Norway spruce, Kuusi, Gran, Epicéa, Fijnspar) in Norway.

    Original source: Vestjordet, E. 1967. Funksjoner og tabeller for kubering av stående gran. 
    Meddelelser fra det Norske Skogforskningsvesen 84: 539–574.

    Args:
        D (float): Diameter of the tree in cm. The diameter should be between 10 cm and 59.4 cm.
        H (float): Height of the tree in m. The height should be less than 39.49 m.

    Returns:
        V (float): The calculated stem volume in dm3.
    """

    # Define parameters
    a=4.33
    b=0.01491
    c=0.02606
    d=-0.31854
    e=0.31106

    # Implement formula
    V = a + b * D**2 * H + c * D * H**2 + d * H**2 + e * D * H
    return V

def stem_volume_formula_114(D,H):

    
    """
    Calculate the stem volume for a standing tree of Picea abies (Norway spruce, Kuusi, Gran, Epicéa, Fijnspar) in Poland.
    This formula is implemented from ZianisÄ(2005).
   

    Args:
        D (float): Diameter of the tree in cm. 
        H (float): Height of the tree in m.

    Returns:
        V (float): The calculated stem volume in m3.
    """
     # Define parameters
    a=0.666151
    b=0.458507
     #Implement formula
    V= (math.pi / 40000) * H * D * (a + b * D)
    return V

def stem_volume_formula_115(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in m3.
    """

    a=0.53005
    b=1.229283
    V = math.pi / 40000 * H * D * (a * D + b)
    return V

def stem_volume_formula_116(D, H):
    """
    Species:    Picea abies
    Location:   Sweden

    Args:
        D: Diameter at breast height in cm. Recommendend range: 5-55.9cm.
        H: Tree height in m. Recommendend range: 3-34.9m.

    Returns:
        V: Stem volume in dm3.
    """
    
    a = 0.1150
    b = 0.01746
    c = 0.02022	
    d = -0.05618

    V = a*D**2 + b*D**2 * H + c * D * H**2 + d*H**2
    return V     

def stem_volume_formula_117(D, H):

    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Picea abies (Norway spruce) from Sweden.
    It was originally published in Brandel, G. 1974. Volymfunktioner för tall och gran. Skoghögskolan, Institutionen för skogsproduktion, Rapporter och Uppsatser 33: 178–191.
    
    Args:
        D: Diameter at breast height in cm. Recommendend range: 2 cm and above.
        H: Tree height in m. Recommendend range: 2 m and above.
        
    Returns:
        V: Stem volume in dm3.
    """

    a = -0.9513
    b = 1.9781
    c = -0.5254
    d = 2.7604
    e = -1.4684

    V = 10**a * D**b * (D+20)**c * H**d * (H-1.3)**e
    return V

def stem_volume_formula_118(D: float, H: float) -> float:
    """Calculate the stem volume of a tree based on diameter and height.

    Species: Picea abies (Norway spruce, Kuusi, Gran, Epicéa, Fijnspar)  
    Country: Sweden

    n = 2609, r2 = 0.998
    
    Original source: Brandel, G. 1990. Volumfunktioner för enskilda träd. 
    Sveriges lantbruksuniversitet, Institutionen för skogsproduktion, Rapport 26: 1-181.
    
    Args:
        D (float): Diameter at breast height in cm. Recommendend range: 4.5cm and above.
        H (float): Tree height in m. Recommendend range: 4m and above.

    Returns:
        float: Stem volume in dm3.
    """

    # Define coefficients
    a = -0.79783
    b = 2.07157
    c = -0.73882
    d = 3.16332
    e = -1.82622

    # Calculate volume
    V = 10**a * D**b * (D + 20)**c * H**d * (H - 1.3)**e

    return V

def stem_volume_formula_119(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = -1.02039
    b = 2.00128
    c = -0.47473
    d = 2.87138
    e = -1.61803
    V = 10 ** a * (D ** b) * ((D + 20) ** c) * (H ** d) * (H - 1.3) ** e
    return V

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

    """
    Calculate the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis et al., (2005) and is recommended for Picea abies (Norway spruce), from Sweden.
    The range of valid values for D is 4.5cm and above, and for H is 4m and above.

    Args:
        D: Diameter at breast height in cm. Recommended range:  4.5cm and above
        H: Tree Height in m. Recommended range: 4m and above
    
    Returns:
        V: Stem volume in dm3
    """

    a = -1.06019
    b = 2.04239
    c = -0.54292
    d = 2.80843
    e = -1.52110

    V = (10 ** a) * (D ** b) * ((D + 20) ** c) * (H ** d) * ((H - 1.3) ** e)
    return V

def stem_volume_formula_122(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a=0.1104
    b=0.01925
    c=0.01815
    d=-0.04936
    V = a * D ** 2 + b * D ** 2 * H + c * D * H ** 2 + d * H ** 2
    return V


def stem_volume_formula_123(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    Species: Picea abies
    Location: Sweden
    
    Reference: Brandel, G. 1974. Volymfunktioner för tall och gran. Skoghögskolan, Institutionen för skogsproduktion, Rapporter och Uppsatser 33: 178-191.

    Args:
        D: Diameter at breast height in cm. Recommended range: At least 2 cm.
        H: Tree height in m. Recommended range: At least 2 m.
    
    Returns:
        V: Volume in dm3.
    """

    # # Raise ValueError if the diameter is out of range
    # if D < 2:
    #     raise ValueError("Diameter must be at least 2 cm.")
    # # Raise ValueError if the height is out of range
    # if H < 2:
    #     raise ValueError("Height must be at least 2 m.")

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

def stem_volume_formula_124(D, H):
    """
    Calculates the volume of the stem of a standing tree. 
    Volume unit in Zianis et al is not properly copied. The original source states that the volume is in dm3 instead of m3.

    Original source is Snorrason & Einarsson (2006) - http://ias.is/wp-content/uploads/Single-tree-biomass-and-stem-volume-functions-for.pdf
    see p. 18 for V, D and H units

    Species: Picea engelmannii (Engelmanni spruce).
    Country: Iceland.

    Args:
        D: Diameter at breast height in cm. Recommended range: 1.4-12.7 cm.
        H: Height of the tree in m. Recommended range: 1.7-12.7 m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a=0.4693
    b=1.311
    c=0.781
    V = a * D ** b * H ** c
    return V 

def stem_volume_formula_125(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 1.78383
    b = 1.13397
    c = -2.90893
    V = D**a * H**b * math.exp(c)
    return V

def stem_volume_formula_126(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a=0.1614
    b=3.706
    c=1.9747
    d=-2.2905
    e=-0.6665
    V = a * H ** b * D ** c * (H - 1.3) ** d * (D + 40) ** e
    return V

def stem_volume_formula_127(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a=0.187
    b=3.7077
    c=1.9854
    d=-2.2816
    e=-0.7161
    V = a * H ** b * D ** c * (H - 1.3) ** d * (D + 40) ** e
    return V

def stem_volume_formula_128(D,H):
    """
    Calculates the volume of the stem of a standing tree.
        
    This formula is implemented from Zianis and is recommended for Picea sitchensis from Norway. 
        
    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.
            
    Returns:
        V: Stem volume in dm3.
    """    
    a = 0.2101
    b = 1.892
    c = 1.1095
    d = -0.3895

    V = a * D**b * (H - 1.3)**c * (D + 40)**d
    return V

def stem_volume_formula_129(D, H):

    """
    Calculate the stem volume for a standing tree of Picea spp. (Molid) in Romania.

    Original source: Giurgiu, V. 1974. O expresie matematica unica a relatiei diametru – înaltime – volum,
    pentru majoritatea speciilor forestiere din Romania. Silvicultura si Exploatarea Padurilor
    89(4): 173–178.

    Args:
        D (float): Diameter of the tree in cm.
        H (float): Height of the tree in m.

    Returns:
        V (float): The calculated stem volume in m3.
    """

    # Define parameters
    a=0.00009464
    b=1.9341
    c=-0.0722
    d=0.6365
    e=0.172

    # Implement formula
    V = a * 10**(b * math.log10(D) + c * math.log10(D)**2 + d * math.log10(H) + e * math.log10(H)**2)
    return V

def stem_volume_formula_130(D,H):
    
    """
    Calculate the stem volume for a standing tree of Picea spp. (Molid) in Iceland.
    In original resource they used dm3 to calculate the volume.
    originaal resouce:https://www.researchgate.net/publication/228771958
    This formula is implemented from Zianis et al. (2005). 
    The recommended range for diameter is between 4.9 and 28.6.
    The recommended range for height is between 4.8 and 15.4.
    Args:
        D (float): Diameter of the tree in cm.
        H (float): Height of the tree in m.

    Returns:
        V (float): The calculated stem volume in dm3.
    """
    # Define parameters
    a=0.0739
    b=1.7508
    c=1.0228
    # Implement formula
    V= a * D**b * H**c
    return V

def stem_volume_formula_131(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Pinus contorta (Contorta tall)
    Country: Iceland

    The formula is given in "Single-tree biomass and stem volume functions for
    eleven tree species used in Icelandic forestry" by Snorrason et al. The
    paper can be found at
    http://ias.is/wp-content/uploads/Single-tree-biomass-and-stem-volume-functions-for.pdf.
    The volume formula is given in Table 1 (see Volume for Black cottonwood).
    The volume unit of m3 in Zianis et al. is not properly copied. In the paper
    after equation 1 on page 18 you can verify that the formula reports the
    volume in dm3.

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.1491
    b = 1.6466
    c = 0.8325
    V = a*D**b*H**c
    return V

def stem_volume_formula_132(D, H):
    """
    Species:    Pinus contorta
    Location:   Netherlands

    Args:
        D: Diameter at breast height in cm. Recommendend range: NA.
        H: Tree height in m. Recommendend range: NA.

    Returns:
        V: Stem volume in dm3.
    """
    
    a = 1.89303
    b = 0.98667
    c = -2.88614

    V = D**a * H**b * math.exp(c)
    return V

def stem_volume_formula_133(D, H):

    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Pinus contorta from Sweden.
    It was originally published in Eriksson, H. 1973. Volymfunktioner för stående träd av ask, asp, klibbal och contorta-tall. Institutionen för Skogsproduktion, Royal college of Forestry, Stockholm. Research Notes 6: 1– 6.
    
    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.
        
    Returns:
        V: Stem volume in dm3.
    """

    a = 0.1121
    b = 0.02870
    c = -0.000061
    d = 0.09176
    e = 0.01249

    V = a*D**2+b*D**2*H+c*D**2*H**2-d*D*H+e*D*H**2
    return V    

def stem_volume_formula_134(D: float, H: float) -> float:
    """Calculate the stem volume of a tree based on diameter and height.

    Species: Pinus contorta (contorta tall)
    Country: Sweden

    n = 1301, r2 = unknown
    
    Original source: Eriksson, H. 1973. Volymfunktioner för stående träd av ask, asp, klibbal och contorta-tall. 
    Institutionen för Skogsproduktion, Royal college of Forestry, Stockholm. Research Notes 26: 1-26
    
    Args:
        D (float): Diameter at breast height in cm.
        H (float): Tree height in m.

    Returns:
        float: Stem volume in dm3.
    """

    # Define coefficients
    a = 0.04514
    b = 1.9005
    c = 1.06964

    # Calculate volume
    V = a * D**b * H**c

    return V

def stem_volume_formula_135(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a=0.0883
    b=0.03202
    c=-0.000114
    d=-0.07892
    e=-0.01049
    
    V = a * D ** 2 + b * D ** 2 * H + c * D ** 2 * H ** 2 - d * D * H + e * D * H ** 2
    return V 

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
    """
    Calculate the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis et al., (2005) and is recommended for Pinus nigra var nigra (Black pine), from Netherlands.
    No valid range for D and H is given. 

    Args:
        D: Diameter at breast height in cm.
        H: Tree Height in m.
    
    Returns:
        V: Stem volume in dm3
    """

    a = 1.95645
    b = 0.88671
    c = -2.7675
 
    V = (D ** a) * (H ** b) * math.exp(c)
    return V

def stem_volume_formula_138(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in m3.
    """

    a=0.00010892
    b=1.9701
    c=0.0102
    d=0.0102
    e=0.133
    V = a * 10 ** (b * math.log10(D) + c * math.log10(D * D) + d * math.log10(H) + e * math.log10(H * H))
    return V

def stem_volume_formula_139(H):
    """
    Calculates the volume of the stem of a standing tree.
    
    Species: Pinus spp.
    Location: Germany
    
    Reference: Hempel, G. 1968. Allometrische studie an Pinus cembra spp. sibirica (Rupr.) Kryl. und Abies sibirica (Ledeb.). Archiv für Forstwesen 17(11):1099-1115.

    Args:
        H: Tree height in m.
    
    Returns:
        V: Volume in m3.
    """

    # Define the coefficients
    a = 0.000074
    b = 3.1

    # Calculate the volume according to the formula given by Zianis et al.
    V = a * H**b

    # Return the calculated volume
    return V

def stem_volume_formula_140(D):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.

    Returns:
        V: The calculated stem volume in m3.
    """

    a=0.0001078
    b=2.56
    v = a * D ** b
    return v

def stem_volume_formula_141(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in mm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a=0.00042613
    b=2.066225947
    c=-0.001926657
    d=0.80636901
    
    V = a * D ** (b + c) * H ** d
    return V

def stem_volume_formula_142(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in mm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a=0.00042613
    b=2.066225947
    c=-0.07956244
    d=0.80636901
    V = a * D ** (b + c) * H ** d
    return V

def stem_volume_formula_143(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in mm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.00042613
    b = 2.066225947
    c = 0.00369501
    d = 0.80636901
    V = a * D**(b+c) * H**d 
    return V

def stem_volume_formula_144(D,H):
    """
    Calculates the volume of the stem of a standing tree.
        
    This formula is implemented from Zianis and is recommended for Pinus sylvestris from Austria. The range of valid values for D is 0.5 cm and above. 
        
    Args:
        D: Diameter at breast height in dm. Recommendend range: 0.5 cm and above.
        H: Tree height in dm.
            
    Returns:
        V: Stem volume in dm3.
    """    
    a = 0.435949
    b = -0.0149083
    c = 5.21091
    d = 0.028702

    V = (math.pi / 4) * (a * D**2 * H + b * D**2 * H * math.log(D)**2 + c * D**2 + d * H)
    return V

def stem_volume_formula_145(D):

    """
    Calculate the stem volume for a standing tree of Pinus sylvestris (Scots pine) in Belgium.

    Original source: Xiao, c.W., curiel Yuste, J., Janssens, I.A., Roskams, P., Nachtergale, l.,
    carrara, A., Sanchez, B.Y. & ceulemans, R. 003. Above-and belowground biomass and net primary
    production in a 73-year-old Scots pine forest. Tree Physiology 3: 505–516.

    Args:
        D (float): Diameter of the tree in cm.

    Returns:
        V (float): The calculated stem volume in m3.
    """

    # Define parameters
    a=0.000244
    b=2.32716

    # Implement formula
    V = a * D**b
    return V

def stem_volume_formula_146(D,H):
    
    """
    Calculate the stem volume for a standing tree of Pinus sylvestris (Scots pine, Mänty, Tall, Furu, Grove den, Pin silvestri) in Belgium.
    This formula is implemented from Zianis et al. (2005). 
    Args:
        D (float): Diameter of the tree in cm.
        H (float): Height of the tree in m.

    Returns:
        V (float): The calculated stem volume in m3.
    """
    # Define parameters
    a=-0.039836
    b=0.004871
    c=-0.000061028
    d=0.000014889
    e=0.000073997
    f=0.0000091
    # Implement formula
    V= a + b*D + c*(D**2) + d*(D**3) + e*H + f*(D**2)*H
    return V

def stem_volume_formula_147(D):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.


    Returns:
        V: The calculated stem volume in ln(dm3).
    """

    a=-2.2945
    b=2.57025
    V = a + b * math.log(D)
    return V

def stem_volume_formula_148(D):
    """
    Species:    Pinus sylvestris
    Location:   Finland

    Args:
        D: Diameter at breast height in cm. Recommendend range: 0.9-50.6cm.

    Returns:
        V: Stem volume in ln(dm3).
    """
    
    a = -5.39417
    b = 3.48060
    c = 2
    d = 1.25
    e = -0.039884 

    V = a + b*math.log(c+d*D) + e*D
    return V

def stem_volume_formula_149(D, H):

    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Pinus sylvestris (Scots pine) from Finland.
    It was originally published in Laasasenaho, J. 198 . Taper curve and volume functions for pine, spruce and birch. communicationes Instituti Forestalis Fenniae 108: 1–74.
    
    Args:
        D: Diameter at breast height in cm. Recommendend range: 0.9 to 50.6 cm.
        H: Tree height in m. Recommendend range: 1.5 to 28.3 m.
        
    Returns:
        V: Stem volume in dm3.
    """

    a = 0.036089
    b = 2.01395
    c = 0.99676
    d = 2.07025
    e = -1.07209

    V = a*(D**b)*(c**D)*(H**d)*(H-1.3)**e
    return V

def stem_volume_formula_150(D: float, H: float) -> float:
    """Calculate the stem volume of a tree based on diameter and height.

    Species: Pinus sylvestris (Scots pine, Mänty, Tall, Furu, Grove den, Pin silvestri)
    Country: Finland

    n = 2326, r2 = unknown
    
    Original source: Hakkila, P. 1979. Wood density survey and dry weight tables for pine, spruce and birch stems in Finland. 
    Communicationes Instituti Forestalis Fenniae 96(3): 1-59.

    Args:
        D (float): Diameter at breast height in cm.
        H (float): Tree height in m.

    Returns:
        float: Stem volume in ln(dm3).
    """

    # Define coefficients
    a = -3.2890
    b = 1.9995
    c = 2.1395
    d = -1.1411
    e = -0.002847

    # Calculate volume
    V = a + b * math.log(D) + c * math.log(H) + d * math.log(H - 1.3) + e * D

    return V

def stem_volume_formula_151(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.0942
    b = 1.9671
    c = 0.7005
    V = a * D**b * H**c
    return V

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
    """
    Calculate the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis et al., (2005) and is recommended for Pinus sylvestris (Scots pine), from Finland.
    No valid range for D and H is given. 

    Args:
        D: Diameter at breast height in cm.
        H: Tree Height in m.
    
    Returns:
        V: Stem volume in dm3
    """

    a = 0.05782
    b = 0.11632
    c = -0.01092
    d = -0.01317

    V = a * H * D**2 + b * D * H + c * D**3 + d * D * H**2
    return V

def stem_volume_formula_154(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in ln(dm3).
    """

    a=-2.37912
    b=2.62903
    c=-0.000126
    V = a + b * math.log(D) + c * D ** 2
    return V

def stem_volume_formula_155(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    Species: Pinus sylvestris
    Location: Germany
    
    Reference: Lockow, K.-W. 1993. Modellbildung und Quantifizierung der Durchmesser- und Volumenstruktur des ausscheidenden Kieferjungbestandes - Holzmeßkundliche Entscheideungshilfen für die Erstdurchforstung. Beiträge für Forstwirtschaft und Landschaftsökologie 27(2): 77-82.

    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.
    
    Returns:
        V: Volume in m3.
    """

    # # Raise ValueError if the diameter is out of range
    # if D < 3 or D > 14:
    #     raise ValueError("Diameter must be between 3 and 14 cm.")
    # # Raise ValueError if the height is out of range
    # if H < 5.8 or H > 10.7:
    #     raise ValueError("Height must be between 5.8 and 10.7 m.")

    # Define the coefficients
    a = 5.6537 * 10**-5
    b = 1.960466
    c = 0.894433

    # Calculate the volume according to the formula given by Zianis et al.
    V = a * D**b * H**c

    # Return the calculated volume
    return V

def stem_volume_formula_156(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in dm.
        H: Height of the tree in dm.

    Returns:
        V: The calculated stem volume in dm3.
    """
    a = 1.480589
    b = 1.982459514
    c = 0.742674501
    V = a * D ** b * H**c
    return V

def stem_volume_formula_157(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in mm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.00207765
    b = 1.952764402
    c = -8.6651 * 10 ** (-5)
    d = 0.48560878
    V = a * D ** (b + c) * H ** d
    return V

def stem_volume_formula_158(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in mm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.00207765
    b = 1.952764402
    c = -0.11110535
    d = 0.48560878
    V = a * D ** (b + c) * H ** d
    return V

def stem_volume_formula_159(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in mm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a=0.00207765
    b=1.952764402
    c=0.001095496
    d=0.48560878
    V = a * D ** (b + c) * H ** d
    return V

def stem_volume_formula_160(D,H):
    """
    Calculates the volume of the stem of a standing tree.
        
    This formula is implemented from Zianis and is recommended for Pinus sylvestris from Netherlands. 
        
    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.
            
    Returns:
        V: Stem volume in dm3.
    """    
    a = 1.82075
    b = 1.07427
    c = -2.8885
 
    V = D ** a * H ** b * math.exp(c)
    return V

def stem_volume_formula_161(D, H):

    """
    Calculate the stem volume for a standing tree of Pinus sylvestris
    (Scots pine, Mänty, Tall, Furu, Grove den, Pin silvestri) in Norway.

    Original source: Bauger, E. 1995. Funksjoner og tabeller for kubering av stående trær.
    Rapport fra Skogforsk(16): 1–26.

    Args:
        D (float): Diameter of the tree in cm.
        H (float): Height of the tree in m.

    Returns:
        V (float): The calculated stem volume in dm3.
    """

    # Define parameters
    a=0.1424
    b=2.0786
    c=1.9028
    d=-1.0259
    e=-0.2640

    # Implement formula
    V = a * H**b * D**c * (H-1.3)**d * (D+100)**e
    return V

def stem_volume_formula_162(D,H):
    
    """
    Calculate the stem volume for a standing tree of Pinus sylvestris
    (Scots pine, Mänty, Tall, Furu, Grove den, Pin silvestri) in Norway. This formula is implemented from Zianis et al. (2005).



    Args:
        D (float): Diameter of the tree in cm.
        H (float): Height of the tree in m.

    Returns:
        V (float): The calculated stem volume in dm3.
    """
    a=0.1263
    b=2.4621
    c=1.9008
    d=-1.3716
    e=-0.2663
    # Define parameters
    V=a * H**b * D**c * (H - 1.3)**d * (D + 100)**e
    return V

def stem_volume_formula_163(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.4434
    b = 4.9667
    c = 1.9912
    d = -3.6612
    e = -0.7502
    V = a * H**b * D**c * (H-1.3)**d * (D+100)**e
    return V

def stem_volume_formula_164(D, H):
    """
    Species:    Pinus sylvestris
    Location:   Norway

    Args:
        D: Diameter at breast height in cm. Recommendend range: 10cm or above.
        H: Tree height in m. Recommendend range: NA.

    Returns:
        V: Stem volume in dm3.
    """
    
    a = 8.6524
    b = 0.076844    
    c = 0.031573

    V = a + b*D**2 + c*D**2 *H
    return V

def stem_volume_formula_165(D, H):

    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Pinus sylvestris (Scots pine) from Norway.
    It was originally published in Brantseg, A. 1967. Furu sønnafjells: kubering av stående skog, funksjoner og tabeller. Meddelelser fra det Norske Skogforsøksvesen 84: 689–739.
    
    Args:
        D: Diameter at breast height in cm. Recommendend range: up to 12 cm.
        H: Tree height in m.
        
    Returns:
        V: Stem volume in dm3.
    """

    a = 0.6716
    b = 0.075708
    c = 0.029679
    d = 0.004341 # NOTE: parameter d listed in Zianis et al. for formula #166 belongs to formula #165 according to the original publication

    V = a+b*D**2+c*D**2*H+d*D*H**2
    return V    

def stem_volume_formula_166(D: float, H: float) -> float:
    """Calculate the stem volume of a tree based on diameter and height.

    Species: Pinus sylvestris (Scots pine, Mänty, Tall, Furu, Grove den, Pin silvestri)  
    Country: Norway

    n = 2622, r2 = 0.999
    
    Original source: Brantseg, A. 1967. Furu sønnafjells: kubering av stående skog, funksjoner og tabeller. 
    Meddelelser fra det Norske Skogforsøksvesen 84: 689-739.

    Args:
        D (float): Diameter at breast height in cm. Recommendend range: 0-12.
        H (float): Tree height in m.

    Returns:
        float: Stem volume in dm3.
    """

    # Define coefficients
    a = 2.0044
    b = 0.029886
    c = 0.036972

    # Calculate volume
    V = a + b * D**2 + c * D**2 * H

    return V

def stem_volume_formula_167(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 2.9121
    b = 0.039994
    c = -0.001091
    V = a + b * D**2 + c * D**2 * H
    return V

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
    # reference: Giurgiu, V. 1974. O expresie matematica unica a relatiei diametru - înaltime - volum, pentru majoritatea speciilor forestiere din Romania. Silvicultura si Exploatarea Padurilor 89(4): 173-178
    # Pinus sylvestris (Scots pine, Mänty, Tall, Furu, Grove den, Pin silvestri), Romania
    # input: diameter D in cm, height H in m
    # output: volume in m3
    """
    Calculate the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis et al., (2005) and is recommended for Pinus sylvestris (Scots pine), from Romania.
    No valid range for D and H is given. 

    Args:
        D: Diameter at breast height in cm.
        H: Tree Height in m.
    
    Returns:
        V: Stem volume in m3
    """    
    a = 0.00014808
    b = 1.8341
    c = -0.0448
    d = 0.3115
    e = 0.3525

    V = a * 10**(b * math.log10(D) + c * math.log10(D)**2 + d * math.log10(H) + e * math.log10(H)**2)
    return V

def stem_volume_formula_170(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.1028
    b = 0.02705
    c = 0.005215
    V = a * D**2 + b * D**2 * H + c * D * H**2
    return V

def stem_volume_formula_171(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    Species: Pinus sylvestris
    Location: Sweden 
    
    Reference: Brandel, G. 1974. Volymfunktioner för tall och gran.Skoghögskolan, Institutionen för skogsproduktion, Rapporter och Uppsatser 33: 178-191.

    Args:
        D: Diameter at breast height in cm. Recommended range: At least 2 cm.
        H: Tree height in m. At least 2 m.
    
    Returns:
        V: Volume in dm3.
    """

    # # Raise ValueError if the diameter is out of range
    # if D < 2:
    #     raise ValueError("Diameter must be at least 2 cm.")
    # # Raise ValueError if the height is out of range
    # if H < 2:
    #     raise ValueError("Height must be at least 2 m.")

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

def stem_volume_formula_172(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = -1.20914
    b = 1.9474
    c = -0.05947
    d = 1.40958
    e = -0.4581
    V = 10 ** a * D**b * (D+20)**c * H**d * (H-1.3)**e
    return V

def stem_volume_formula_173(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = -1.38903
    b = 1.84493
    c = 0.06563
    d = 2.02122
    e = -1.01095
    V = 10 ** a * (D ** b) * ((D + 20) ** c) * (H ** d) * (H - 1.3) ** e
    return V

def stem_volume_formula_174(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = -1.25246
    b = 1.98244
    c = -0.13118
    d = 1.03781
    e = -0.03482
    V = 10 ** a * D ** b * (D + 20) ** c * H ** d * (H - 1.3) ** e
    return V

def stem_volume_formula_175(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = -1.52761
    b = 1.82928
    c = 0.07454
    d = 1.43792
    e = -0.35559
    V = 10 ** a * D ** b * (D + 20) ** c * H ** d * (H - 1.3) ** e 
    return V

def stem_volume_formula_176(D,H):
    """
    Calculates the volume of the stem of a standing tree.
        
    This formula is implemented from Zianis and is recommended for Pinus sylvestris from Sweden. The range of valid values for D is 5-49.9 cm. 
    Original source is Näslund (1947) - https://pub.epsilon.slu.se/10185/1/medd_statens_skogsforskningsanst_032_04.pdf

    Args:
        D: Diameter at breast height in cm. Recommendend range: 5-49.9 cm.
        H: Tree height in m. Recommendend range: 3-32.9 cm.
            
    Returns:
        V: Stem volume in dm3.
    """    
    a = 0.1072
    b = 0.02427
    c = 0.007315

    V = a * D**2 + b * D**2 * H + c * D * H**2
    return V

def stem_volume_formula_177(D, H):

    """
    Calculate the stem volume for a standing tree of Pinus sylvestris (Scots pine, Mänty, Tall, Furu, Grove den, Pin silvestri) in Sweden.

    Original source: Brandel, G. 1974. Volymfunktioner för tall och gran. Skoghögskolan,
    Institutionen för skogsproduktion, Rapporter och Uppsatser 33: 178–191.

    Args:
        D (float): Diameter of the tree in cm. Recommended range: 2 cm and above.
        H (float): Height of the tree in m. Recommended range: 2 m and above.

    Returns:
        V (float): The calculated stem volume in dm3.
    """

    # Define parameters
    a=-1.2605
    b=1.9322
    c=-0.0897
    d=2.1795
    e=-1.1676

    # Implement formula
    V = 10**a * D**b * (D + 20)**c * H**d * (H + 1.3)**e
    return V

def stem_volume_formula_178(D,H):
    """
    This formula is implemented from Zianis et al. (2005).
    Calculate the stem volume of a tree based on diameter and height.
    The recommended range for diameter is between 5 and 10.4 dm.
    Species: Abies grandis (Grand fir)  
    Country: Netherlands

    Args:
        D (float): Diameter at breast height in dm.
        H (float): Tree height in dm.

    Returns:
        float: Stem volume in dm3.
    """
     # Define parameters

    a=0.366419
    b=1.13323
    c=0.1306
    # Implement formula
    V= (math.pi / 4) * (a * D**2 * H + b * D**2 + c * D) 
    return V

def stem_volume_formula_179(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in mm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.0009507
    b = 1.895629295
    c = 0.001650837
    d = 0.8392146
    V = a * D * (b + c) * (H ** d)
    return V

def stem_volume_formula_180(D, H):
    """
    Species:    Populus spp.
    Location:   Netherlands

    Args:
        D: Diameter at breast height in cm. Recommendend range: NA.
        H: Tree height in m. Recommendend range: NA.

    Returns:
        V: Stem volume in dm3.
    """
    
    a = 0.0009507
    b = 1.895629295
    c = -0.00773694
    d = 0.8392146

    V = a*D**(b+c) * H**d
    return V

def stem_volume_formula_181(D, H):

    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Populus spp. (Poplar) from the Netherlands.
    It was originally published in Schelhaas, M.J., Nabuurs, G.J., Jans, W.W.P., Moors, E.J., Sabaté, S. & Daamen, W.P. 00 . Converging estimates of the forest carbon sink. Alterra-rapport 631: 1–44. 
    
    Args:
        D: Diameter at breast height in mm.
        H: Tree height in m.
        
    Returns:
        V: Stem volume in dm3.
    """

    a = 0.0009507
    b = 1.895629295
    c = -0.00773694
    d = 0.8392146

    V = a*D**(b+c)*H**d
    return V

def stem_volume_formula_182(D: float, H: float) -> float:
    """Calculate the stem volume of a tree based on diameter and height.

    Species: Populus spp. (Poplar, Plop)  
    Country: Romania

    n = unknown, r2 = unknown
    
    Original source: Giurgiu, V. 1974. O expresie matematica unica a relatiei diametru - înaltime - volum, pentru 
    majoritatea speciilor forestiere din Romania. Silvicultura si Exploatarea Padurilor 89(4): 173-178.

    Args:
        D (float): Diameter at breast height in cm.
        H (float): Tree height in m.

    Returns:
        float: Stem volume in m3.
    """

    # Define coefficients
    a = 0.00018059
    b = 1.9342
    c = 0.0013
    d = -0.0161
    e = 0.4099

    # Calculate volume
    V = a * 10**(b * math.log10(D) + c * math.log10(D)**2 + d * math.log10(H) + e * math.log10(H)**2)

    return V

def stem_volume_formula_183(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.00041486
    b = 1.4466
    c = 0.1089
    d = -0.1963
    e = 0.5681
    V = a * 10 * (b * math.log10(D) + c * (math.log10(D) ** 2) + d * math.log10(H) + e * (math.log10(H) ** 2))
    return V

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
    """
    Calculate the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis et al., (2005) and is recommended for Populus tremula (Aspen), from Norway.
    The range of valid values for D is 13cm and above.

    Args:
        D: Diameter at breast height in cm. Recommended range:  13cm and above
        H: Tree Height in m.
    
    Returns:
        V: Stem volume in dm3
    """ 
    a = 9.69
    b = 0.0365

    V = a + b * (D**2) * H
    return V

def stem_volume_formula_186(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = -0.21
    b = 0.0398
    V = a + b*D**2 * H
    return V


def stem_volume_formula_187(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    Species: Populus tremulus
    Location: Romania
    
    Giurgiu, V. 1974. O expresie matematica unica a relatiei diametru - înaltime - volum, pentru majoritatea speciilor forestiere din Romania. Silviculturasi Exploatarea Padurilor 89(4): 173-178.

    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.
    
    Returns:
        V: Volume in m3.
    """

    # # Import the log10 function from the math package
    # from math import log10

    # Define the coefficients
    a = 0.00007604
    b = 1.7812
    c = 0.0528
    d = 0.8533
    e = 0.0654

    # Calculate the volume according to the formula given by Zianis et al.
    V = a * 10**(b * math.log10(D) + c * math.log10(D)**2 + d * math.log10(H) + e * math.log10(H)**2)

    # Return the calculated volume
    return V

def stem_volume_formula_188(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.01548
    b = 0.03255
    c = -4.7e-05
    d = -0.01333
    e = 0.004859
    V = a * D**2 + b * D**2 * H + c * D**2 * H ** 2 + d * D * H + e * D * H ** 2
    return V

def stem_volume_formula_189(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.03597
    b = 1.84297
    c = 1.15988
    V = a * D ** b * H ** c
    return V

def stem_volume_formula_190(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.03392
    b = -0.01491
    c = -5e-06
    d = 0.01704
    e = 0.002926
    V = a * D ** 2 * H + b * D ** 2 * H + c * D ** 2 * H ** 2 + d * D * H + e * D * H ** 2
    return V

def stem_volume_formula_191(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Populus trichocarpa (Black cottonwood)
    Country: Iceland

    The formula is given in "Single-tree biomass and stem volume functions for
    eleven tree species used in Icelandic forestry" by Snorrason et al. The
    paper can be found at
    http://ias.is/wp-content/uploads/Single-tree-biomass-and-stem-volume-functions-for.pdf.
    The volume formula is given in Table 1 (see Volume for Black cottonwood).
    The volume unit of m3 in Zianis et al. is not properly copied. In the paper
    after equation 1 on page 18 you can verify that the formula reports the
    volume in dm3.

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.0732
    b = 1.6933
    c = 1.0562
    V = a * D**b * H**c  
    return V

def stem_volume_formula_192(D,H):
    """
    Calculates the volume of the stem of a standing tree.
        
    This formula is implemented from Zianis and is recommended for Prunus avium from Belgium.
    Original source is Dagnelie et al (1999) - https://orbi.uliege.be/bitstream/2268/100984/1/tables%20de%20cubage%201999.pdf

    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.
            
    Returns:
        V: Stem volume in m3.
    """    
    a = -0.002311
    b = -0.00117728
    c = 0.000149061
    d = -7.8058e-6
    e = 3.3282e-4
    f = 3.1526e-5

    V = a + b * D + c * D**2 + d * D**3 + e * H + f * D**2 * H 
    return V

def stem_volume_formula_193(D, H):

    """
    Calculate the stem volume for a standing tree of Pseudotsuga menziesii (Douglas fir, Duglas) in Belgium.

    Original source: Dagnelie, P., Palm, R., Rondeux, J. & Thill, A. 1999. Tables de cubage des
    arbres et des peuplements forestiers. les Presses Agronomiques de Gembloux, Gembloux. 1 6 p.

    Args:
        D (float): Diameter of the tree in cm.
        H (float): Height of the tree in m.

    Returns:
        V (float): The calculated stem volume in m3.
    """

    # Define the parameters
    a=-0.019911
    b=0.001871101
    c=0.000127328
    d=-5.7631*10**(-6)
    e=0.00071591
    f=3.9371*10**(-5)

    # Implement formula
    V = a + b * D + c * D**2 + d * D**3 + e * H + f * D**2 * H
    return V

def stem_volume_formula_194(D,H):

    """
    Calculate the stem volume for a standing tree.

    This formula is implemented from Zianis et al. (2005) and is recommended for #Pseudotsuga menziesii (Douglas fir, Duglasfrom Neatherlands. 
   

    Args:
        D (float): Diameter of the tree in cm.
        H (float): Height of the tree in m.

    Returns:
        V (float): The calculated stem volume in dm3.
    """
    # Define the parameters
    a=1.90053
    b=0.80726
    c=-2.43151
     # Implement formula
    V= (D**a) * (H**b) * math.exp(c) 
    return V

def stem_volume_formula_195(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a=1.8211
    b=4.153
    c=2.1342
    d=-2.6902
    e=-1.4265
    V = a * H ** b * D ** c * (H - 1.3) ** d * (D + 40) ** e
    return V

def stem_volume_formula_196(D, H):
    """
    Species:    Pseudotsuga menziesii
    Location:   Romania

    Args:
        D: Diameter at breast height in cm. Recommendend range: NA.
        H: Tree height in m. Recommendend range: NA.

    Returns:
        V: Stem volume in m3.
    """
    
    a = 0.0000477
    b = 1.8688
    c = 0.0424
    d = 1.1411
    e = -0.1047

    V = a*10**(b*math.log10(D) + c*math.log10(D)**2 + d*math.log10(H) + e*math.log10(H)**2)    
    return V

def stem_volume_formula_197(D, H):

    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Pseudotsuga spp. from the Netherlands.
    It was originally published in Schelhaas, M.J., Nabuurs, G.J., Jans, W.W.P., Moors, E.J., Sabaté, S. & Daamen, W.P. 00 . Converging estimates of the forest carbon sink. Alterra-rapport 631: 1–44. 
    
    Args:
        D: Diameter at breast height in mm.
        H: Tree height in m.
        
    Returns:
        V: Stem volume in dm3.
    """

    a = 0.00095916
    b = 2.092560524
    c = 0.000297255
    d = 0.48824344

    V = a*D**(b+c)*H**d
    return V

def stem_volume_formula_198(D: float, H: float) -> float:
    """Calculate the stem volume of a tree based on diameter and height.

    Species: Pseudotsuga spp.  
    Country: Netherlands

    n = unknown, r2 = unknown
    
    Original source: Schelhaas, M.J., Nabuurs, G.J., Jans, W.W.P., Moors, E.J., Sabaté, S. & Daamen, W.P. 2002. 
    Converging estimates of the forest carbon sink. Alterra-rapport 631: 1-44.

    Args:
        D (float): Diameter at breast height in mm.
        H (float): Tree height in m.

    Returns:
        float: Stem volume in dm3.
    """

    # Define coefficients
    a = 0.00095916
    b = 2.092560524
    c = -0.0449007
    d = 0.48824344

    # Calculate volume
    V = a * D**(b + c) * H**d

    return V

def stem_volume_formula_199(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in mm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.00095916
    b = 2.092560524
    c = 0
    d = 0.48824344

    V = a * D ** (b + c) * H ** d
    return V


def stem_volume_formula_200(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Quercus grisea (Gray oak, Stejar brumariu) from Romania. 
    
    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.
        
    Returns:
        V: Stem volume in m3.
    """
       #coefficients
    a=0.00007188
    b=1.4486
    c=0.0204
    d=1.4084
    e=0.0409

    V = a*10**(b*math.log10(D)+c*math.log10(D)**2+d*math.log10(H)+e*math.log10(H)**2)
    return V

def stem_volume_formula_201(D, H):
    """
    Calculate the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis et al., (2005) and is recommended for Quercus ilex (Holm oak), from Italy.
     The range of valid values for D is 4.5-26.1cm, and for H is 6-16m.

    Args:
        D: Diameter at breast height in cm. Recommended range: 4.5-26.1cm
        H: Tree Height in m. Recommended range: 6-16m
    
    Returns:
        V: Stem volume in dm3
    """ 
    a = 1.1909
    b = 0.038639

    V = a + b * (D**2) * H
    return V

def stem_volume_formula_202(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in m3.
    """

    a = 9.6e-05
    b = 1.821
    c = 0.759
    V = a * D ** b * H ** c
    return V

def stem_volume_formula_203(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    Species: Quercus laevis
    Location: Romania
    
    Giurgiu, V. 1974. O expresie matematica unica a relatiei diametru - înaltime - volum, pentru majoritatea speciilor forestiere din Romania. Silviculturasi Exploatarea Padurilor 89(4): 173-178.

    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.
    
    Returns:
        V: Volume in m3.
    """

    # # Import the log10 function from the math package
    # from math import log10


    # Define the coefficients
    a = 0.0001992
    b = 2.014
    c = -0.0602	
    d = -0.1108
    e = 0.4811

    # Calculate the volume according to the formula given by Zianis et al.
    V = a * 10**(b * math.log10(D) + c * math.log10(D)**2 + d * math.log10(H) + e * math.log10(H)**2)

    # Return the calculated volume
    return V

def stem_volume_formula_204(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in ln(m3).
    """

    a=-9.646
    b=2.076
    c=0.761
    V = a + b * math.log(D) + c * H
    return V

def stem_volume_formula_205(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in ln(m3).
    """

    a = -11.473
    b = 2.548
    c = 0.967
    V = a + b * math.log(D) + c * H
    return V

def stem_volume_formula_206(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in m3.
    """

    a = 0.00035164
    b = 1.1119
    c = 0.3108
    d = 0.5356
    e = 0.2139
    V = a * 10 ** (b * math.log10(D) + c * math.log10(D) ** 2 + d * math.log10(H) + e * math.log10(H) ** 2)
    return V

def stem_volume_formula_207(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a=2.00333
    b=0.85925
    c=-2.86353
    V = D ** a * H ** b * math.exp(c)
    return V

def stem_volume_formula_208(D,H):
    """
    Calculates the volume of the stem of a standing tree.
        
    This formula is implemented from Zianis and is recommended for Quercus rubra from Belgium.
    Original source is Dagnelie et al (1999) - https://orbi.uliege.be/bitstream/2268/100984/1/tables%20de%20cubage%201999.pdf

    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.
            
    Returns:
        V: Stem volume in m3.
    """    
    a = -0.02149
    b = 0.002986681
    c = -4.2506e-5
    d = -2.1806e-6
    e = -0.000743
    f = 3.7473e-5

    V = a + b * D + c * D**2 + d * D**3 + e * H + f * D**2 * H
    return V

def stem_volume_formula_209(D, H):

    """
    Calculate the stem volume for a standing tree of Quercus rubra (Red oak, chêne rouge) in the Netherlands.

    Original source: Dik, E.J. 1984. Estimating the wood volume of standing trees in forestry practice.
    Rijksinstituut voor onderzoek in de bos en landschapsbouw de Dorschkamp, Wageningen.
    Uitvoerige verslagen 19(1): 1–114.

    Args:
        D (float): Diameter of the tree in cm.
        H (float): Height of the tree in m.

    Returns:
        V (float): The calculated stem volume in dm3.
    """

    # Define parameters
    a=1.83932
    b=0.9724
    c=-2.71877
    
    # Implement formula
    V = D**a * H**b * math.exp(c)
    return V
    
def stem_volume_formula_210(D,H):
    

    """
    Calculates the volume of the stem of a standing tree.

    This formula is implemented from Zianis and is recommended for Quercus spp. 
    (Oak, Chênes, Stejar) from Austria. The diameter should be biger than 1.

    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.

    Returns:
        v: Stem volume in m3.
    """

    a=0.115631
    b=65.9961
    c=1.20321
    d=-0.930406
    e=-215.758
    f=168.477
    V= (math.pi / 4) * (
    a * D**2 * H +
    b * D**2 +
    c * D * H +
    d * H +
    e * D +
    f
) 

    return V

def stem_volume_formula_211(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in dm.
        H: Height of the tree in dm.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.417118
    b = 0.21941
    c = 13.32594
    V = (math.pi / 4) * (a * D**2 * H + b * D**2 * H * (math.log(D)**2) + c * D**2)
    return V

def stem_volume_formula_212(D, H):
    """
    Species:    Quercus spp.
    Location:   Belgium

    Args:
        D: Diameter at breast height in cm. Recommendend range: NA.
        H: Tree height in m. Recommendend range: NA.

    Returns:
        V: Stem volume in m3.
    """
    
    a = -0.0022735
    b = 0.000389557
    c = 0.000124772
    d = -0.0000018434
    e = -0.0016657
    f = 0.000036985

    V = a + b*D + c*D**2 + d*D**3 + e*H + f*D**2 * H
    return V 	      

def stem_volume_formula_213(D, H):

    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Quercus spp. (Oak) from the Netherlands.
    It was originally published in Schelhaas, M.J., Nabuurs, G.J., Jans, W.W.P., Moors, E.J., Sabaté, S. & Daamen, W.P. 00 . Converging estimates of the forest carbon sink. Alterra-rapport 631: 1–44. 
    
    Args:
        D: Diameter at breast height in mm.
        H: Tree height in m.
        
    Returns:
        V: Stem volume in dm3.
    """

    a = 0.00095853
    b = 2.040672356
    c = 0.001965013
    d = 0.56366437

    V = a*D**(b+c)*H**d
    return V

def stem_volume_formula_214(D: float, H: float) -> float:
    """Calculate the stem volume of a tree based on diameter and height.

    Species: Quercus spp. (Oak, chênes, Stejar)
    Country: Netherlands

    n = unknown, r2 = unknown
    
    Resource: Schelhaas, M.J., Nabuurs, G.J., Jans, W.W.P., Moors, E.J., Sabaté, S. & Daamen, W.P. 2002. 
    Converging estimates of the forest carbon sink. Alterra-rapport 631: 1-44.

    Args:
        D (float): Diameter at breast height in mm.
        H (float): Tree height in m.

    Returns:
        float: Stem volume in dm3.
    """

    # Define coefficients
    a = 0.00095853
    b = 2.040672356
    c = -0.02101921
    d = 0.56366437

    # Calculate volume
    V = a * D**(b + c) * H**d

    return V

def stem_volume_formula_215(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in mm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.00095853
    b = 2.040672356
    c = -0.04354461
    d = 0.56366437
    V = a * D * (b + c) * (H ** d)
    return V

def stem_volume_formula_216(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for  Quercus spp. (Oak, chênes, Stejar) from Romania. 
    
    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.
        
    Returns:
        V: Stem volume in m3.
    """
       #coefficients
    a=0.00008839
    b=1.8905
    c=0.0469
    d=0.8059
    e=-0.0045

    V = a*10**(b*math.log10(D)+c*math.log10(D)**2+d*math.log10(H)+e*math.log10(H)**2)
    return V

def stem_volume_formula_217(D, H):
    # reference: Broadmeadow, M. & Matthews, R. 2004. Survey methods for Kyoto Protocol monitoring and verification of UK forest carbon stocks. UK Emissions by Sources and Removals by Sinks due to Land Use, Land Use Change and Forestry Activities, Report (June 2004). CEH, Edinburgh.
    # Quercus spp. (Oak, Chênes, Stejar), UK
    # input: diameter D in cm, height H in m
    # output: volume in m3
    """
    Calculate the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis et al., (2005) and is recommended for Quercus spp. (Oak), UK
    No valid range for D and H is given. 

    Args:
        D: Diameter at breast height in cm.
        H: Tree Height in m.
    
    Returns:
        V: Stem volume in dm3
    """  
    # coefficients
    a = -0.011724
    b = 0.0000765
    c = 0.75

    # equation 
    V =  a + b * (D**2) * (H**c)

    return V

def stem_volume_formula_218(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = -1.86827
    b = 0.21461
    c = 0.01283
    d = 0.0138
    e = -0.06311
    V = a + b * D ** 2 + c * D ** 2 * H + d * D * H ** 2 + e * H ** 2
    return V

def stem_volume_formula_219(D, H):
    """
    Calculates the volume of the stem of a standing tree.
    
    Species: Salix caprea
    Location: Romania
    
    Giurgiu, V. 1974. O expresie matematica unica a relatiei diametru - înaltime - volum, pentru majoritatea speciilor forestiere din Romania. Silviculturasi Exploatarea Padurilor 89(4): 173-178.

    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.
    
    Returns:
        V: Volume in m3.
    """

    # # Import the log10 function from the math package
    # from math import log10

    # Define the coefficients
    a = 0.00011585
    b = 1.6688
    c = 0.1090
    d = 0.7781
    e = 0.0269

    # Calculate the volume according to the formula given by Zianis et al.
    V = a * 10**(b * math.log10(D) + c * math.log10(D)**2 + d * math.log10(H) + e * math.log10(H)**2)

    # Return the calculated volume
    return V

def stem_volume_formula_220(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in m3.
    """

    a = 4.281e-05
    b = 2.0766
    c = -0.1296
    d = 0.6843
    e = 0.2745
    V = a * 10 ** (b * math.log10(D) + c * math.log10(D) ** 2 + d * math.log10(H) + e * math.log10(H) ** 2)
    return V

def stem_volume_formula_221(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in m3.
    """

    a = 7.325e-05
    b = 1.5598
    c = 0.0302
    d = 0.8572
    e = 0.1791
    V = a * 10 * (b * math.log10(D) + c * (math.log10(D) ** 2) + d * math.log10(H) + e * (math.log10(H) ** 2)) 
    return V

def stem_volume_formula_222(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = -1.86827
    b = 0.21461
    c = 0.01283
    d = 0.0138
    e = -0.06311
    V = (a + b * D ** 2 + c * D ** 2 * H + d * H ** 2 + D + e * H ** 2)
    return V

def stem_volume_formula_223(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 1.67887
    b = 1.11243
    c = -2.64821
    V = D ** a * H ** b * math.exp(c)
    return V

def stem_volume_formula_224(D,H):
    """
    Calculates the volume of the stem of a standing tree.
        
    This formula is implemented from Zianis and is recommended for Thuja pilicata from Norway. The range of valid values for D is 5 cm and above. 
        
    Args:
        D: Diameter at breast height in cm. Recommendend range: 5 cm and above.
        H: Tree height in m.
            
    Returns:
        V: Stem volume in dm3.
    """    
    a = 1.3057
    b = 3.9075
    c = 1.9832
    d = -2.3337
    e = -1.3024

    V = a * H**b * D**c * (H - 1.3)**d * (D + 40)**e
    return V

def stem_volume_formula_225(D, H):

    """
    Calculate the stem volume for a standing tree of Tilia cordata (Tei) in Romania.

    Original source: Giurgiu, V. 1974. O expresie matematica unica a relatiei diametru – înaltime – volum, 
    pentru majoritatea speciilor forestiere din Romania. Silviculturasi Exploatarea Padurilor 89(4): 173–178.

    Args:
        D (float): Diameter of the tree in cm.
        H (float): Height of the tree in m.

    Returns:
        V (float): The calculated stem volume in m3.
    """

    # Define parameters
    a=0.00004124
    b=1.9302
    c=0.0209
    d=0.129
    e=-0.1903

    # Implement formula
    V = a * 10**(b * math.log10(D) + c * math.log10(D)**2 + d * math.log10(H) + e * math.log10(H)**2)
    return V

def stem_volume_formula_226(D,H):
    
    """
    Calculate the stem volume for a standing tree of Tsuga heterophylla (Hemlock) in the Netherlands.
    This formula is implemented from Zianis et el(2005).

    Args:
        D (float): Diameter of the tree in cm.
        H (float): Height of the tree in m.

    Returns:
        V (float): The calculated stem volume in dm3.
    """
    # Define parameters
    a=1.76755
    b=1.37219
    c=-3.54922
    # Implement formula
    V= (D**a) * (H**b) * math.exp(c)#QTsuga heterophylla (Hemlock)(Neatherlands)
    return V

def stem_volume_formula_227(D, H):
    """
    Calculates the volume of the stem of a standing tree.

    Species: Unknown  
    Country: Unknown

    Args:
        D: Diameter at breast height in cm.
        H: Height of the tree in m.

    Returns:
        V: The calculated stem volume in dm3.
    """

    a = 0.4291
    b = 2.6153
    c = 1.9145
    d = -1.2696
    e = -0.6715
    V =  a * (H ** b) * (D ** c) * (H - 1.3) ** d * (D + 100) ** e
    return V

def stem_volume_formula_228(D, H):
    """
    Species:    Ulmus spp.
    Location:   Belgium
    
    Args:
        D: Diameter at breast height in cm. Recommendend range: NA.
        H: Tree height in m. Recommendend range: NA.
        
    Returns:
        V: Stem volume in m3."""
    
    a = -0.034716
    b = 0.004268168
    c = -0.00013227
    d = -0.0000017667
    e = 0.00016516
    f = 0.000038311

    V = a + b*D + c*D**2 + d*D**3 + e*H + f*D**2 * H
    return V

def stem_volume_formula_229(D, H):

    """
    Calculates the volume of the stem of a standing tree.
    
    This formula is implemented from Zianis and is recommended for Ulmus spp. (Elm) from the Netherlands.
    It was originally published in Dik, E.J. 1984. Estimating the wood volume of standing trees in forestry practice. Rijksinstituut voor onderzoek in de bos en landschapsbouw de Dorschkamp, Wageningen. Uitvoerige verslagen 19(1): 1–114. 
    
    Args:
        D: Diameter at breast height in cm.
        H: Tree height in m.
        
    Returns:
        V: Stem volume in dm3.
    """

    a = 1.94295
    b = 1.29229
    c = -4.20064

    import math

    V = D**a*H**b*math.exp(c)
    return V

def stem_volume_formula_230(D: float, H: float) -> float:
    """Calculate the stem volume of a tree based on diameter and height.

    Species: Ulmus spp. (Elm, Orme, Ulm)
    Country: Romania

    n = unknown, r2 = unknown
    
    Original source: Giurgiu, V. 1974. O expresie matematica unica a relatiei diametru - înaltime - volum, pentru 
    majoritatea speciilor forestiere din Romania. Silvicultura si Exploatarea Padurilor 89(4): 173-178.

    Args:
        D (float): Diameter at breast height in cm.
        H (float): Tree height in m.

    Returns:
        float: Stem volume in m3.
    """

    # Define coefficients
    a = 3.992 * 10**-5
    b = 2.1569
    c = -0.0933
    d = 1.0728
    e = -0.0708

    # Calculate volume
    V = a * 10**(b * math.log10(D) + c * math.log10(D)**2 + d * math.log10(H)+ e * math.log10(H)**2)

    return V
