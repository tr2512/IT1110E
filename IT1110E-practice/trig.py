pi = 3.14159265358979
def exponential(x):
    a = 1
    i = 1
    c = 1
    while True:
        c *= x/i
        a += c
        if c < 10e-9:
            break
        i += 1
    return round(a,6)
def sine(x):
    x -= x // (2*pi) * 2*pi
    a = x
    i = 1
    c = x
    while True:
        c *= x*x * (-1) / ((2*i+1)*(2*i))
        a += c
        if abs(x*c / (2*i+2)) < 10**-9:
            break
        i += 1
    return round(a,6)
def cosine(x):
    x -= x // (2*pi) * 2*pi
    a = 1
    i = 1
    c = 1
    while True:
        c *= x*x * (-1) / ((2*i)*(2*i-1))
        #c *= x * x * (-1) / ((2*i)*(2*i-1))
        a += c
        if abs((c*x)/(2*i+1)) <10**-9:
            break
        i += 1
    return round(a,6)
