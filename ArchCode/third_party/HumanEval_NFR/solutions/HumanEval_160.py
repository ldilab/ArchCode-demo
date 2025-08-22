
def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """
    if not isinstance(operator, list) or not isinstance(operand, list):
        return None
    if len(operator) != len(operand)-1:
        return None
    for oprt in operator:
        if not isinstance(oprt, str):
            return None

    expression = str(operand[0])
    for oprt, oprn in zip(operator, operand[1:]):
        expression+= oprt + str(oprn)
    try:
        return eval(expression)
    except:
        return None
