from solutions.HumanEval_76 import *
# Test Cases Regarding Functional Requirements
## General Cases
### 1 is a simple power of 4 since 4**0 = 1
assert is_simple_power(1, 4) == True, 'Failed for case where x is a simple power of n.'

### 2 is a simple power of 2 since 2**1 = 2
assert is_simple_power(2, 2) == True, 'Failed for case where x is a simple power of n.'

### 8 is a simple power of 2 since 2**3 = 8
assert is_simple_power(8, 2) == True, 'Failed for case where x is a simple power of n.'

### 3 is not a simple power of 2 since there is no integer `int` such that 2**int = 3
assert is_simple_power(3, 2) == False, 'Failed for case where x is not a simple power of n.'

### 3 is not a simple power of 1 since 1**int = 1, but 1 != 3
assert is_simple_power(3, 1) == False, 'Failed for case where x is not a simple power of n.'

### 2 is not a simple power of 8 since there is no integer `int` such that 8**int = 2
assert is_simple_power(2, 8) == False, 'Failed for case where x is not a simple power of n.'

## Edge Cases
### 1 is a simple power of 1 since 1**int = 1
assert is_simple_power(1, 1) == True, 'Failed for case where x is a simple power of n and n = 1.'

### 0 is not a simple power of any number other than 0
assert is_simple_power(0, 2) == False, 'Failed for case where x is 0 and n is not 0.'

### 2 is not a simple power of 0 since 0**n=0 for n other than 0
assert is_simple_power(2, 0) == False, 'Failed for case where n is 0 and x is not 0.'

### x and n are both negative
assert is_simple_power(-1, -1) == True, 'Failed to handle case where x is negative.'

### x and n are both negative
assert is_simple_power(-27, -3) == True, 'Failed to handle case where x is negative.'

### x is negative but n is positive
assert is_simple_power(-8, 2) == False, 'Failed to handle case where x is negative.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The larger of x and n is 10^6
### 10^6 is a simple power of 10 since 10**6 = 10^6
assert is_simple_power(10**6, 10) == True, 'Failed for large input size.'

### The larger of x and n is 10^6
### 10^6 is not a simple power of 3 since there is no integer `int` such that 3**int = 10^6
assert is_simple_power(10**6, 3) == False, 'Failed for large input size.'

### The larger of x and n is 10^6
### Any number is simple power of itself
assert is_simple_power(10**6, 10**6) == True, 'Failed for large input size.'

## Specific Quality Requirements
### Robustness
#### x is not an integer, so the function should handle the case not to raise error
assert not is_simple_power('invalid', 4), 'Failed to handle case where x is not an integer.'

#### n is not an integer, so the function should handle the case not to raise error
assert not is_simple_power(1, 'invalid'), 'Failed to handle case where n is not an integer.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(is_simple_power))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'