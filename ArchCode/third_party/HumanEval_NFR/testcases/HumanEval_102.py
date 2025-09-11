from solutions.HumanEval_102 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The biggest even number in the range [12, 15] is 14
assert choose_num(12, 15) == 14, 'Failed to find the biggest even number in the range.'

### The range [3, 9] contains the even numbers [4, 6, 8]
### The biggest even number in the range is 8
assert choose_num(3, 9) == 8, 'Failed to handle case where there are multiple even numbers in the range.'

## Edge Cases
### The range [5, 5] contains only one number, which is odd
assert choose_num(5, 5) == -1, 'Failed to handle case where the range contains only one number, which is odd.'

### The range [6, 6] contains only one number, which is even
assert choose_num(6, 6) == 6, 'Failed to handle case where the range contains only one number, which is even.'

### There are no even numbers in the range [13, 12]
assert choose_num(13, 12) == -1, 'Failed to handle case where there are no numbers in the range.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The range [1, 10^6+1] contains 10^6+1 numbers
assert choose_num(1, 10**6+1) == 10**6, 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The input `x` is not an integer, so the function should handle the case not to raise error
assert not choose_num(5.5, 10), 'Failed to handle case where the input `x` is not an integer.'

#### The input `y` is not an integer, so the function should handle the case not to raise error
assert not choose_num(5, 10.5), 'Failed to handle case where the input `y` is not an integer.'

#### The inputs `x` and `y` are not integers, so the function should handle the case not to raise error
assert not choose_num(5.5, 10.5), 'Failed to handle case where both inputs `x` and `y` are not integers.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(choose_num))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'