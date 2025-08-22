from solutions.HumanEval_126 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The list [1, 2, 3, 4, 5] is sorted in ascending order and has no duplicates
### The function should return True
assert is_sorted([1, 2, 3, 4, 5]) == True, 'Failed for sorted list.'

### The list [1, 3, 2, 4, 5] is not sorted in ascending order
### The function should return False
assert is_sorted([1, 3, 2, 4, 5]) == False, 'Failed for unsorted list.'

### The list [1, 2, 3, 4, 5, 6, 7] is sorted in ascending order and has no duplicates
### The function should return True
assert is_sorted([1, 2, 3, 4, 5, 6, 7]) == True, 'Failed for sorted list.'

### The list [1, 3, 2, 4, 5, 6, 7] is not sorted in ascending order
### The function should return False
assert is_sorted([1, 3, 2, 4, 5, 6, 7]) == False, 'Failed for unsorted list.'

### The list [1, 2, 2, 3, 3, 4] is sorted in ascending order and has no more than 1 duplicate of the same number
### The function should return True
assert is_sorted([1, 2, 2, 3, 3, 4]) == True, 'Failed for sorted list with duplicates.'

### The list [1, 2, 2, 2, 3, 4] is not sorted in ascending order
### The function should return False
assert is_sorted([1, 1, 2, 2, 2, 3, 4]) == False, 'Failed for unsorted list with duplicates.'

## Edge Cases
### The list is empty, so the function should return True
assert is_sorted([]) == True, 'Failed for empty list.'

### The list [5] is already sorted in ascending order and has no duplicates
### The function should return True
assert is_sorted([5]) == True, 'Failed for single-element sorted list.'

### The list [1, 1, 1] has more than 1 duplicate of the same number
### The function should return False
assert is_sorted([1, 1, 1]) == False, 'Failed for list with multiple duplicates.'

### The list [3, 2, 1] is not sorted in ascending order
### The function should return False
assert is_sorted([3, 2, 1]) == False, 'Failed for sorted in descending order.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The list contains 10^6 elements with increasing values from 1 to 10^6
### The list is sorted in ascending order and has no duplicates
### The function should return True
assert is_sorted(list(range(1, 10**6 + 1))) == True, 'Failed to handle large input size.'

### The list contains 10^6 elements with increasing values from 1 to 10^6
### The list is already sorted and every value has exactly one duplicate
### The function should return True
assert is_sorted([x for x in range(1, 10**6+1) for _ in range(2)]) == True, 'Failed to handle large input size.'

### The list contains 10^6 elements, all of which are 1
### The list is sorted but has too many duplicates
### The function should return False
assert is_sorted([1] * 10**6) == False, 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The lst input is not a list, so the function should handle the case not to raise error
assert not is_sorted('invalid'), 'Failed to handle case where the input lst is not a list.'

#### The lst input contains elements that are not integers, so the function should handle the case not to raise error
assert not is_sorted([1, 2, 'invalid', 4]), 'Failed to handle case where the input list contains elements that are not integers.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(is_sorted))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'