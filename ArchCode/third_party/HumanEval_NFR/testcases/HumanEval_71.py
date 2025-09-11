from solutions.HumanEval_71 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The sides [3, 4, 5] form a valid triangle with an area of 6.00
assert triangle_area(3, 4, 5) == 6.00, 'Failed to calculate the area of a valid triangle.'

### The sides [1, 2, 10] do not form a valid triangle, so the function should return -1
assert triangle_area(1, 2, 10) == -1, 'Failed to handle case where the sides do not form a valid triangle.'

## Edge Cases
### The sides [0, 0, 0] do not form a valid triangle, so the function should return -1
assert triangle_area(0, 0, 0) == -1, 'Failed to handle case where the sides are all zero.'

### The sides [-1, -2, -3] do not form a valid triangle, so the function should return -1
assert triangle_area(-1, -2, -3) == -1, 'Failed to handle case where the sides are negative.'

### The sides [1, 1, 2] do not form a valid triangle, so the function should return -1
assert triangle_area(1, 1, 2) == -1, 'Failed to handle case where the sum of any two sides is equal to the third side.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The sides [10^5, 10^5, 10^5] form a valid triangle with an area of 4.330127018922193
assert triangle_area(10**5, 10**5, 10**5) == 4330127018.92, 'Failed to handle large input values.'

## Specific Quality Requirements
### Robustness
# Test case for handling "invalid" input as the first side
assert not triangle_area("invalid", 4, 5), "Failed to handle Invalid input."

# Test case for handling "invalid" input as the second side
assert not triangle_area(3, "invalid", 5), "Failed to handle Invalid input."

# Test case for handling "invalid" input as the third side
assert not triangle_area(3, 4, "invalid"), "Failed to handle Invalid input."

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(triangle_area))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
