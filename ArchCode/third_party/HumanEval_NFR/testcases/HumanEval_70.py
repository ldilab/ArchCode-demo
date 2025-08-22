from solutions.HumanEval_70 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The minimum value is 1, the maximum value of the remaining integers is 4, and the minimum value is 2
assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3], 'Failed to sort the list in a strange order.'

### All elements in the list are the same, so the strange sorted list should be the same as the input list
assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5], 'Failed to handle case where all elements in the list are the same.'

### The input list is empty, so the function should return an empty list
assert strange_sort_list([]) == [], 'Failed to handle an empty input list.'

## Edge Cases
### The input list contains only one element, so the strange sorted list should be the same as the input list
assert strange_sort_list([10]) == [10], 'Failed to handle case where the input list contains only one element.'

### The minimum value is 2, the maximum value of the remaining integers is 4
assert strange_sort_list([4, 2]) == [2, 4], 'Failed to handle case where the input list contains two elements.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input list contains 10^4 elements with increasing values from 1 to 10^4
### The minimum value is 1, the maximum value of the remaining integers is 10^4, and so on
### The strange sorted list should be [1, 10^4, 2, 10^4 - 1, ..., 5000, 5001]
assert strange_sort_list(list(range(1, 10**4 + 1))) == [i // 2 + 1 if i % 2 == 1 else 10001 - i // 2 for i in range(1, 10001)], 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The lst input is not a list of integers, so the function should handle the case not to raise error
assert not strange_sort_list('invalid'), 'Failed to handle case where the input lst is not a list of integers.'

#### The lst list contains elements that are not integers, so the function should handle the case not to raise error
assert not strange_sort_list([1, 2, 'invalid', 4]), 'Failed to handle case where the input list contains elements that are not integers.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(strange_sort_list))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
