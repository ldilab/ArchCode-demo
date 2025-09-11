from solutions.HumanEval_78 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The input num string contains 1 prime hexadecimal digit, which is B
assert hex_key("AB") == 1, 'Failed to count the number of prime hexadecimal digits.'

### The input num string contains 2 prime hexadecimal digits, which are two 7's
assert hex_key("1077E") == 2, 'Failed to count the number of prime hexadecimal digits.'

### The input num string contains 4 prime hexadecimal digits, which are B, D, and two 3's
assert hex_key("ABED1A33") == 4, 'Failed to count the number of prime hexadecimal digits.'

### The input num string contains all 6 prime hexadecimal digits
assert hex_key("123456789ABCDEF0") == 6, 'Failed to count the number of prime hexadecimal digits.'

### The input num string contains 2 prime hexadecimal digits, which are 2
assert hex_key("2020") == 2, 'Failed to count the number of prime hexadecimal digits.'

## Edge Cases
### The input num string is empty, so the function should return 0
assert hex_key("") == 0, 'Failed to handle an empty input num string.'

### The input num string does not contain any prime hexadecimal digits, so the function should return 0
assert hex_key("14689") == 0, 'Failed to handle case where no prime hexadecimal digits are present.'

### The input num string contains all prime hexadecimal digits, so the function should return the length of the num string
assert hex_key("2357BD") == 6, 'Failed to handle case where all hexadecimal digits are prime.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The num string contains 10^6 characters, all of which are prime hexadecimal digits
### The function should return 10^6
assert hex_key("2" * 10**6) == 10**6, 'Failed to handle large input size.'

### The num string contains 10^6 characters, none of which are prime hexadecimal digits
### The function should return 0
assert hex_key("4" * 10**6) == 0, 'Failed to handle case where no prime hexadecimal digits are present.'

## Specific Quality Requirements
### Robustness
#### The input num is not a string, so the function should handle the case not to raise error
assert not hex_key(1234), 'Failed to handle case where the input num is not a string.'

#### The input num contains lowercase hexadecimal characters, so the function should handle the case not to raise error
assert not hex_key("abcdef"), 'Failed to handle case where the input num contains lowercase hexadecimal characters.'

#### The input num contains non-hexadecimal characters, so the function should handle the case not to raise error
assert not hex_key("GHIJKL"), 'Failed to handle case where the input num contains non-hexadecimal characters.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(hex_key))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'