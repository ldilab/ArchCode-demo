from solutions.HumanEval_99 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The closest integer to 10 is 10
assert closest_integer("10") == 10, 'Failed to find the closest integer.'

### The closest integer to 15.3 is 15
assert closest_integer("15.3") == 15, 'Failed to find the closest integer.'

### The closest integer to -14.5 is -15
assert closest_integer("-14.5") == -15, 'Failed to handle case where the number is negative and equidistant from two integers.'

### The closest integer to 14.5000 is 15
assert closest_integer("14.5000") == 15, 'Failed to handle case where the number is positive and equidistant from two integers.'

## Edge Cases
### The input value is already an integer, so the function should return the same integer
assert closest_integer("100.0000000000000000000000000000") == 100, 'Failed to handle case where the input value is already an integer.'

### The closest integer to 1.49.....9 is 1
assert closest_integer("1.49999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999") == 1, 'Failed to handle case where the input value has many digits after the decimal point.'

### The closest integer to -0.49.....9 is 0
assert closest_integer("-0.49999999999999999999999999999999999999999999999999999999999") == 0, 'Failed to handle case where the input value is negative and has many digits after the decimal point.'

### The input value is large, so converting it to float may fail due to precision issue
assert closest_integer("99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999.5") == 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 'Failed to handle case where the input value is large' 

### The input value is large, so converting it to float may fail due to precision issue
assert closest_integer("99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999.000000000000000000000000000000000000000000000000000001") == 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999, 'Failed to handle case where the input value is large'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### Satisfied if the function executes in constant time and space for any input size and completes within 1 second.

## Specific Quality Requirements
### Robustness
#### The input value is not a string, so the function should handle the case not to raise error
assert not closest_integer(10), 'Failed to handle case where the input value is not a string.'

#### The input value is an empty string, so the function should handle the case not to raise error
assert not closest_integer(""), 'Failed to handle case where the input value is an empty string.'

#### The input value contains non-numeric characters, so the function should handle the case not to raise error
assert not closest_integer("15a.3"), 'Failed to handle case where the input value contains non-numeric characters.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(closest_integer))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'