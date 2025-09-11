from solutions.HumanEval_58 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The common elements between the two lists are [1, 5, 653]
assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653], 'Failed to find the common elements.'

### The common elements between the two lists are [2, 3]
assert common([5, 3, 2, 8], [3, 2]) == [2, 3], 'Failed to find the common elements.'

## Edge Cases
### Both input lists are empty, so the function should return an empty list
assert common([], []) == [], 'Failed to handle empty input lists.'

### There are no common elements between the two lists, so the function should return an empty list
assert common([1, 2, 3], [4, 5, 6]) == [], 'Failed to handle case where there are no common elements.'

### The common elements between the two lists are [1]
assert common([1, 1, 1], [1, 1, 1]) == [1], 'Failed to handle case with multiple common elements.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input lists contain 10^6 elements each, with all elements being unique
### The common elements between the two lists are [1, 2, 3, ..., 10^6]
assert common(list(range(1, 10**6 + 1)), list(range(1, 10**6 + 1))) == list(range(1, 10**6 + 1)), 'Failed to handle large input size.'

### The input lists contain 10^6 elements each, with no common elements
### The function should return an empty list
assert common(list(range(1, 10**6 + 1)), list(range(10**6 + 1, 2*10**6 + 1))) == [], 'Failed to handle case where there are no common elements.'

## Specific Quality Requirements
### Robustness
#### The input lists contain non-integer elements, so the function should return is None
assert not common([1, 2, 'invalid', 4], [3, 2, 'invalid']), 'Failed to handle case where the input lists contain non-integer elements.'

#### The input l1 is not a list, so the function should return is None
assert not common('invalid', [1, 2, 3]), 'Failed to handle case where the input l1 is not a list.'

#### The input l2 is not a list, so the function should return is None
assert not common([1, 2, 3], 'invalid'), 'Failed to handle case where the input l2 is not a list.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(common))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
