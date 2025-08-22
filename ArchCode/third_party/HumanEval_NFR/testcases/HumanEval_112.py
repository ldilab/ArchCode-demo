from solutions.HumanEval_112 import *
# Test Cases Regarding Functional Requirements
## General Cases
### Deleting 'a' and 'e' from 'abcde' results in 'bcd', which is not a palindrome
assert reverse_delete("abcde", "ae") == ('bcd', False), 'Failed for general case 1'

### Deleting 'b' from 'abcdef' results in 'acdef', which is not a palindrome
assert reverse_delete("abcdef", "b") == ('acdef', False), 'Failed for general case 2'

### Deleting 'a' and 'b' from 'abcdedcba' results in 'cdedc', which is a palindrome
assert reverse_delete("abcdedcba", "ab") == ('cdedc', True), 'Failed for general case 3'

## Edge Cases
### Both `s` and `c` are empty strings, so the result should be an empty string and True
assert reverse_delete("", "") == ('', True), 'Failed to handle empty input strings'

### `s` is an empty string, so the result should be an empty string and True
assert reverse_delete("", "abc") == ('', True), 'Failed to handle empty `s` string'

### `c` is an empty string
assert reverse_delete("abcde", "") == ('abcde', False), 'Failed to handle empty `c` string'

## Test Cases Regarding Non-functional Requirements
### Performance Requirements
#### The length of `s` is 10^6 and `c` is 1
#### Deleting 'a' from 'a' results in an empty string, which is a palindrome
assert reverse_delete('a' * 10**6, 'a') == ('', True), 'Failed to handle large input size'

#### Deleting 'd' from the input string obtains palindrome
assert reverse_delete('a' * 10**5 + 'b' * 10**5 + 'a' * 10**5 + 'd', 'defghijklmnopqrstuvwxyz') == ('a' * 10**5 + 'b' * 10**5 + 'a' * 10**5, True), 'Failed to handle large input size'

## Specific Quality Requirements
### Robustness
#### The inputs `s` and `c` are not strings, so the result should be None
assert not reverse_delete(123, ['a', 'b']), 'Failed to handle non-string inputs'

#### `s` contains special characters and whitespaces
#### Deleting '!' and whitespaces from 'a ! b c !b! a' results in 'abcba', which is a palindrome
assert reverse_delete('a ! b c !b! a', '! ') == ('abcba', True), 'Failed to handle special characters and whitespaces in `s`'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 10
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(reverse_delete))
assert result.total_complexity <= 10, 'Failed to have a Cyclomatic Complexity less than or equal to 10 by Radon.'