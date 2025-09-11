from solutions.HumanEval_62 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The derivative of the polynomial 3 + x + 2x^2 + 4x^3 + 5x^4 is 1 + 4x + 12x^2 + 20x^3
assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20], 'Failed to compute the derivative of the polynomial.'

### The derivative of the polynomial 1 + 2x + 3x^2 is 2 + 6x
assert derivative([1, 2, 3]) == [2, 6], 'Failed to compute the derivative of the polynomial.'

## Edge Cases
### The input list is empty, so the function should return an empty list
assert derivative([]) == [], 'Failed to handle an empty input list.'

### The input list has a single element, so the derivative is []
assert derivative([5]) == [], 'Failed to handle case where the input list has a single element.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input list has 10^6 elements, all of which are 1
### The derivative of the polynomial is a list of [1, 2, 3 ... 10**6 - 1]
assert derivative([1] * 10**6) == [i for i in range(1, 10**6)], 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The xs input is not a list, so the function should handle the case not to raise error
assert not derivative('invalid'), 'Failed to handle case where the input xs is not a list.'

#### The xs list contains elements that are not integers, so the function should handle the case not to raise error
assert not derivative([1, 2, 'invalid', 4]), 'Failed to handle case where the input list contains elements that are not integers.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(derivative))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
