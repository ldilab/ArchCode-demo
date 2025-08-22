from solutions.HumanEval_12 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The input list is empty, so the function should handle the case not to raise error
assert not longest([]), 'Failed to handle an empty input list.'

### The longest string is 'a'
assert longest(['a', 'b', 'c']) == 'a', 'Failed to find the longest string.'

### Multiple strings have the same longest length, 'ccc'
### The function should return the first occurrence, which is 'ccc'
assert longest(['a', 'bb', 'ccc']) == 'ccc', 'Failed to return the first occurrence of the longest string.'

## Edge Cases
### The input list is empty, so the function should handle the case not to raise error
assert not longest([]), 'Failed to handle an empty input list.'

### The input list contains only one string, 'abc'
### The function should return 'abc' as the longest string
assert longest(['abc']) == 'abc', 'Failed to handle case where the input list contains only one string.'

### Multiple strings have the same longest length, 'abc'
### The function should return the first occurrence, which is 'abc'
assert longest(['abc', 'def', 'abc']) == 'abc', 'Failed to return the first occurrence of the longest string.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The strings list contains 10^6 strings, each with 10^4 characters
### The longest string is 'x' with 10^4 characters
assert longest(['x' * 10**4] * 10**6) == 'x' * 10**4, 'Failed to handle large input size.'

### The strings list contains 10^4 strings, each with 1 character
### The longest string is 'x' with 1 character
assert longest(['x'] * 10**4) == 'x', 'Failed to handle case where all strings have the same length.'

### The strings list contains 10^4 strings, each with increasing lengths from 1 to 10^6
### The longest string is 'x' with 10^4 characters
assert longest(['x' * n for n in range(1, 10**4 + 1)]) == 'x' * 10**4, 'Failed to handle case where the longest string has maximum length.'

## Specific Quality Requirements
### Robustness
#### The strings input is not a list, so the function should handle the case not to raise error
assert not longest('invalid'), 'Failed to handle case where the input strings is not a list.'

#### The strings list contains elements that are not strings, so the function should handle the case not to raise error
assert not longest(['a', 123, 'c']), 'Failed to handle case where the input list contains elements that are not strings.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(longest))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
