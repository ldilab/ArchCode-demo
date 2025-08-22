from solutions.HumanEval_50 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The input string is "fghij", so the decoded string should be "abcde"
assert decode_shift("fghij") == "abcde", 'Failed to decode the string correctly.'

## Edge Cases
### The input string is empty, so the decoded string should also be empty
assert decode_shift("") == "", 'Failed to handle an empty input string for decoding.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input string has length 10^6, all characters are "f"
### The decoded string should have length 10^6, all characters are "a"
assert decode_shift("f" * 10**6) == "a" * 10**6, 'Failed to handle large input size for decoding.'

## Specific Quality Requirements
### Robustness
#### The input string contains non-alphabetic characters and the target characters for shifting are "a" to "z"
#### The decoded string should have the non-alphabetic characters remain unchanged
assert decode_shift("fgh123!@#") == "abc123!@#", 'Failed to handle non-alphabetic characters in the input string for decoding.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(decode_shift))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 for decode_shift.'
