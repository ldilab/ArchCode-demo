from solutions.HumanEval_68 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The smallest even value is 2, and it has the smallest index
assert pluck([4, 2, 3]) == [2, 1], 'Failed to find the smallest even value with the smallest index.'

### The smallest even value is 2, and it has the smallest index
assert pluck([1, 2, 3]) == [2, 1], 'Failed to find the smallest even value with the smallest index.'

### The input list is empty, so the function should return an empty list
assert pluck([]) == [], 'Failed to handle an empty input list.'

### The smallest even value is 0, but there are two zeros, so we choose the first zero with the smallest index
assert pluck([5, 0, 3, 0, 4, 2]) == [0, 1], 'Failed to handle multiple nodes with the same smallest even value.'

## Edge Cases
### The input list contains no even values, so the function should return an empty list
assert pluck([1, 3, 5]) == [], 'Failed to handle case where no even values are found.'

### The input list contains only odd values, so the function should return an empty list
assert pluck([1, 3, 5, 7]) == [], 'Failed to handle case where no even values are found.'

### The input list contains a single node with a value of 0, which is the smallest even value
assert pluck([0]) == [0, 0], 'Failed to handle case where the input list contains a single node.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input list contains 10^6 elements, all of which are odd
### The function should return an empty list since there are no even values
assert pluck([1] * 10**6) == [], 'Failed to handle large input size.'

### The input list contains 10^6 elements, all of which are even
### The function should return [0, 0] since 0 is the smallest even value and has the smallest index
assert pluck([0] * 10**6) == [0, 0], 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The arr input is not a list, so the function should handle the case not to raise error
assert not pluck('invalid'), 'Failed to handle case where the input arr is not a list.'

#### The arr list contains elements that are not integers, so the function should handle the case not to raise error
assert not pluck([1, 2, 'invalid', 4]), 'Failed to handle case where the input list contains elements that are not integers.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(pluck))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
