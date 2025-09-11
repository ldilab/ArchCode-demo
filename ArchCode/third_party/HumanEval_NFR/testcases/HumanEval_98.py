from solutions.HumanEval_98 import *
# Test Cases Regarding Functional Requirements
## General Cases
### There is 1 uppercase vowel 'E' at even index 4
assert count_upper('aBCdEf') == 1, 'Failed to count the number of uppercase vowels in even indices.'

### There are no uppercase vowels in even indices
assert count_upper('abcdefg') == 0, 'Failed to handle case where there are no uppercase vowels in even indices.'

### There are no uppercase vowels in even indices
assert count_upper('dBBE') == 0, 'Failed to handle case where there are no uppercase vowels in even indices.'

## Edge Cases
### The input string is empty, so the function should return 0
assert count_upper('') == 0, 'Failed to handle an empty input string.'

### There are no uppercase vowels in even indices
assert count_upper('12345') == 0, 'Failed to handle case where the input string does not contain any uppercase vowels in even indices.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input string has a length of 10^6 and all characters are uppercase vowels
### All uppercase vowels are at even indices, so the expected count is 10^6 / 2 = 500,000
assert count_upper('A' * 10**6) == 500000, 'Failed to handle large input size.'

### The input string has a length of 10^6 and all characters are lowercase vowels
### There are no uppercase vowels in even indices, so the expected count is 0
assert count_upper('a' * 10**6) == 0, 'Failed to handle large input size when there are no uppercase vowels in even indices.'

### The input string has a length of 10^6 and all characters are consonants
### There are no uppercase vowels in even indices, so the expected count is 0
assert count_upper('z' * 10**6) == 0, 'Failed to handle large input size when there are no uppercase vowels in even indices.'

### The input string has a length of 10^6 and all characters are digits
### There are no uppercase vowels in even indices, so the expected count is 0
assert count_upper('1' * 10**6) == 0, 'Failed to handle large input size when there are no uppercase vowels in even indices.'

## Specific Quality Requirements
### Robustness
#### The input is not a string, so the function should handle the case not to raise error
assert not count_upper(12345), 'Failed to handle case where the input is not a string.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(count_upper))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'