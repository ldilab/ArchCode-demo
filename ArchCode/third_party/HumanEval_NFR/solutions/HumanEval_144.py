
def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    if not isinstance(x, str) or not isinstance(n, str):
        return None
    if not x or not n:
        return None
    import re
    if not re.match(r"^\d+/\d+$", x) or not re.match(r"^\d+/\d+$", n):
        return None

    a, b = x.split("/")
    c, d = n.split("/")
    if int(b) == 0 or int(d) == 0:
        return None
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    if (numerator/denom == int(numerator/denom)):
        return True
    return False
