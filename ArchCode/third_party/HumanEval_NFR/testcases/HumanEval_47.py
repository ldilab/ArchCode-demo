from solutions.HumanEval_47 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The list is [3, 1, 2, 4, 5]
### The median is 3
assert median([3, 1, 2, 4, 5]) == 3, 'Failed to calculate the median for an odd-length list.'

### The list is [-10, 4, 6, 1000, 10, 20]
### The median is (6 + 10) / 2 = 8
assert median([-10, 4, 6, 1000, 10, 20]) == 8, 'Failed to calculate the median for an even-length list.'

## Edge Cases
### The list is empty, so the function should handle the case not to raise error
assert not median([]), 'Failed to handle an empty list.'

### The list contains a single element, so the function should return that element as the median
assert median([100]) == 100, 'Failed to handle a list with a single element.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The list contains 10^6 elements with increasing values from 1 to 10^6
### The median is 500000.5
assert median(list(range(1, 10**6 + 1))) == 500000.5, 'Failed to handle large input size.'

### The list contains 10^6 elements, all of which are 10^6
### The median is 10^6
assert median([10**6] * 10**6) == 10**6, 'Failed to handle case where all elements in the list have the same value.'

## Specific Quality Requirements
### Robustness
#### The l input is not a list, so the function should handle the case not to raise error
assert not median('invalid'), 'Failed to handle case where the input l is not a list.'

#### The l list contains elements that are not integers, so the function should handle the case not to raise error
assert not median([1, 2, 'invalid', 4]), 'Failed to handle case where the input list contains elements that are not integers.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(median))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
