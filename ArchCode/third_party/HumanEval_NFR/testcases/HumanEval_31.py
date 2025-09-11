from solutions.HumanEval_31 import *
# Test Cases Regarding Functional Requirements
## General Cases
### 6 is not a prime number, so the function should return False
assert is_prime(6) == False, 'Failed to identify a non-prime number.'

### 101 is a prime number, so the function should return True
assert is_prime(101) == True, 'Failed to identify a prime number.'

### 11 is a prime number, so the function should return True
assert is_prime(11) == True, 'Failed to identify a prime number.'

### 13441 is a prime number, so the function should return True
assert is_prime(13441) == True, 'Failed to identify a prime number.'

### 61 is a prime number, so the function should return True
assert is_prime(61) == True, 'Failed to identify a prime number.'

### 4 is not a prime number, so the function should return False
assert is_prime(4) == False, 'Failed to identify a non-prime number.'

### 1 is not a prime number, so the function should return False
assert is_prime(1) == False, 'Failed to identify a non-prime number.'

## Edge Cases
### -1 is not a prime number, so the function should return False
assert is_prime(-1) == False, 'Failed to handle negative numbers.'

### 0 is not a prime number, so the function should return False
assert is_prime(0) == False, 'Failed to handle the case where n is 0.'

### 2 is a prime number, so the function should return True
assert is_prime(2) == True, 'Failed to handle the smallest prime number.'

### 3 is a prime number, so the function should return True
assert is_prime(3) == True, 'Failed to handle the smallest odd prime number.'

### 97 is a prime number, so the function should return True
assert is_prime(97) == True, 'Failed to handle a prime number with only 2 factors.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input number is 9999991, which is a prime number
assert is_prime(9999991) == True, 'Failed to handle a large prime number.'

## The input number is 9999990, which is not a prime number
assert is_prime(9999990) == False, 'Failed to handle a large non-prime number.'

## Specific Quality Requirements
### Robustness
#### The input is not an integer, so the function should handle the case not to raise error
assert not is_prime('invalid'), 'Failed to handle case where the input is not an integer.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(is_prime))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
