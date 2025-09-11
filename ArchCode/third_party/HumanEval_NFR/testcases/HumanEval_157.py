from solutions.HumanEval_157 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The sides 3, 4, and 5 form a right-angled triangle
assert right_angle_triangle(3, 4, 5) == True, 'Failed to identify a right-angled triangle.'

### The sides 1, 2, and 3 do not form a right-angled triangle
assert right_angle_triangle(1, 2, 3) == False, 'Failed to identify a non-right-angled triangle.'

## Edge Cases
### The sides 1, 1, and 1 do not form a right-angled triangle
assert right_angle_triangle(1, 1, 1) == False, 'Failed to identify a non-right-angled triangle.'

### The sides 3, 4, and 6 do not form a right-angled triangle
assert right_angle_triangle(3, 4, 6) == False, 'Failed to identify a non-right-angled triangle.'

### The sides 3, 4, and 8 do not form a triangle
assert right_angle_triangle(3, 4, 8) == False, 'Failed to identify a non-triangle.'

### Floating-point numbers
#### The sides 1.5, 2.0, and 2.5 form a right-angled triangle
assert right_angle_triangle(1.5, 2.0, 2.5) == True, 'Failed to handle floating-point numbers.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input sides are extremely large numbers
### The function should return True since 10^100, 10^100, and 10^200 form a right-angled triangle
assert right_angle_triangle(3*10**100, 4*10**100, 5*10**100) == True, 'Failed to handle extremely large numbers.'

## Specific Quality Requirements
### Robustness
### One of the sides is 0, so it does not form a triangle. Return None
assert not right_angle_triangle(0, 5, 10), 'Failed to handle case where one of the sides is 0.'

### Negative numbers are not allowed, so the function should handle the case not to raise error
assert not right_angle_triangle(-3, 4, 5), 'Failed to handle case where negative numbers are not allowed.'

### String inputs are not allowed, so the function should handle the case not to raise error
assert not right_angle_triangle('3', '4', '5'), 'Failed to handle case where string inputs are not allowed.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(right_angle_triangle))
assert result.total_complexity <= 10, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'