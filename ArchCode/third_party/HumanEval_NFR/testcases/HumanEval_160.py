from solutions.HumanEval_160 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The operator list contains '+' and '*', and the operand list is [2, 3, 4, 5]
### The expression built is: 2 + 3 * 4 - 5
### The expected result is 9
assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9, 'Failed to evaluate the algebraic expression correctly.'

### The operator list contains '-', '*', and '//', and the operand list is [1, 2, 3, 4, 5]
### The expression built is: 1 - 2 * 3 // 4 * 5
### The expected result is -4
assert do_algebra(['-', '*', '//', '*'], [1, 2, 3, 4, 5]) == -4, 'Failed to evaluate the algebraic expression correctly.'

## Edge Cases
### Priority of operators
#### The operator list contains '+', '-', '*', and '//', and the operand list is [1, 2, 3, 4, 5]
#### The expression built is: 1 + 2 - 3 * 4 // 5
#### The expected result is 0
assert do_algebra(['+', '-', '*', '//'], [1, 2, 3, 4, 5]) == 1, 'Failed to handle case where the priority of operators is not considered.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The operand list contains 10^6 elements, all of which are 1
### The operator list contains 10^6-1 '+' operators
### The expected result is 10^6
assert do_algebra(['+'] * (10**6 - 1), [1] * 10**6) == 10**6, 'Failed to handle large input size.'

### The operand list contains 10^6 elements, all of which are 1
### The operator list contains 10^6-1 '*' operators
### The expected result is 1
assert do_algebra(['*'] * (10**6 - 1), [1] * 10**6) == 1, 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
### The length of the operator list is not equal to the length of the operand list minus one, so the function should handle the case not to raise error
assert not do_algebra([], [2, 3, 4, 5]), 'Failed to handle an empty operator list.'

### The length of the operator list is not equal to the length of the operand list minus one, so the function should handle the case not to raise error
assert not do_algebra(['+'], [2]), 'Failed to handle case where the length of the operator list is not equal to the length of the operand list minus one.'

### The operator input is not a list, so the function should handle the case not to raise error
assert not do_algebra('+', [2, 3, 4, 5]), 'Failed to handle an operator input that is not a list.'

### The operand input is not a list, so the function should handle the case not to raise error
assert not do_algebra(['+', '*', '-'], 2), 'Failed to handle an operand input that is not a list.'

### The operand list contains an element that is not a non-negative integer, so the function should handle the case not to raise error
assert not do_algebra(['+', '*', '-'], [2, -3, 4, 5]), 'Failed to handle an operand list with an element that is not a non-negative integer.'

### The operator list contains an element that is not a string, so the function should handle the case not to raise error
assert not do_algebra(['+', 5, '-'], [2, 3, 4, 5]), 'Failed to handle an operator list with an element that is not a string.'

### The expression built involves division by zero, so the function should handle the case not to raise error
assert not do_algebra(['//'], [2, 0]), 'Failed to handle division by zero in the expression.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 10
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(do_algebra))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 10 by Radon.'