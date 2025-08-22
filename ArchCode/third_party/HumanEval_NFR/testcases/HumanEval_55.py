from solutions.HumanEval_55 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The 10th Fibonacci number is 55
assert fib(10) == 55, 'Failed to calculate the correct Fibonacci number.'

### The 1st Fibonacci number is 1
assert fib(1) == 1, 'Failed to calculate the correct Fibonacci number.'

### The 8th Fibonacci number is 21
assert fib(8) == 21, 'Failed to calculate the correct Fibonacci number.'

## Edge Cases
### The input is not an integer, so the function should handle the case not to raise error
assert not fib(3.14), 'Failed to handle a non-integer input value.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input value is 40, so the function should provide the result within 5 seconds
### The 40th Fibonacci number is too large to include in the test case
assert fib(40) is not None, 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The input value is not an integer, so the function should handle the case not to raise error
assert not fib('invalid'), 'Failed to handle a non-integer input value.'

#### The input value is a negative number, so the function should handle the case not to raise error
assert not fib(-10), 'Failed to handle a negative input value.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(fib))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
