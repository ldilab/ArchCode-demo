from solutions.HumanEval_83 import *
# Test Cases Regarding Functional Requirements
## General Cases
### For n = 2, there are 18 2-digit positive integers that start or end with 1
assert starts_one_ends(2) == 18, 'Failed to count the number of 2-digit positive integers that start or end with 1.'

### For n = 3, there are 180 3-digit positive integers that start or end with 1
assert starts_one_ends(3) == 180, 'Failed to count the number of 3-digit positive integers that start or end with 1.'

### For n = 4, there are 1800 4-digit positive integers that start or end with 1
assert starts_one_ends(4) == 1800, 'Failed to count the number of 4-digit positive integers that start or end with 1.'

## Edge Cases
### For n = 1, there is only one 1-digit positive integer that start or end with 1
assert starts_one_ends(1) == 1, 'Failed to count the number of 1-digit positive integers that start or end with 1.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input value of n fairly large, 1000
assert starts_one_ends(1000) == 18 * (10 ** 998), 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The input value of n is not a positive integer, so the function should raise a TypeError or return 0
assert not starts_one_ends(0), 'Failed to handle case where the input n is not a positive integer.'
assert not starts_one_ends(-1), 'Failed to handle case where the input n is not a positive integer.'
assert not starts_one_ends(1.5), 'Failed to handle case where the input n is not a positive integer.'
assert not starts_one_ends('invalid'), 'Failed to handle case where the input n is not a positive integer.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(starts_one_ends))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'