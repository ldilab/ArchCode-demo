from solutions.HumanEval_92 import *
# Test Cases Regarding Functional Requirements
## General Cases
### 5 is equal to the sum of 2 and 7, and all numbers are integers, so the function should return True
assert any_int(5, 2, 7) == True, 'Failed for the case where one number is equal to the sum of the other two.'

### None of the numbers are equal to the sum of the other two, so the function should return False
assert any_int(3, 2, 2) == False, 'Failed for the case where none of the numbers are equal to the sum of the other two.'

### -2 is equal to the sum of 3 and 1, and all numbers are integers, so the function should return True
assert any_int(3, -2, 1) == True, 'Failed for the case where one number is equal to the sum of the other two with negative numbers.'

### None of the numbers are equal to the sum of the other two, so the function should return False
assert any_int(-1, -2, -4) == False, 'Failed for the case where none of the numbers are equal to the sum of the other two.'

## Edge Cases
### All numbers are the same, but the function should return True in this case (0 + 0 = 0)
assert any_int(0, 0, 0) == True, 'Failed for the case where all numbers are the same.'

### None of the numbers are equal to the sum of the other two, so the function should return False
assert any_int(10**20, 10**20, 10**20) == False, 'Failed for the case where all numbers are the same.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### Satisfied if no errors occur across all test cases

## Specific Quality Requirements
### Robustness
#### The inputs are not numbers, so the function should handle the case not to raise error
assert not any_int('invalid', 1, 2), 'Failed to handle case where inputs are not numbers.'

#### The inputs are not integers, so the function should handle the case not to raise error
assert not any_int(1.5, 2.5, 4.0), 'Failed to handle case where inputs are not integers.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(any_int))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'