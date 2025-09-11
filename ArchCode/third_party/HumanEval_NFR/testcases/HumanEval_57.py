from solutions.HumanEval_57 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The elements in the list are monotonically increasing, so the function should return True
assert monotonic([1, 2, 4, 20]) == True, 'Failed to recognize monotonically increasing list.'

### The elements in the list are not monotonically increasing or decreasing, so the function should return False
assert monotonic([1, 20, 4, 10]) == False, 'Failed to recognize non-monotonic list.'

### The elements in the list are monotonically decreasing, so the function should return True
assert monotonic([4, 1, 0, -10]) == True, 'Failed to recognize monotonically decreasing list.'

## Edge Cases
### The list is empty, so the function should return True
assert monotonic([]) == True, 'Failed to handle an empty list.'

### The list has a single element, so the function should return True
assert monotonic([10]) == True, 'Failed to handle a list with a single element.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The list contains 10^6 elements with increasing values from 1 to 10^6
### The elements are monotonically increasing, so the function should return True
assert monotonic(list(range(1, 10**6 + 1))) == True, 'Failed to handle large input size.'

### The list contains 10^6 elements with decreasing values from 10^6 to 1
### The elements are monotonically decreasing, so the function should return True
assert monotonic(list(range(10**6, 0, -1))) == True, 'Failed to handle large input size with monotonically decreasing elements.'

### The list contains 10^6 elements with alternating values of 1 and 2
### The elements are not monotonically increasing or decreasing, so the function should return False
assert monotonic([1, 2] * (10**6 // 2)) == False, 'Failed to handle large input size with non-monotonic elements.'

## Specific Quality Requirements
### Robustness
#### The input is not a list, so the function should handle the case not to raise error
assert not monotonic('invalid'), 'Failed to handle case where the input is not a list.'

#### The input list contains elements that are not integers or floats, so the function should handle the case not to raise error
assert not monotonic([1, 2, 'invalid', 4]), 'Failed to handle case where the input list contains elements that are not integers or floats.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(monotonic))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
