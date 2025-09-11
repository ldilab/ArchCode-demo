from solutions.HumanEval_35 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The maximum element in the list is 3
assert max_element([1, 2, 3]) == 3, 'Failed to find the maximum element.'

### The maximum element in the list is 123
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123, 'Failed to find the maximum element.'

## Edge Cases
### The list contains multiple maximum elements 4, so the function can return any of them
assert max_element([1, 3, 2, 4, 3, 4]) == 4, 'Failed to handle case with duplicate maximum elements.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The list contains 10^6 elements with increasing values from 1 to 10^6
### The maximum element in the list is 10^6
assert max_element(list(range(1, 10**6 + 1))) == 10**6, 'Failed to handle large input size.'

### The list contains 10^6 elements, all of which are 10^6
### The maximum element in the list is 10^6
assert max_element([10**6] * 10**6) == 10**6, 'Failed to handle case where all elements have the same value.'

## Specific Quality Requirements
### Robustness
#### The list is empty, so the function should handle the case not to raise error
assert not max_element([]), 'Failed to handle an empty list.'

#### The input is not a list, so the function should handle the case not to raise error
assert not max_element('invalid'), 'Failed to handle case where the input is not a list.'

#### The list contains elements that are not integers, so the function should handle the case not to raise error
assert not max_element([1, 2, 'invalid', 4]), 'Failed to handle case where the list contains elements that are not integers.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(max_element))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
