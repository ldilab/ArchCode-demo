from solutions.HumanEval_25 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The prime factorization of 8 is 2 * 2 * 2
assert factorize(8) == [2, 2, 2], 'Failed to factorize number correctly.'

### The prime factorization of 25 is 5 * 5
assert factorize(25) == [5, 5], 'Failed to factorize number correctly.'

### The prime factorization of 70 is 2 * 5 * 7
assert factorize(70) == [2, 5, 7], 'Failed to factorize number correctly.'

## Edge Cases
### The input number is 0, so the function should return an empty list
assert factorize(0) == [], 'Failed to handle the case where the input number is 0.'

### The input number is 1, so the function should return an empty list
assert factorize(1) == [], 'Failed to handle the case where the input number is 1.'

### The input number is a prime number, so the function should return a list with a single element equal to the input number
assert factorize(13) == [13], 'Failed to handle the case where the input number is a prime number.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input number is 10^12, which is a product of 2^12 and 5^12
assert factorize(10**12) == [2] * 12 + [5] * 12, 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The input number is not an integer, so the function should handle the case not to raise error
assert not factorize('invalid'), 'Failed to handle case where the input number is not an integer.'

#### The input number is negative, so the function should handle the case not to raise error
assert not factorize(-10), 'Failed to handle case where the input number is negative.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(factorize))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
