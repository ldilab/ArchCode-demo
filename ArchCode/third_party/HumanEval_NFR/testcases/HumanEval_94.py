from solutions.HumanEval_94 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The largest prime in the list is 181, and the sum of its digits is 10
assert skjkasdkd([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]) == 10, 'Failed to find the largest prime and calculate the sum of its digits.'

### The largest prime in the list is 4597, and the sum of its digits is 25
assert skjkasdkd([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]) == 25, 'Failed to find the largest prime and calculate the sum of its digits.'

### The largest prime in the list is 5107, and the sum of its digits is 13
assert skjkasdkd([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]) == 13, 'Failed to find the largest prime and calculate the sum of its digits.'

### The largest prime in the list is 83, and the sum of its digits is 11
assert skjkasdkd([0,724,32,71,99,32,6,0,5,91,83,0,5,6]) == 11, 'Failed to find the largest prime and calculate the sum of its digits.'

### The largest prime in the list is 3, and the sum of its digits is 3
assert skjkasdkd([0,81,12,3,1,21]) == 3, 'Failed to find the largest prime and calculate the sum of its digits.'

### The largest prime in the list is 7, and the sum of its digits is 7
assert skjkasdkd([0,8,1,2,1,7]) == 7, 'Failed to find the largest prime and calculate the sum of its digits.'

## Edge Cases
### The length of the list is 1 and its only element is a prime number
assert skjkasdkd([2147483647]) == 46, 'Failed to handle a length-1 list containing a large prime number'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input list contains 10^6 + 1 elements
### The function should return 2 since it is the only prime number in the list
assert skjkasdkd([4] * 10**6 + [2]) == 2, 'Failed to handle large input size.'

### The input list contains 10^6 + 1 elements
### The largest prime in the list is 999983, and the sum of its digits is 47
assert skjkasdkd([2] * 10**6 + [999983]) == 47, 'Failed to handle large input size with all prime numbers.'

## Specific Quality Requirements
### Robustness
### The input list is empty, so the function should handle the case not to raise error
assert not skjkasdkd([]), 'Failed to handle an empty input list.'

### There are no prime numbers in the list, so the function should handle the case not to raise error
assert not skjkasdkd([4, 8, 12, 16, 20]), 'Failed to handle the case where there are no prime numbers in the list.'

#### The lst input is not a list of integers, so the function should handle the case not to raise error
assert not skjkasdkd('invalid'), 'Failed to handle case where the input lst is not a list of integers.'

#### The lst input contains elements that are not integers, so the function should handle the case not to raise error
assert not skjkasdkd([1, 2, 'invalid', 4]), 'Failed to handle case where the input list contains elements that are not integers.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 10
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(skjkasdkd))
assert result.total_complexity <= 10, 'Failed to have a Cyclomatic Complexity less than or equal to 10 by Radon.'