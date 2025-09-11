from solutions.HumanEval_97 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The unit digits of 148 and 412 are 8 and 2 respectively, and their product is 16
assert multiply(148, 412) == 16, 'Failed to multiply the unit digits correctly.'

### The unit digits of 19 and 28 are 9 and 8 respectively, and their product is 72
assert multiply(19, 28) == 72, 'Failed to multiply the unit digits correctly.'

### The unit digits of 2020 and 1851 are 0 and 1 respectively, and their product is 0
assert multiply(2020, 1851) == 0, 'Failed to multiply the unit digits correctly.'

### The unit digits of 14 and -15 are 4 and 5 respectively, and their product is 20
assert multiply(14, -15) == 20, 'Failed to multiply the unit digits correctly.'

## Edge Cases
### The unit digits of 0 and 0 are both 0, and their product is 0
assert multiply(0, 0) == 0, 'Failed to handle case where both inputs are 0.'

### The unit digits of 10 and 10 are both 0, and their product is 0
assert multiply(10, 10) == 0, 'Failed to handle case where both inputs are 0.'

### The unit digits of 1234567890 and 9876543210 are 0 and 0 respectively, and their product is 0
assert multiply(1234567890, 9876543210) == 0, 'Failed to handle case where both inputs have all digits as 0.'

### The unit digits of 10**6 and 10**6 are 0 and 0 respectively, and their product is 0
assert multiply(10**6, 10**6) == 0, 'Failed to handle case where both inputs are large numbers with all digits as 0.'

### The unit digits of -14 and 13 are 4 and 3 respectively, and their product is 12
assert multiply(-14, 13) == 12, 'Failed to handle case where one of the inputs is negative.'

### The unit digits of -987654 and -1234567 are 4 and 7 respectively, and their product is 28
assert multiply(-987654, -1234567) == 28, 'Failed to handle case where both of the inputs are negative.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The inputs are large numbers with multiple digits
### The function should return the product of the unit digits quickly
assert multiply(987654321098765432109876543210987654321098765432109876543210987654321, 123456789012345678901234567890123456789012345678901234567890123456789) == 9, 'Failed to handle large input size.'

### The inputs are large numbers with multiple digits
### The function should return the product of the unit digits quickly
assert multiply(12345678912345678, 98765432109876543) == 24, 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The inputs are not integers, so the function should raise a TypeError
assert not multiply('invalid', 'invalid'), 'Failed to handle case where the inputs are not integers.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(multiply))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'