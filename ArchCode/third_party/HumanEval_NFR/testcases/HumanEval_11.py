from solutions.HumanEval_11 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The binary XOR of '010' and '110' is '100'
assert string_xor('010', '110') == '100', 'Failed to perform binary XOR operation correctly.'

### The binary XOR of '10101' and '01010' is '11111'
assert string_xor('10101', '01010') == '11111', 'Failed to perform binary XOR operation correctly.'

## Edge Cases
### The input strings are empty, so the function should return an empty string
assert string_xor('', '') == '', 'Failed to handle empty input strings.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input strings are very long, consisting of 10^6 1s and 0s
### The binary XOR of the two strings is '0'*10^6
assert string_xor('1'*10**6, '1'*10**6) == '0'*10**6, 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The input strings contain non-numeric characters, so the function should return an empty string
assert not string_xor('10a1', '1010'), 'Failed to handle input strings with non-numeric characters.'

#### The input strings are not strings, so the function should return an empty string
assert not string_xor(['1', '0', '1'], '1010'), 'Failed to handle input strings that are not strings.'

### The input strings have different lengths, so the function should return an empty string
assert not string_xor('10101', '101'), 'Failed to handle input strings of different lengths.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(string_xor))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
