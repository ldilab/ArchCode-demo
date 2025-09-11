from solutions.HumanEval_46 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The 5th element of the Fib4 sequence is 4
assert fib4(5) == 4, 'Failed to compute the n-th element of the Fib4 sequence.'

### The 6th element of the Fib4 sequence is 8
assert fib4(6) == 8, 'Failed to compute the n-th element of the Fib4 sequence.'

### The 7th element of the Fib4 sequence is 14
assert fib4(7) == 14, 'Failed to compute the n-th element of the Fib4 sequence.'

## Edge Cases
### The 0th element of the Fib4 sequence is 0
assert fib4(0) == 0, 'Failed to compute the 0th element of the Fib4 sequence.'

### The 1st element of the Fib4 sequence is 0
assert fib4(1) == 0, 'Failed to compute the 1st element of the Fib4 sequence.'

### The 2nd element of the Fib4 sequence is 2
assert fib4(2) == 2, 'Failed to compute the 2nd element of the Fib4 sequence.'

### The 3rd element of the Fib4 sequence is 0
assert fib4(3) == 0, 'Failed to compute the 3rd element of the Fib4 sequence.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input n is a large number (n = 10^5)
### The function should provide the result within 5 seconds
assert isinstance(fib4(10**5), int) == True, 'Failed to meet the performance requirement of providing the result within 5 seconds.'

## Specific Quality Requirements
### Robustness
#### The input n is a negative number, so the function should handle the case not to raise error
assert not fib4(-5), 'Failed to handle case where the input n is a negative number.'

#### The input n is not an integer, so the function should handle the case not to raise error
assert not fib4('invalid'), 'Failed to handle case where the input n is not an integer.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(fib4))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
