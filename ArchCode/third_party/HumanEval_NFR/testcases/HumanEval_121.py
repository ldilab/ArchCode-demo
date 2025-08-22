from solutions.HumanEval_121 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The odd elements at even positions are 5 and 7, so the sum is 12
assert solution([5, 8, 7, 1]) == 12, 'Failed to calculate the sum of odd elements in even positions.'

### The odd elements at even positions are 3, 3, and 3, so the sum is 9
assert solution([3, 3, 3, 3, 3]) == 9, 'Failed to calculate the sum of odd elements in even positions.'

### There are no odd elements at even positions, so the sum is 0
assert solution([30, 13, 24, 321]) == 0, 'Failed to handle case where there are no odd elements in even positions.'

### All elements in the input list are odd numbers,
### so the function should return 15
assert solution([1, 3, 5, 7, 9]) == 15, 'Failed to handle case where all elements in the list are odd numbers in even positions.'

### All elements in the input list are even numbers,
### so the function should return 0 since there are no odd elements in even positions
assert solution([2, 4, 6, 8]) == 0, 'Failed to handle case where all elements in the list are even numbers.'

## Edge Cases
### The input list is empty, so the function should return 0
assert solution([]) == 0, 'Failed to handle an empty input list.'

### The input list contains one odd integer, so the function should return it
assert solution([-9]) == -9, 'Failed to handle a length-1 input list.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input list contains 10^5 elements with alternating odd and even numbers,
### so the sum of odd elements in even positions is (1 + 3 + 5 + ... + (10^6 - 1)) = (5 * 10^5)^2
assert solution(list(range(1, 10**6))) == 25 * 10**10, 'Failed to handle large input size.'

### The input list contains 10^6 elements, all of which are odd numbers,
### so the sum of odd elements in even positions is (1 + 3 + 5 + ... + 2 * 10^6 - 1) = 10^12
assert solution([1] * 10**6) == 5 * 10**5, 'Failed to handle case where all elements in the list are the same odd number.'

### The input list contains 2 * 10^5 elements with alternating even and odd numbers,
### so there are no odd elements in even positions and the sum should be 0
assert solution([2, 1] * 10**5) == 0, 'Failed to handle case where all elements in the list are the same even number.'

## Specific Quality Requirements
### Robustness
#### The input is not a list, so the function should handle the case not to raise error
assert not solution('invalid'), 'Failed to handle case where the input is not a list.'

#### The input list contains elements that are not integers, so the function should handle the case not to raise error
assert not solution([1, 2, 'invalid', 4]), 'Failed to handle case where the input list contains elements that are not integers.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 10
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(solution))
assert result.total_complexity <= 10, 'Failed to have a Cyclomatic Complexity less than or equal to 10 by Radon.'