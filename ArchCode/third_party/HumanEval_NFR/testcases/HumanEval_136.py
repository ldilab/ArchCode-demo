from solutions.HumanEval_136 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The largest negative integer is -2 and the smallest positive integer is 1
assert largest_smallest_integers([2, 4, -2, 1, 3, 5, 7]) == (-2, 1), 'Failed to find the largest negative and smallest positive integers.'

### There are no negative integers in the list, so the largest negative integer should be None
assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1), 'Failed to handle case where there are no negative integers.'

### There are no positive integers in the list, so the smallest positive integer should be None
assert largest_smallest_integers([-2, -4, -1, -3, -5, -7]) == (-1, None), 'Failed to handle case where there are no positive integers.'

## Edge Cases
### The input list is empty, so both the largest negative and smallest positive integers should be None
assert largest_smallest_integers([]) == (None, None), 'Failed to handle an empty input list.'

### The input list contains only 0, so both the largest negative and smallest positive integers should be None
assert largest_smallest_integers([0]) == (None, None), 'Failed to handle case where the list contains only 0.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input list contains 10^6 elements with increasing values from -10^6 to 10^6
### The largest negative integer is -1 and the smallest positive integer is 1
assert largest_smallest_integers(list(range(-10**6, 10**6 + 1))) == (-1, 1), 'Failed to handle large input size.'

### The input list contains 10^6 elements with increasing values from -10^6 to -1
### There are no positive integers in the list, so the smallest positive integer should be None
assert largest_smallest_integers(list(range(-10**6, 0))) == (-1, None), 'Failed to handle case where there are no positive integers.'

### The input list contains 10^6 elements with decreasing values from 10^6 to 1
### There are no negative integers in the list, so the largest negative integer should be None
assert largest_smallest_integers(list(range(10**6, 0, -1))) == (None, 1), 'Failed to handle case where there are no negative integers.'

## Specific Quality Requirements
### Robustness
#### The input list is not a list, so the function should handle the case not to raise error
assert not largest_smallest_integers('invalid'), 'Failed to handle case where the input list is not a list.'

#### The input list contains elements that are not integers, so the function should handle the case not to raise error
assert not largest_smallest_integers([1, 2, 'invalid', 4]), 'Failed to handle case where the input list contains elements that are not integers.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(largest_smallest_integers))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
