from solutions.HumanEval_81 import *
# Test Cases Regarding Functional Requirements
## General Cases
### Convert each GPA to its corresponding letter grade based on the table
### The input list contains GPAs [4.0, 3, 1.7, 2, 3.5]
### The expected output is ['A+', 'B', 'C-', 'C', 'A-']
assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-'], 'Failed to convert GPAs to letter grades.'

## Edge Cases
### The input list is empty, so the function should return an empty list
assert numerical_letter_grade([]) == [], 'Failed to handle an empty input list.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The grades list contains 10^6 elements, all of which are 4.0
### The expected output is a list of 10^6 'A+' grades
assert numerical_letter_grade([4.0] * 10**6) == ['A+'] * 10**6, 'Failed to handle large input size.'

### The grades list contains 10^6 elements, all of which are 2.0
### The expected output is a list of 10^6 'C+' grades
assert numerical_letter_grade([2.1] * 10**6) == ['C+'] * 10**6, 'Failed to handle large input size.'

### The grades list contains 10^6 elements, all of which are 0.0
### The expected output is a list of 10^6 'E' grades
assert numerical_letter_grade([0.0] * 10**6) == ['E'] * 10**6, 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The grades input is not a list, so the function should return an empty list
assert not numerical_letter_grade('invalid'), 'Failed to handle case where the input grades is not a list.'

#### The input list contains negative GPAs, so the function should handle the case not to raise error
assert not numerical_letter_grade([4.0, 3, -1.7, 2, 3.5]), 'Failed to handle negative GPAs in the input list.'

#### The grades list contains elements that are not numbers, so the function should handle the case not to raise error
assert numerical_letter_grade([4.0, 3, 'invalid', 2, 3.5]) == [], 'Failed to handle case where the input list contains elements that are not numbers.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 10
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(numerical_letter_grade))
assert result.total_complexity <= 10, 'Failed to have a Cyclomatic Complexity less than or equal to 10 by Radon.'