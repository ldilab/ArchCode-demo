from solutions.HumanEval_13 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The GCD of 3 and 5 is 1
assert greatest_common_divisor(3, 5) == 1, 'Failed to calculate the GCD.'

### The GCD of 25 and 15 is 5
assert greatest_common_divisor(25, 15) == 5, 'Failed to calculate the GCD.'

## Edge Cases
### One input is zero, so the GCD should be the non-zero input
assert greatest_common_divisor(0, 5) == 5, 'Failed to handle case where one input is zero.'

### Both inputs are zero, so the GCD should be zero
assert greatest_common_divisor(0, 0) == 0, 'Failed to handle case where both inputs are zero.'

### Both inputs are negative, so the GCD should be positive
# assert greatest_common_divisor(-6, -9) == 3, 'Failed to handle case where both inputs are negative.'

### One input is negative and the other is positive, so the GCD should be positive
assert greatest_common_divisor(-6, 9) == 3, 'Failed to handle case where one input is negative.'

### Both inputs are the same, so the GCD should be the value of the inputs
assert greatest_common_divisor(5, 5) == 5, 'Failed to handle case where the inputs are the same.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The inputs are extremely large prime numbers, so the GCD should be 1
assert greatest_common_divisor(999999999989, 999999999937) == 1, 'Failed to handle large prime numbers.'

### The inputs are extremely large non-prime numbers with a common factor of 100
### The GCD should be 100
assert greatest_common_divisor(100000000100, 100000000200) == 100, 'Failed to handle large non-prime numbers with a common factor.'

## Specific Quality Requirements
### Robustness
#### The inputs are not integers, so the function should handle the case not to raise error
assert not greatest_common_divisor('invalid', 5), 'Failed to handle when the inputs are not integers.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(greatest_common_divisor))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
