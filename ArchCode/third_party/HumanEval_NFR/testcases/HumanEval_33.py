from solutions.HumanEval_33 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The indices divisible by three are [0, 3, 6]
### The sorted values at these indices are [2, 4, 5]
### The function should return [2, 6, 3, 4, 8, 9, 5]
assert sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5], 'Failed to sort values at indices divisible by three.'

### Only one indice divisible by three is [0]
### The function should return the input list unchanged
assert sort_third([1, 2, 3]) == [1, 2, 3], 'Failed to handle case where there are no indices divisible by three.'

## Edge Cases
### The input list is empty, so the function should return an empty list
assert sort_third([]) == [], 'Failed to handle an empty input list.'

### All indices in the input list divisible by three are already sorted
### The function should return the input list sorted
assert sort_third([9, 6, 3, 12, 15]) == [9, 6, 3, 12, 15], 'Failed to handle case where all indices are divisible by three.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input list contains 10^6 elements in ascending order from 1 to 10^6
### None of the indices in the input list are divisible by three
### The function should return the input list unchanged
assert sort_third(list(range(1, 10**6 + 1))) == list(range(1, 10**6 + 1)), 'Failed to handle case where there are no indices divisible by three.'

## Specific Quality Requirements
### Robustness
#### The input is not a list, so the function should handle the case not to raise error
assert not sort_third('invalid'), 'Failed to handle case where the input is not a list.'

#### The input list contains a non-integer element, so the function should handle the case not to raise error
assert not sort_third([1, 2, 3, 'invalid']), 'Failed to handle case where the input list contains non-integer elements.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(sort_third))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
