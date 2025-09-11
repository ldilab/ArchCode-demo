from solutions.HumanEval_7 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The `strings` list is empty, so the function should return an empty list
assert filter_by_substring([], 'a') == [], 'Failed to handle an empty `strings` list.'

### The `strings` list contains strings 'abc', 'bacd', and 'array' that contain the `substring`
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array'], 'Failed to filter the `strings` list correctly.'

## Edge Cases
### The `strings` list is empty, so the function should return an empty list
assert filter_by_substring([], 'abc') == [], 'Failed to handle an empty `strings` list.'

### None of the strings in the `strings` list contain the `substring`, so the function should return an empty list
assert filter_by_substring(['def', 'xyz', '123'], 'abc') == [], 'Failed to handle case where no string in `strings` contains the `substring`.'

### The `strings` list contains multiple strings that contain the `substring` with the same frequency
### The function should return any of the strings
assert filter_by_substring(['abc', 'bac', 'cab'], 'a') == ['abc', 'bac', 'cab'], 'Failed to return any of the strings containing the `substring`.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The `strings` list contains 10^4 strings, each with a length of 10^4, and all the strings contain the `substring`
### The function should return the entire `strings` list
assert filter_by_substring(['a' * 10**4] * 10**4, 'a') == ['a' * 10**4] * 10**4, 'Failed to handle large input size.'

### The `strings` list contains 10^4 strings, each with a length of 10^4, and none of the strings contain the `substring`
### The function should return an empty list
assert filter_by_substring(['b' * 10**4] * 10**4, 'a') == [], 'Failed to handle case where no string in `strings` contains the `substring`.'

## Specific Quality Requirements
### Robustness
#### The `strings` input is not a list of strings, so the function should return an empty list
assert not filter_by_substring('invalid', 'a'), 'Failed to handle case where the input `strings` is not a list of strings.'

#### The `substring` input is not a string, so the function should return an empty list
assert not filter_by_substring(['abc', 'bacd', 'cde', 'array'], 123), 'Failed to handle case where the input `substring` is not a string.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(filter_by_substring))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
