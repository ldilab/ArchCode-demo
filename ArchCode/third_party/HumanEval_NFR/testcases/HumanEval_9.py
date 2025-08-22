from solutions.HumanEval_9 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The rolling maximum at each moment in the sequence is [1, 2, 3, 3, 3, 4, 4]
assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4], 'Failed to generate the correct rolling maximum sequence.'

### The rolling maximum at each moment in the sequence is [10, 10, 10, 10, 10]
assert rolling_max([10, 10, 10, 10, 10]) == [10, 10, 10, 10, 10], 'Failed to generate the correct rolling maximum sequence when all elements are the same.'

## Edge Cases
### The input list is empty, so the function should return an empty list
assert rolling_max([]) == [], 'Failed to handle an empty input list.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The numbers list contains 10^6 elements with increasing values from 1 to 10^6
### The rolling maximum at each moment in the sequence is [1, 2, 3, ..., 10^6]
assert rolling_max(list(range(1, 10**6 + 1))) == list(range(1, 10**6 + 1)), 'Failed to handle large input size.'

### The numbers list contains 10^6 elements with decreasing values from 10^6 to 1
### The rolling maximum at each moment in the sequence is [10^6, 10^6 - 1, 10^6 - 1, ..., 1]
assert rolling_max(list(range(10**6, 0, -1))) == [10**6] * 10**6, 'Failed to handle large input size with decreasing values.'

## Specific Quality Requirements
### Robustness
#### The numbers input is not a list of integers, so the function should return an empty list
assert not rolling_max('invalid'), 'Failed to handle case where the input numbers is not a list of integers.'

#### The numbers list contains elements that are not integers, so the function should return an empty list
assert not rolling_max([1, 2, 'invalid', 4]), 'Failed to handle case where the input list contains elements that are not integers.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(rolling_max))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
