
def f(x):
    """
    Returns float of input string.
    :param x: int,float or String number
    try float but if ValueError, print "Invalid input"
    """
    try:
        return float(x)
    except ValueError:
        print("Invalid input")

print(f(10))
print(f("ten"))
