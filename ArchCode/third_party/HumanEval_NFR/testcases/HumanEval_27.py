from solutions.HumanEval_27 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The input string is "Hello"
### The lowercase characters 'e', 'l', and 'l' are flipped to uppercase, and the uppercase character 'H' is flipped to lowercase
### The expected output is "hELLO"
assert flip_case("Hello") == "hELLO", 'Failed to flip lowercase characters to uppercase and vice versa.'

### The input string is "wORLD"
### The lowercase character 'w' is flipped to uppercase, and the uppercase characters 'O', 'R', 'L', and 'D' are flipped to lowercase
### The expected output is "World"
assert flip_case("wORLD") == "World", 'Failed to flip lowercase characters to uppercase and vice versa.'

## Edge Cases
### The input string is empty, so the function should return an empty string
assert flip_case("") == "", 'Failed to handle an empty input string.'

### The input string contains only non-alphabetical characters, so the function should return the input string unchanged
assert flip_case("123#$%^") == "123#$%^", 'Failed to handle a string with no alphabetical characters.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input string has a length of 10^6 and consists of alternating uppercase and lowercase characters
### The expected output is the input string with the case of each character flipped
assert flip_case("AbCdEfGhIjKlMnOpQrStUvWxYz" * 10**4) == "aBcDeFgHiJkLmNoPqRsTuVwXyZ" * 10**4, 'Failed to handle large input size.'

### The input string has a length of 10^6 and consists of only lowercase characters
### The expected output is the input string with all characters flipped to uppercase
assert flip_case("abcdefghijklmnopqrstuvwxyz" * 10**4) == "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 10**4, 'Failed to handle case where all characters are lowercase.'

### The input string has a length of 10^6 and consists of only uppercase characters
### The expected output is the input string with all characters flipped to lowercase
assert flip_case("ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 10**4) == "abcdefghijklmnopqrstuvwxyz" * 10**4, 'Failed to handle case where all characters are uppercase.'

## Specific Quality Requirements
### Robustness
#### The input is not a string, so the function should handle the case not to raise error
assert not flip_case(123), 'Failed to handle case where the input is not a string.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(flip_case))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
