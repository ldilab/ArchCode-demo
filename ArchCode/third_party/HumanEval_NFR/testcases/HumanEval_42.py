from solutions.HumanEval_42 import *
# Test Cases Regarding Functional Requirements
## General Cases
### Increment each element of the list by 1
assert incr_list([1, 2, 3]) == [2, 3, 4], 'Failed to increment each element by 1.'

### Increment each element of the list by 1
assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124], 'Failed to increment each element by 1.'

## Edge Cases
### The input list is empty, so the function should return an empty list
assert incr_list([]) == [], 'Failed to handle an empty input list.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input list contains 10^6 elements with increasing values from 1 to 10^6
### Increment each element of the list by 1
assert incr_list(list(range(1, 10**6 + 1))) == list(range(2, 10**6 + 2)), 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The input is not a list, so the function should handle the case not to raise error
assert not incr_list('invalid'), 'Failed to raise TypeError when the input is not a list.'

### The input list contains non-integer elements, so the function should handle the case not to raise error
assert incr_list([1, 2, '3']), 'Failed to raise TypeError when the input list contains non-integer elements.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(incr_list))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
