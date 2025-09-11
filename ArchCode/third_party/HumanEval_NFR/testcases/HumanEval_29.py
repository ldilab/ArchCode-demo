from solutions.HumanEval_29 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The input list is empty, so the function should return an empty list
assert filter_by_prefix([], 'a') == [], 'Failed to handle an empty input list.'

### The input list contains strings that start with the given prefix, so the function should return those strings in a list
assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array'], 'Failed to filter strings with the given prefix.'

## Edge Cases
### The input list contains strings that do not start with the given prefix, so the function should return an empty list
assert filter_by_prefix(['bcd', 'cde', 'def', 'efg'], 'a') == [], 'Failed to handle case where no strings start with the given prefix.'

### The input list contains strings that all have the same prefix, so the function should return the entire input list
assert filter_by_prefix(['abc', 'abcd', 'abcde', 'abcdef'], 'abc') == ['abc', 'abcd', 'abcde', 'abcdef'], 'Failed to handle case where all strings have the same prefix.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input list contains 10^6 strings, all of which start with the given prefix
### The function should return the entire input list
assert filter_by_prefix(['a' + str(i) for i in range(10**6)], 'a') == ['a' + str(i) for i in range(10**6)], 'Failed to handle large input size.'

### The input list contains 10^6 strings, none of which start with the given prefix
### The function should return an empty list
assert filter_by_prefix(['b' + str(i) for i in range(10**6)], 'a') == [], 'Failed to handle large input size where no strings start with the given prefix.'

### The input list contains 10^6 strings, all of which are empty strings
### The function should return an empty list
assert filter_by_prefix([''] * 10**6, 'a') == [], 'Failed to handle case where all strings are empty strings.'

## Specific Quality Requirements
### Robustness
#### The strings input is not a list, so the function should handle the case not to raise error
assert not filter_by_prefix('invalid', 'a'), 'Failed to handle case where the input strings is not a list.'

#### The prefix input is not a string, so the function should handle the case not to raise error
assert not filter_by_prefix(['abc', 'def', 'ghi'], 123), 'Failed to handle case where the input prefix is not a string.'

#### The strings list contains an element that is not a string, so the function should handle the case not to raise error
assert not filter_by_prefix(['abc', 123, 'def'], 'a'), 'Failed to handle case where the input list contains elements that are not strings.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(filter_by_prefix))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
