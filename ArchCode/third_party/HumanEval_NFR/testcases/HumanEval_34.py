from solutions.HumanEval_34 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The input list contains duplicate elements
### The function should return the unique elements in sorted order
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123], 'Failed to return sorted unique elements.'

### The input list contains no duplicate elements
### The function should return the unique elements in sorted order
assert unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], 'Failed to return sorted unique elements when there are no duplicates.'

## Edge Cases
### The input list is empty, so the function should return an empty list
assert unique([]) == [], 'Failed to handle an empty input list.'

### The input list contains all duplicate elements
### The function should return a list with a single element, the first occurrence of the element
assert unique([1, 1, 1, 1, 1, 1]) == [1], 'Failed to handle case where all elements in the list are duplicates.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input list contains 10^6 elements, all of which are the same value 1
### The function should return a list with a single element, 1
assert unique([1] * 10**6) == [1], 'Failed to handle large input size.'

### The input list contains 10^6 elements, all of which are unique
### The function should return the same list in sorted order
assert unique(list(range(1, 10**6 + 1))) == list(range(1, 10**6 + 1)), 'Failed to handle large input size with unique elements.'

### The input list contains 10^6 elements, all of which are unique and in reverse order
### The function should return the same list in sorted order
assert unique(list(range(10**6, 0, -1))) == list(range(1, 10**6 + 1)), 'Failed to handle large input size with unique elements in reverse order.'

## Specific Quality Requirements
### Robustness
#### The input is not a list, so the function should handle the case not to raise error
assert not unique('invalid'), 'Failed to handle case where the input is not a list.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(unique))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
