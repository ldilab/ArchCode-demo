from solutions.HumanEval_49 import *
# Test Cases Regarding Functional Requirements
## General Cases
### 2^3 modulo 5 is 3
assert modp(3, 5) == 3, 'Failed to calculate 2^n modulo p correctly.'

### 2^1101 modulo 101 is 2
assert modp(1101, 101) == 2, 'Failed to calculate 2^n modulo p correctly.'

### 2^0 modulo 101 is 1
assert modp(0, 101) == 1, 'Failed to calculate 2^n modulo p correctly.'

### 2^3 modulo 11 is 8
assert modp(3, 11) == 8, 'Failed to calculate 2^n modulo p correctly.'

### 2^100 modulo 101 is 1
assert modp(100, 101) == 1, 'Failed to calculate 2^n modulo p correctly.'

## Edge Cases
### 2^-3 modulo 5 is 1
### The function should handle negative values of n and p
assert modp(-3, 5) == 1, 'Failed to handle negative values of n and p.'

### 2^0 modulo 0 is not defined
### The function should handle the case where p is zero and handle the case not to raise error
assert not modp(0, 0), 'Failed to handle the case where p is zero.'

### 2^0 modulo 1 is 1
### The function should handle the case where p is one
assert modp(0, 1) == 1, 'Failed to handle the case where p is one.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The function should provide results within 5 seconds for large inputs
### 2^1000000 modulo 10^9 is 73741817
### The function should handle large values of n and p
assert modp(1000000, 10**9) == 747109376, 'Failed to handle large values of n and p.'

## Specific Quality Requirements
### Robustness
#### The input n is not an integer, so the function should handle the case not to raise error
assert not modp('invalid', 10), 'Failed to handle case where the input n is not an integer.'

#### The input p is not an integer, so the function should handle the case not to raise error
assert not modp(3, 'invalid'), 'Failed to handle case where the input p is not an integer.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(modp))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
