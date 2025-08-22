from solutions.HumanEval_20 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The closest elements in the list are 2.0 and 2.2
assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2), 'Failed to find the closest elements in the list.'

### The closest elements in the list are both 2.0
assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0), 'Failed to handle case where there are duplicate closest elements.'

## Edge Cases
### The numbers list has less than two elements, so the function should raise a ValueError or handle the case not to raise error
assert not find_closest_elements([]), 'Failed to handle case where the numbers list has less than two elements.'
assert not find_closest_elements([1.0]), 'Failed to handle case where the numbers list has less than two elements.'

### The numbers list contains duplicate elements, so the function should handle it correctly
### The closest elements in the list are 1.0 and 1.0
assert find_closest_elements([1.0, 1.0, 1.0, 1.0]) == (1.0, 1.0), 'Failed to handle case where there are duplicate elements in the numbers list.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The numbers list contains 10^4 elements with increasing values from 1 to 10^4
### The closest elements in the list are 1 and 2
assert find_closest_elements(list(range(1, 10**4 + 1))) == (1, 2), 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The numbers input is not a list of floats, so the function should handle the case not to raise error
assert not find_closest_elements('invalid'), 'Failed to handle case where the input numbers is not a list of floats.'

#### The numbers list contains elements that are not floats, so the function should handle the case not to raise error
assert not find_closest_elements([1.0, 2.0, 'invalid', 4.0]), 'Failed to handle case where the input list contains elements that are not floats.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 10
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(find_closest_elements))
assert result.total_complexity <= 10, 'Failed to have a Cyclomatic Complexity less than or equal to 10 by Radon.'
