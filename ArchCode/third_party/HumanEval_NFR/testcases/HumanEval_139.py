from solutions.HumanEval_139 import *
# Test Cases Regarding Functional Requirements
## General Cases
### special_factorial(4) = 4! * 3! * 2! * 1! = 24 * 6 * 2 * 1 = 288
assert special_factorial(4) == 288, 'Failed to calculate the special factorial correctly.'

### special_factorial(5) = 5! * 4! * 3! * 2! * 1! = 120 * 24 * 6 * 2 * 1 = 34560
assert special_factorial(5) == 34560, 'Failed to calculate the special factorial correctly.'

### special_factorial(6) = 6! * 5! * 4! * 3! * 2! * 1! = 720 * 120 * 24 * 6 * 2 * 1 = 24883200
assert special_factorial(6) == 24883200, 'Failed to calculate the special factorial correctly.'

## Edge Cases
### special_factorial(1) = 1
assert special_factorial(1) == 1, 'Failed to handle the special factorial of 1.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### Calculate the special factorial for a input value of 10^3
### The function should provide the result in 5 seconds.
assert isinstance(special_factorial(10**3), int) == True, 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
### special_factorial(0) is None
### The function should handle the case not to raise error for any input of 0 or 1.
assert not special_factorial(0), 'Failed to handle the special factorial of 0.'

#### The input `n` is a negative number, so the function should handle the case not to raise error.
assert not special_factorial(-10), 'Failed to handle case where `n` is a negative number.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(special_factorial))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
