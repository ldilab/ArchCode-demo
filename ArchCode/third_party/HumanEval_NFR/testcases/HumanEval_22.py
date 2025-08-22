from solutions.HumanEval_22 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The input list contains a mix of integer and non-integer values
### The function should filter out non-integer values and return only the integer values
assert filter_integers(['a', 3.14, 5]) == [5], 'Failed to filter out non-integer values.'

### The input list contains a mix of integer and non-integer values
### The function should filter out non-integer values and return only the integer values
assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3], 'Failed to filter out non-integer values.'

## Edge Cases
### The input list is empty, so the function should return an empty list
assert filter_integers([]) == [], 'Failed to handle an empty input list.'

### The input list contains no integer values, so the function should return an empty list
assert filter_integers(['a', 'b', 'c']) == [], 'Failed to handle case where there are no integer values.'

### The input list contains only integer values, so the function should return the same list
assert filter_integers([1, 2, 3]) == [1, 2, 3], 'Failed to handle case where all values are integers.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input list contains 10^6 elements, all of which are integers
### The function should return the same list, without any filtering
assert filter_integers(list(range(1, 10**6 + 1))) == list(range(1, 10**6 + 1)), 'Failed to handle large input size.'

### The input list contains 10^6 elements, all of which are non-integer values
### The function should return an empty list, as there are no integer values to filter
assert filter_integers(['a'] * 10**6) == [], 'Failed to handle large input size with no integer values.'

### The input list contains 10^6 elements, alternating between integer and non-integer values
### The function should filter out the non-integer values and return only the integer values
assert filter_integers([1, 'a', 2, 'b'] * (10**6 // 4)) == [1, 2] * (10**6 // 4), 'Failed to handle large input size with alternating integer and non-integer values.'

## Specific Quality Requirements
### Robustness
#### The values input is not a list, so the function should return an None
assert not filter_integers('invalid'), 'Failed to handle case where the input values is not a list.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(filter_integers))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
