from solutions.HumanEval_5 import *
# Test Cases Regarding Functional Requirements
## General Cases
### Insert 4 between every two consecutive elements of the input list [1, 2, 3]
### The output should be [1, 4, 2, 4, 3]
assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3], 'Failed to insert delimeter between consecutive elements.'

## Edge Cases
### The input list is empty, so the function should return an empty list
assert intersperse([], 5) == [], 'Failed to handle an empty input list.'

### Insert 10 between every two consecutive elements of the input list [5, 5, 5, 5]
### The output should be [5, 10, 5, 10, 5, 10, 5]
assert intersperse([5, 5, 5, 5], 10) == [5, 10, 5, 10, 5, 10, 5], 'Failed to insert delimeter between consecutive elements when all elements have the same value.'

### Insert -1 between every two consecutive elements of the input list [1, 2, 3, 4, 5]
### The output should be [1, -1, 2, -1, 3, -1, 4, -1, 5]
assert intersperse([1, 2, 3, 4, 5], -1) == [1, -1, 2, -1, 3, -1, 4, -1, 5], 'Failed to insert delimeter between consecutive elements when delimeter is a negative number.'

### Insert 0 between every two consecutive elements of the input list [1, 2, 3, 4, 5]
### The output should be [1, 0, 2, 0, 3, 0, 4, 0, 5]
assert intersperse([1, 2, 3, 4, 5], 0) == [1, 0, 2, 0, 3, 0, 4, 0, 5], 'Failed to insert delimeter between consecutive elements when delimeter is zero.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The numbers list contains 10^6 elements with increasing values from 1 to 10^6
### Insert 1 between every two consecutive elements of the numbers list
### The output should be [1, 1, 2, 1, 3, 1, ..., 10^6, 1]
assert intersperse(list(range(1, 10**6 + 1)), 1) == [i for j in zip(range(1, 10**6 + 1), [1] * (10**6)) for i in j][:-1], 'Failed to handle case where the delimeter length is 1.'

## Specific Quality Requirements
### Robustness
#### The numbers input is not a list of integers, so the function should return an empty list
assert not intersperse('invalid', 10), 'Failed to handle case where the input numbers is not a list of integers.'

#### The delimeter input is not an integer, so the function should return an empty list
assert not intersperse([1, 2, 3], 'invalid'), 'Failed to handle case where the input delimeter is not an integer.'

#### The numbers list contains elements that are not integers, so the function should return an empty list
assert not intersperse([1, 2, 'invalid', 4], 5), 'Failed to handle case where the input list contains elements that are not integers.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(intersperse))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
