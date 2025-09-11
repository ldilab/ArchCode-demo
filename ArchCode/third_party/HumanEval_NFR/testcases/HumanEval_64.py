from solutions.HumanEval_64 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The input string "abcde" contains 2 vowels: 'a' and 'e'
assert vowels_count("abcde") == 2, 'Failed to count the vowels in the string.'

### The input string "ACEDY" contains 3 vowels: 'A', 'E', and 'Y'
assert vowels_count("ACEDY") == 3, 'Failed to count the vowels in the string.'

## Edge Cases
### The input string is empty, so the function should return 0
assert vowels_count("") == 0, 'Failed to handle an empty string.'

### The input string "xyz" does not contain any vowels, so the function should return 0
assert vowels_count("xyz") == 0, 'Failed to handle case where no vowels are present.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input string contains 10^6 characters, all of which are vowels
### The function should correctly count all the vowels and return 10^6
assert vowels_count("a" * 10**6) == 10**6, 'Failed to handle large input size.'

### The input string contains 10^6 characters, none of which are vowels
### The function should correctly count and return 0
assert vowels_count("z" * 10**6) == 0, 'Failed to handle case where no vowels are present in a large input.'

## Specific Quality Requirements
### Robustness
#### The input to the function is not a string, so the function should handle the case not to raise error
assert not vowels_count(123), 'Failed to handle case where the input is not a string.'

#### The input string contains uppercase characters, so the function should correctly count the vowels regardless of case
assert vowels_count("ABCDE") == 2, 'Failed to handle case where the input string contains uppercase characters.'

#### The input string contains non-alphabet characters, so the function should only count the vowels among the alphabetic characters
assert vowels_count("a1e2i3o4u5") == 5, 'Failed to handle case where the input string contains non-alphabet characters.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(vowels_count))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
