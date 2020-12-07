def f(x, y, z, a=0.1, b=0.08):
    """
    Returns (x+y)*a+z*b
    :param x: int.
    :param y: int.
    :param z: int.
    :param a: float default is 0.1.
    :param b: float default is 0.08.
    :return the float sum of (x+y)*a and z*b
    """
    return (x+y)*a+z*b

print(f(3,2,4))
#0.8200000000000001
