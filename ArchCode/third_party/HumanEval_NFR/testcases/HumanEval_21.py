from solutions.HumanEval_21 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The smallest number is 1 and the largest number is 5
### After rescaling, the smallest number becomes 0 and the largest number becomes 1
assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0], 'Failed to rescale the numbers correctly.'

## Edge Cases
### The input list is empty, so the function should return an empty list
assert rescale_to_unit([]) == [], 'Failed to handle an empty input list.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The nums list contains 10^6 elements with increasing values from 1 to 10^6
### After rescaling, the smallest number becomes 0 and the largest number becomes 1
assert all(abs(a - b) < 1e-5 for a, b in zip(rescale_to_unit(list(range(1, 10**6 + 1))), [i * 1e-6 for i in range(10**6 + 1)])), 'Failed to scale the input list.'


## Specific Quality Requirements
### Robustness
#### The input list has a single element, so the function should handle the case not to raise error
assert rescale_to_unit([3.14159]) == [], 'Failed to handle a single element input list.'

#### The numbers input is not a list of floats, so the function should handle the case not to raise error
assert not rescale_to_unit('invalid'), 'Failed to handle case where the input numbers is not a list of floats.'

#### The numbers list contains elements that are not floats, so the function should handle the case not to raise error
assert not rescale_to_unit([1, 2, 'invalid', 4.0]), 'Failed to handle case where the input list contains elements that are not floats.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(rescale_to_unit))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
