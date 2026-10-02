import math as m

def sin(a):

    return m.sin(a)

def cos(a):

    return m.cos(a)

def tan(a):

    return m.tan(a)

def arcsin(a):

    if -1 <= a <= 1:

        return m.asin(a)

    else:

        return "Error"

def arccos(a):

    if -1 <= a <= 1:

        return m.acos(a)

    else:

        return "Error"

def arctan(a):

    return m.atan(a)

def square(a):

    return a**2

def cube(a):

    return pow(a, 3)

def sqrt(a):

    if a >= 0:

        return m.sqrt(a)

    else:

        return "Error"

def sqrt3(a):

    if a < 0:
        return -((-a) ** (1/3))
    else:
        return a ** (1/3)

def pow10(a):

    return 10**a

def log(a):

    if a > 0:

        return m.log10(a)

    else:

        return "Error"

def ln(a):

    if a > 0:

        return m.log(a)

    else:

        return "Error"

def reciproco(a):

    if a != 0:

        return 1/a

    else:

        return "Error"

def absolute(a):

    return abs(a)

def factorial(a):

    if a >= 0 and type(a) == int:

        return m.factorial(a)

    else:

        return "Error"

def e_pow_x(a):

    return m.exp(a)
