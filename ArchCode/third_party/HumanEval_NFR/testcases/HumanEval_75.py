from solutions.HumanEval_75 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The input number is 30, which can be expressed as the product of 2, 3, and 5
### The function should return True
assert is_multiply_prime(30) == True, 'Failed to detect a number that is the product of 3 prime numbers.'

### The input number is 15, which cannot be expressed as the product of 3 prime numbers
### The function should return False
assert is_multiply_prime(15) == False, 'Failed to detect a number that is not the product of 3 prime numbers.'

### The input number is 99, which is 3 * 3 * 11
### The function should return True
assert is_multiply_prime(99) == True, 'Failed to handle case where the input number is the product of 3 prime numbers.'

### The input number is 100, which is 2 * 2 * 5 * 5
### The function should return False
assert is_multiply_prime(100) == False, 'Failed to detect a number that is not the product of 3 prime numbers.'

### The input number is 53, which is a prime number
### The function should return False since the input number is not the product of 3 prime numbers
assert is_multiply_prime(53) == False, 'Failed to handle case where the input number is a prime number.'

## Edge Cases
### The input number is 1, which is not considered a prime number
### The function should return False
assert is_multiply_prime(1) == False, 'Failed to handle case where the input number is 1.'

### The input number is 2, which is a prime number
### The function should return False since the input number is not the product of 3 prime numbers
assert is_multiply_prime(2) == False, 'Failed to handle case where the input number is a prime number.'

### The input number is 6, which is too small to be a product of 3 prime numbers
### The function should return False
assert is_multiply_prime(6) == False, 'Failed to handle case where the input number is small.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input number is 97, which is a prime number
### The function should return False since the input number is not the product of 3 prime numbers
assert is_multiply_prime(97) == False, 'Failed to handle case where the input number is a prime number.'

### The input number is 95 = 5 * 19, which is not the product of 3 prime numbers
### The function should return False
assert is_multiply_prime(95) == False, 'Failed to handle large input size.'

### The input number is 64 = 2 * 2 * 2 * 2 * 2 * 2, which is the product of 6 primes
### The function should return False
assert is_multiply_prime(64) == False, 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The input is not an integer, so the function should return False
assert not is_multiply_prime('invalid'), 'Failed to handle case where the input is not an integer.'

#### The input is a negative number, so the function should return False
assert not is_multiply_prime(-10), 'Failed to handle case where the input is a negative number.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(is_multiply_prime))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'