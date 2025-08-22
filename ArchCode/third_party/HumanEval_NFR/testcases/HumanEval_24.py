from solutions.HumanEval_24 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The largest divisor of 15 that is smaller than 15 is 5
assert largest_divisor(15) == 5, 'Failed to find the largest divisor.'

### The largest divisor of 10 that is smaller than 10 is 5
assert largest_divisor(10) == 5, 'Failed to find the largest divisor.'

### The largest divisor of 16 that is smaller than 16 is 8
assert largest_divisor(16) == 8, 'Failed to find the largest divisor.'

### The largest divisor of 20 that is smaller than 20 is 10
assert largest_divisor(20) == 10, 'Failed to find the largest divisor.'

## Edge Cases
### The largest divisor of a prime number n that is smaller than n is 1
assert largest_divisor(2) == 1, 'Failed to find the largest divisor of a prime number.'

### The largest divisor of a prime number n that is smaller than n is 1
assert largest_divisor(3) == 1, 'Failed to find the largest divisor of a prime number.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input is a large prime number, so the function should return 1
assert largest_divisor(9999991) == 1, 'Failed to handle large input size.'

### The input is a large composite number, so the function should return the largest divisor that is smaller than the input
assert largest_divisor(9999989) == 44843, 'Failed to handle large input size.'


## Specific Quality Requirements
### Robustness
#### The input is a negative number, so the function should return -1
assert not largest_divisor(-5), 'Failed to handle negative input.'

#### There is no divisor smaller than 1 that divides 1 evenly, so the function should handle the case not to raise error
assert not largest_divisor(1), 'Failed to handle case where there is no divisor that meets the condition.'

#### The input is not an integer, so the function should handle the case not to raise error
assert not largest_divisor('invalid'), 'Failed to handle case where the input is not an integer.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(largest_divisor))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
