from solutions.HumanEval_152 import *
# Test Cases Regarding Functional Requirements
## General Cases
### All guesses are correct, so the returned list should have all 0s
assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3], 'Failed to handle all correct guesses.'

### Some guesses are incorrect, so the returned list should have the absolute differences between the guesses and scores
assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6], 'Failed to handle incorrect guesses.'

## Edge Cases
### The input lists are empty but has same length, so the function should return an empty list
assert compare([], []) == [], 'Failed to handle empty input lists.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The `game` and `guess` lists contain 10^6 elements with increasing values from 1 to 10^6
### The guesses are all correct, so the function should return a list of 10^6 zeros
assert compare(list(range(1, 10**6 + 1)), list(range(1, 10**6 + 1))) == [0] * 10**6, 'Failed to handle large input size with all correct guesses.'

## Specific Quality Requirements
### Robustness
### The lengths of the `game` and `guess` lists are different, so the function should handle the case not to raise error
assert not compare([1, 2, 3, 4, 5], [1, 2, 3, 4]), 'Failed to handle lists with different lengths.'

#### The `game` input is not a list, so the function should handle the case not to raise error
assert not compare('invalid', [1, 2, 3, 4, 5]), 'Failed to handle case where the input game is not a list.'

#### The `guess` input is not a list, so the function should handle the case not to raise error
assert not compare([1, 2, 3, 4, 5], 'invalid'), 'Failed to handle case where the input guess is not a list.'

#### The `game` list contains elements that are not integers, so the function should handle the case not to raise error
assert not compare([1, 2, 'invalid', 4, 5], [1, 2, 3, 4, 5]), 'Failed to handle case where the input list contains elements that are not integers.'

#### The `guess` list contains elements that are not integers, so the function should handle the case not to raise error
assert not compare([1, 2, 3, 4, 5], [1, 2, 'invalid', 4, 5]), 'Failed to handle case where the input list contains elements that are not integers.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 10
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(compare))
assert result.total_complexity <= 10, 'Failed to have a Cyclomatic Complexity less than or equal to 10 by Radon.'