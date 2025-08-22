from solutions.HumanEval_77 import *
# Test Cases Regarding Functional Requirements
## General Cases
### 2 is not a cube of any integer
assert iscube(2) == False, 'Failed to identify that 2 is not a cube.'

### -1 is a cube of -1
assert iscube(-1) == True, 'Failed to identify that -1 is a cube.'

### 64 is a cube of 4
assert iscube(64) == True, 'Failed to identify that 64 is a cube.'

### The input is a negative cube, -8 is a cube of -2
assert iscube(-8) == True, 'Failed to identify a negative input as a cube.'

### 180 is not a cube of any integer
assert iscube(180) == False, 'Failed to identify that 180 is not a cube.'

## Edge Cases
### The input is a very small cube, 1 is a cube of 1
assert iscube(1) == True, 'Failed to identify a very small input as a cube.'

### 0 is a cube of 0
assert iscube(0) == True, 'Failed to identify that 0 is a cube.'


# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### Test a large input value
### The input is a very large integer, 999999999999 is not a cube of any integer
assert iscube(999999999999) == False, 'Failed to handle a large input value.'

### The input is a very large cube, 1000000000000 is a cube of 10000
assert iscube(1000000000000) == True, 'Failed to identify a very large input as a cube.'


## Specific Quality Requirements
### Robustness
#### The input is not an integer, so the function should handle the case not to raise error
assert not iscube('invalid'), 'Failed to handle a non-integer input.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(iscube))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'