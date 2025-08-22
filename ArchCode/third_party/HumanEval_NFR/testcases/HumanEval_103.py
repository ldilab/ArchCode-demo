from solutions.HumanEval_103 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The average of the integers from 1 through 5 is 3, which is "0b11" in binary representation
assert rounded_avg(1, 5) == "0b11", 'Failed to compute the rounded average and convert it to binary.'

### n is greater than m, so the function should return -1
assert rounded_avg(7, 5) == -1, 'Failed to handle case where n is greater than m.'

### The average of the integers from 10 through 20 is 15, which is "0b1111" in binary representation
assert rounded_avg(10, 20) == "0b1111", 'Failed to compute the rounded average and convert it to binary.'

### The average of the integers from 20 through 33 is 26.5,
### which is "0b11010" in binary representation after rounding
assert rounded_avg(20, 33) == "0b11010", 'Failed to compute the rounded average and convert it to binary.'

## Edge Cases
### The average of the single integer 5 is 5, which is "0b101" in binary representation
assert rounded_avg(5, 5) == "0b101", 'Failed to handle case where n is equal to m.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The inputs are the maximum positive integers, so the function should return the result within a reasonable time
assert rounded_avg(10**9, 10**9) == "0b111011100110101100101000000000", 'Failed to handle large inputs within the required time.'

## Specific Quality Requirements
### Robustness
#### The n input is not a positive integer, so the function should handle the case not to raise error
assert not rounded_avg('invalid', 10), 'Failed to handle case where the input n is not a positive integer.'

#### The m input is not a positive integer, so the function should handle the case not to raise error
assert not rounded_avg(10, 'invalid'), 'Failed to handle case where the input m is not a positive integer.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(rounded_avg))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'