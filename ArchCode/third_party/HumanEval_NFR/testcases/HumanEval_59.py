from solutions.HumanEval_59 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The largest prime factor of 13195 is 29
assert largest_prime_factor(13195) == 29, 'Failed to find the largest prime factor.'

### The largest prime factor of 2048 is 2
assert largest_prime_factor(2048) == 2, 'Failed to find the largest prime factor.'

## Edge Cases
### The input is less than or equal to 1, so the function should handle the case not to raise error
assert not largest_prime_factor(1), 'Failed to handle the case not to raise error for n <= 1'

### The input is a prime number, so the function should handle the case not to raise error
assert not largest_prime_factor(17), 'Failed to handle the case not to raise error for prime n'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input is a large number, 10^8, which is not a prime
### The largest prime factor of 10^8 is 5, so the function should return 5
assert largest_prime_factor(10**8) == 5, 'Failed to handle large input size.'

### The input is a large prime number, 10^6 + 19
### The function should raise a ValueError since the input is a prime number
assert not largest_prime_factor(10**6 + 19), 'Failed to handle the case not to raise error for prime n'

## Specific Quality Requirements
### Robustness
#### The input is not an integer, so the function should handle the case not to raise error
assert not largest_prime_factor('invalid'), 'Failed to handle the case not to raise error for invalid input'

#### The input is a negative number, so the function should handle the case not to raise error
assert not largest_prime_factor(-10), 'Failed to handle the case not to raise error for negative n'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(largest_prime_factor))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
