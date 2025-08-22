from solutions.HumanEval_69 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The integer 2 has a frequency of 2, which is equal to its value
### Therefore, the function should return 2
assert search([4, 1, 2, 2, 3, 1]) == 2, 'Failed to find the greatest integer with frequency greater than or equal to its value.'

### The integer 3 has a frequency of 3, which is greater than its value
### Therefore, the function should return 3
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3, 'Failed to find the greatest integer with frequency greater than or equal to its value.'

### No integer has a frequency greater than or equal to its value
### Therefore, the function should return -1
assert search([5, 5, 4, 4, 4]) == -1, 'Failed to handle case where no integer satisfies the condition.'

## Edge Cases
### The input list contains a single element, which does not satisfy the condition
### Therefore, the function should return -1
assert search([5]) == -1, 'Failed to handle case where the list contains a single element that satisfies the condition.'

### All elements in the input list have frequencies less than their own values
### Therefore, the function should return -1
assert search([2, 3, 4, 5]) == -1, 'Failed to handle case where no integer satisfies the condition.'

### Multiple integers have frequencies greater than or equal to their values
### The function should return the greatest one, which is 4
assert search([2, 2, 4, 4, 4, 4]) == 4, 'Failed to find the greatest integer when multiple integers satisfy the condition.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input list contains 10^6 elements, all of which are 1
### The greatest integer with frequency greater than or equal to its value is 1
assert search([1] * 10**6) == 1, 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
### Empty input list
### Since the input list is empty, there is no integer that satisfies the condition
### The function should handle the case not to raise error
assert not search([]), 'Failed to handle case where the input list is empty.'

#### The input is not a list, so the function should handle the case not to raise error
assert not search('invalid'), 'Failed to handle case where the input is not a list.'

#### The input list contains non-integer elements, so the function should handle the case not to raise error
assert not search([1, 2, 'invalid', 4]), 'Failed to handle case where the input list contains non-integer elements.'

#### The input list contains negative elements, so the function should handle the case not to raise error
assert not search([1, 2, 3, -4, 5]), 'Failed to handle case where the input list contains negative elements.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(search))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
