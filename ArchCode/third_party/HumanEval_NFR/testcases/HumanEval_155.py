from solutions.HumanEval_155 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The input number has 1 even digit (2) and 1 odd digit (1)
assert even_odd_count(-12) == (1, 1), 'Failed to count even and odd digits correctly.'

### The input number has 1 even digit (2) and 2 odd digits (1, 3)
assert even_odd_count(123) == (1, 2), 'Failed to count even and odd digits correctly.'

## Edge Cases
### The input number is 0, which has one even digit (0) and no odd digits
assert even_odd_count(0) == (1, 0), 'Failed to handle input number of 0.'

### The input number is a single even digit (4)
assert even_odd_count(4) == (1, 0), 'Failed to handle input number with a single even digit.'

### The input number is a single odd digit (9)
assert even_odd_count(9) == (0, 1), 'Failed to handle input number with a single odd digit.'

### The input number has all even digits (2468)
assert even_odd_count(2468) == (4, 0), 'Failed to handle input number with all even digits.'

### The input number has all odd digits (13579)
assert even_odd_count(13579) == (0, 5), 'Failed to handle input number with all odd digits.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input number is a large positive even number (10^6)
assert even_odd_count(10**6) == (6, 1), 'Failed to handle large input number.'

### The input number is a large negative odd number (-10^9 + 1)
assert even_odd_count(-10**9 + 1) == (0, 9), 'Failed to handle large negative input number.'

## Specific Quality Requirements
### Robustness
#### The num input is not an integer, so the function should handle the case not to raise error
assert not even_odd_count('invalid'), 'Failed to handle case where the num input is not an integer.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(even_odd_count))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'