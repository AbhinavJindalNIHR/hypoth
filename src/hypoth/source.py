

#Requirements
#    2 inputs, positive, int or float (is digit)
#    1 output, float
#            external library? no external lib


#create a function : calculate hypot = sqrt(a^2 + b^2)
def hypoth(a,b):
    """This is hypoth function

    Args:
        a (int, float): Side of triangle
        b (int, float): second side of triangle

    Returns:
        float: hypotenuse
    """
    return sqrt((a**2 + b**2))
#create s sqrt func: positive num - returns a float
def sqrt(a):
    """Square root function

    Args:
        a (int, float): positive or negative number
    """
    return(a**0.5)

print(sqrt(4))
print(hypoth(3,4))

print(sqrt(4))
print(hypoth(3,4))

