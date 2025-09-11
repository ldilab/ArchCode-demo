from solutions.HumanEval_14 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The input string is 'abc', so the function should return ['a', 'ab', 'abc']
assert all_prefixes('abc') == ['a', 'ab', 'abc'], 'Failed to return all prefixes of the input string.'

### The input string is 'hello', so the function should return ['h', 'he', 'hel', 'hell', 'hello']
assert all_prefixes('hello') == ['h', 'he', 'hel', 'hell', 'hello'], 'Failed to return all prefixes of the input string.'

## Edge Cases
### The input string is empty, so the function should return an empty list
assert all_prefixes('') == [], 'Failed to handle an empty input string.'

### The input string is 'a', so the function should return ['a']
assert all_prefixes('a') == ['a'], 'Failed to handle a single-character input string.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input string has 10^4 characters, all of which are 'a'
### The function should return a list containing 10^6 elements, each being 'a'
assert all_prefixes('a' * 10**4) == ['a' * i for i in range(1, 10 ** 4 + 1)], 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The input is not a string, so the function should return an empty list
assert not all_prefixes(123), 'Failed to handle a non-string input.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(all_prefixes))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
