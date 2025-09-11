from solutions.HumanEval_146 import *
# Test Cases Regarding Functional Requirements
## General Cases
### Only one number, 15, is greater than 10 and has both first and last digits odd
assert specialFilter([15, -73, 14, -15]) == 1, 'Failed to count the correct number of elements.'

### Two numbers, 33 and 109, are greater than 10 and have both first and last digits odd
assert specialFilter([33, -2, -3, 45, 21, 109]) == 2, 'Failed to count the correct number of elements.'

## Edge Cases
### The input list is empty, so the function should return 0
assert specialFilter([]) == 0, 'Failed to handle an empty input list.'

### None of the numbers are greater than 10 and have both first and last digits odd
### The function should return 0
assert specialFilter([2, 4, 6, 8]) == 0, 'Failed to handle case where no element satisfies the condition.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The nums list contains 10^6 elements, all of which are greater than 10 and have both first and last digits odd
### The function should return the count of all elements, which is 10^6
assert specialFilter([11, 13, 15, 17, 19] * (10**6 // 5)) == 10**6, 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The nums input is not a list, so the function should handle the case not to raise error
assert not specialFilter('invalid'), 'Failed to handle case where the input nums is not a list.'

#### The nums list contains elements that are not numbers, so the function should handle the case not to raise error
assert not specialFilter([1, 'invalid', 3, 5]), 'Failed to handle case where the input list contains elements that are not numbers.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(specialFilter))
assert result.total_complexity <= 10, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'