from solutions.HumanEval_3 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The balance never falls below zero, so the function should return False
assert below_zero([1, 2, 3]) == False, 'Failed to handle case where balance never falls below zero.'

### The balance falls below zero at index 2, so the function should return True
assert below_zero([1, 2, -4, 5]) == True, 'Failed to detect when the balance falls below zero.'

## Edge Cases
### The operations list is empty, so the function should return False
assert below_zero([]) == False, 'Failed to handle an empty input list.'

### The balance never falls below zero, so the function should return False
assert below_zero([0, 0, 0, 0, 0]) == False, 'Failed to handle case where the balance remains at zero throughout the list.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The operations list contains 10^6 elements, all of which are 1
### The balance never falls below zero, so the function should return False
assert below_zero([1] * 10**6) == False, 'Failed to handle large input size.'

### The operations list contains 10^6 elements, all of which are -1
### The balance falls below zero at index 0, so the function should return True
assert below_zero([-1] * 10**6) == True, 'Failed to handle large input size.'

### The operations list contains 10^6 elements, alternating between 1 and -1
### The balance does not fall below zero until the end, so the function should return False
assert below_zero([1, -1] * (10**6 // 2)) == False, 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The operations input is not a list of integers, so the function should handle the case not to raise error
assert not below_zero('invalid'), 'Failed to handle case where the input operations is not a list of integers.'

#### The operations list contains elements that are not integers, so the function should handle the case not to raise error
assert not below_zero([1, 2, 'invalid', 4]), 'Failed to handle case where the input list contains elements that are not integers.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(below_zero))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
