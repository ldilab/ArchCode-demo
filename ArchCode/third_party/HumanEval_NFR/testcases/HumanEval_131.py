from solutions.HumanEval_131 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The number 235 has odd digits 3 and 5, and their product is 15
assert digits(235) == 15, 'Failed to find the product of odd digits.'

### The number 123459 has odd digits 1, 3, 5, and 9, and their product is 135
assert digits(123459) == 135, 'Failed to find the product of odd digits.'

### The number 2468 has no odd digits, so the function should return 0
assert digits(2468) == 0, 'Failed to handle case where all digits are even.'

## Edge Cases
### The number 0 has no odd digits, so the function should return 0
assert digits(0) == 0, 'Failed to handle case where input is 0.'

### The number 1 has only one digit, which is odd, so the function should return 1
assert digits(1) == 1, 'Failed to handle case where input has only one odd digit.'

### The number 2 has only one digit, which is even, so the function should return 0
assert digits(2) == 0, 'Failed to handle case where input has only one even digit.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The number 1 has only one digit, which is odd, so the function should return 1
assert digits(10**6) == 1, 'Failed to handle large input size.'

### The number 10^6 - 1 has all odd digits, so the function should return the product of all the digits, which is 9^6
assert digits(10**6 - 1) == 9**6, 'Failed to handle large input size with all odd digits.'

### The number 10^6 + 1 has both odd and even digits, so the function should return the product of the odd digits, which is 1
assert digits(10**6 + 1) == 1, 'Failed to handle large input size with odd and even digits.'

## Specific Quality Requirements
### Robustness
#### The input n is not a positive integer, so the function should handle the case not to raise error
assert not digits(-123), 'Failed to handle case where the input n is not a positive integer.'

#### The input n is not an integer, so the function should handle the case not to raise error
assert not digits('invalid'), 'Failed to handle case where the input n is not an integer.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(digits))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
