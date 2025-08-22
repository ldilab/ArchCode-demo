from solutions.HumanEval_88 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The sum of the first and last elements is odd, so the array should be sorted in ascending order
assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5], 'Failed to sort the array in ascending order when the sum is odd.'

### The sum of the first and last elements is even, so the array should be sorted in descending order
assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0], 'Failed to sort the array in descending order when the sum is even.'

## Edge Cases
### The input array is empty, so the function should return an empty array
assert sort_array([]) == [], 'Failed to handle an empty input array.'

### The input array has a single element, so the function should return a copy of the input array
assert sort_array([5]) == [5], 'Failed to handle an input array with a single element.'

### The input array has a single element, so the function should return a copy of the input array
assert sort_array([4]) == [4], 'Failed to handle an input array with a single element.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input array contains 10^6 elements in ascending order from 0 to 10^6 - 1
### The sum of the first and last elements is odd, so the array should be sorted in ascending order
assert sort_array(list(range(10**6))) == list(range(10**6)), 'Failed to handle large input size.'

### The input array contains 10^6 elements in descending order from 10^6 - 1 to 0
### The sum of the first and last elements is odd, so the array should be sorted in ascending order
assert sort_array(list(range(10**6 - 1, -1, -1))) == list(range(10**6)), 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The input is not an array, so the function should handle the case not to raise error
assert not sort_array('invalid'), 'Failed to handle case where the input is not an array.'

#### The input array contains elements that are not integers, so the function should handle the case not to raise error
assert not sort_array([2, 4, 'invalid', 0, 1, 5, 6]), 'Failed to handle case where the input array contains elements that are not integers.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 10
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(sort_array))
assert result.total_complexity <= 10, 'Failed to have a Cyclomatic Complexity less than or equal to 10 by Radon.'