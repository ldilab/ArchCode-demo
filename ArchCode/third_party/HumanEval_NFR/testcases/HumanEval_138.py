from solutions.HumanEval_138 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The number 4 cannot be written as the sum of exactly 4 positive even numbers
assert is_equal_to_sum_even(4) == False, 'Failed to handle case where the number cannot be written as the sum of 4 positive even numbers.'

### The number 6 cannot be written as the sum of exactly 4 positive even numbers
assert is_equal_to_sum_even(6) == False, 'Failed to handle case where the number cannot be written as the sum of 4 positive even numbers.'

### The number 8 can be written as the sum of exactly 4 positive even numbers
assert is_equal_to_sum_even(8) == True, 'Failed to handle case where the number can be written as the sum of 4 positive even numbers.'

## Edge Cases
### The number is negative, so it cannot be written as the sum of 4 positive even numbers
assert is_equal_to_sum_even(-10) == False, 'Failed to handle case where the number is negative.'

### The number is not an integer, so it cannot be written as the sum of 4 positive even numbers
assert is_equal_to_sum_even(8.5) == False, 'Failed to handle case where the number is not an integer.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The number 10^9 can be written as the sum of exactly 4 positive even numbers
assert is_equal_to_sum_even(10**9) == True, 'Failed to handle case where the number is large.'

## Specific Quality Requirements
### Robustness
#### The input is not an integer, so the function should handle the case not to raise error
assert not is_equal_to_sum_even('invalid'), 'Failed to handle case where the input is not an integer.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(is_equal_to_sum_even))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
