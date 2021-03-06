import math

def precision_and_scale(x):
    max_digits = 14
    int_part = int(abs(x))
    magnitude = 1 if int_part == 0 else int(math.log10(int_part)) + 1
    if magnitude >= max_digits:
        return (magnitude, 0)
    frac_part = abs(x) - int_part
    multiplier = 10 ** (max_digits - magnitude)
    frac_digits = multiplier + int(multiplier * frac_part + 0.5)
    while frac_digits % 10 == 0:
        frac_digits /= 10
    scale = int(math.log10(frac_digits))
    return (magnitude + scale, scale)

floatNb = 0.2    
print(floatNb, " ", precision_and_scale(floatNb))
floatNb = 0.2    
print(floatNb, " ", precision_and_scale(floatNb))
floatNb = 12.255   
print(floatNb, " ", precision_and_scale(floatNb))
floatNb = 2  
print(floatNb, " ", precision_and_scale(floatNb))
floatNb = 35  
print(floatNb, " ", precision_and_scale(floatNb))
floatNb = 35.0  
print(floatNb, " ", precision_and_scale(floatNb))
floatNb = 35.01  
print(floatNb, " ", precision_and_scale(floatNb))
floatNb = 35.01  
print(floatNb, " * 100 ", precision_and_scale(floatNb * 100))
