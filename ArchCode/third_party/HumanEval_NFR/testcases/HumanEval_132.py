from solutions.HumanEval_132 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The string '[[]]' contains a valid subsequence of brackets where at least one bracket is nested
assert is_nested('[[]]') == True, 'Failed to identify a nested bracket in a valid subsequence.'

### The string '[]]]]]]][[[[[]' does not contain a valid subsequence of brackets where at least one bracket is nested
assert is_nested('[]]]]]]][[[[[]') == False, 'Failed to identify absence of a nested bracket in any valid subsequence.'

### The string '[][]' does not contain a valid subsequence of brackets where at least one bracket is nested
assert is_nested('[][]') == False, 'Failed to identify absence of a nested bracket in any valid subsequence.'

### The string '[]' does not contain a valid subsequence of brackets where at least one bracket is nested
assert is_nested('[]') == False, 'Failed to identify absence of a nested bracket in any valid subsequence.'

### The string '[[][]]' contains a valid subsequence of brackets where at least one bracket is nested
assert is_nested('[[][]]') == True, 'Failed to identify a nested bracket in a valid subsequence.'

### The string '[[]][[' contains a valid subsequence of brackets where at least one bracket is nested
assert is_nested('[[]][[') == True, 'Failed to identify a nested bracket in a valid subsequence.'

## Edge Cases
### The input string is empty, so the function should return False
assert is_nested('') == False, 'Failed to handle an empty input string.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input string contains 10^6 opening brackets followed by 10^6 closing brackets
### None of the brackets are nested, so the function should return True
assert is_nested('['*10**6 + ']'*10**6) == True, 'Failed to handle large input size.'

### The input string contains 10^6 nested brackets, where each nested sequence is surrounded by a pair of brackets
### At least one bracket is nested, so the function should return True
assert is_nested('[[]]'*10**6) == True, 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The input is not a string, so the function should handle the case not to raise error
assert not is_nested(123), 'Failed to handle case where the input is not a string.'

### The input string contains characters other than square brackets, so the function should handle the case not to raise error
assert not is_nested('[[]]]a]]][[[[[]'), 'Failed to handle case where the input string contains characters other than square brackets.'


### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 10
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(is_nested))
assert result.total_complexity <= 10, 'Failed to have a Cyclomatic Complexity less than or equal to 10 by Radon.'
