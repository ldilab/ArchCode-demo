from solutions.HumanEval_150 import *
# Test Cases Regarding Functional Requirements
## General Cases
### 7 is a prime number, so the function should return the value of x which is 34
assert x_or_y(7, 34, 12) == 34, 'Failed to return the value of x for a prime number.'

### 15 is not a prime number, so the function should return the value of y which is 5
assert x_or_y(15, 8, 5) == 5, 'Failed to return the value of y for a non-prime number.'

## Edge Cases
### The input number is negative, so the function should return the value of y which is -5
assert x_or_y(-7, 34, -5) == -5, 'Failed to handle a negative input number.'

### The input number is 0, which is not a prime number, so the function should return the value of y which is 0
assert x_or_y(0, 34, 0) == 0, 'Failed to handle a zero input number.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input number is a prime number
### The function should return the value of x within 1 second
assert x_or_y(99991, 34, 0) == 34, 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The input number is not an integer, so the function should handle the case not to raise error
assert not x_or_y('invalid', 34, 0), 'Failed to handle a non-integer input number.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 3
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(x_or_y))
assert result.total_complexity <= 10, 'Failed to have a Cyclomatic Complexity less than or equal to 3 by Radon.'