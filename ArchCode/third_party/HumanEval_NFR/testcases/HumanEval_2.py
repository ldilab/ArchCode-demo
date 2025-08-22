from solutions.HumanEval_2 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The decimal part of 3.5 is 0.5
assert truncate_number(3.5) == 0.5, 'Failed to return the decimal part of the number.'

### The decimal part of 7.2 is 0.2
assert abs(truncate_number(7.2) - 0.2) < 1e-6, 'Failed to return the decimal part of the number.'

## Edge Cases
### The input number is zero, so the function should return zero as the decimal part
assert truncate_number(0) == 0, 'Failed to handle zero as input.'

### The input number is a very large float, so the function should return the decimal part without causing overflow or precision loss
assert truncate_number(10**100) == 0, 'Failed to handle very large input numbers.'

### The input number is a very small float, so the function should return the decimal part without causing underflow or precision loss
assert abs(truncate_number(10**-100)) < 1e-6, 'Failed to handle very small input numbers.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input number is within a reasonable range
### The function should provide results within a few milliseconds
assert abs(truncate_number(3.14159) - 0.14159) < 1e-6, 'Failed to meet performance requirements.'

### The input number is a very large float
### The function should provide results within a few milliseconds
assert truncate_number(10**100) == 0, 'Failed to meet performance requirements for very large input numbers.'

### The input number is a very small float
### The function should provide results within a few milliseconds
assert truncate_number(10**-1000) == 0, 'Failed to meet performance requirements for very small input numbers.'

## Specific Quality Requirements
### Robustness
#### The input number is not a float, so the function should handle the case not to raise error
assert not truncate_number('invalid'), 'Failed to handle non-float input.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(truncate_number))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
