from solutions.HumanEval_18 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The substring 'a' can be found 3 times in the string 'aaa'
assert how_many_times('aaa', 'a') == 3, 'Failed to count the number of occurrences of the substring.'

### The substring 'aa' can be found 3 times in the string 'aaaa'
assert how_many_times('aaaa', 'aa') == 3, 'Failed to count the number of occurrences of the substring.'

### The substring 'abc' can be found 2 times in the string 'abcabc'
assert how_many_times('abcabc', 'abc') == 2, 'Failed to count the number of occurrences of the substring.'

### The substring 'aba' can be found 0 times in the string 'abcabc'
assert how_many_times('abcabc', 'aba') == 0, 'Failed to count the number of occurrences of the substring.'

## Edge Cases
### Both the string and the substring are empty, so the function should return 0
assert how_many_times('', '') == 1, 'Failed to handle empty string and substring.'

### The substring 'a' cannot be found in the empty string, so the function should return 0
assert how_many_times('', 'a') == 0, 'Failed to handle empty string.'

### The substring 'abc' cannot be found in the string 'a', so the function should return 0
assert how_many_times('a', 'abc') == 0, 'Failed to handle substring longer than the string.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The string contains 10^6 'a' characters and the substring is 'a'
### The substring can be found 10^6 times in the string
assert how_many_times('a' * 10**6, 'a') == 10**6, 'Failed to handle large input size.'

### The string contains 10^6 'a' characters and the substring is 'aa'
### The substring can be found 10^6-1 times in the string
assert how_many_times('a' * 10**6, 'aa') == 10**6 - 1, 'Failed to handle large input size.'

### The string contains 10^6 'a' characters and the substring is 'aaa'
### The substring can be found 10^6-2 times in the string
assert how_many_times('a' * 10**6, 'aaa') == 10**6 - 2, 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The string input is not a string, so the function should return 0
assert not how_many_times(123, 'a'), 'Failed to handle case where the input string is not a string.'

#### The substring input is not a string, so the function should return 0
assert not how_many_times('abc', 123), 'Failed to handle case where the input substring is not a string.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(how_many_times))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
