from solutions.HumanEval_89 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The input string is 'hi'
### Each letter is shifted down by two multiplied by two places in the alphabet
### The output should be 'lm'
assert encrypt('hi') == 'lm', 'Failed to encrypt the input string.'

### The input string is 'asdfghjkl'
### Each letter is shifted down by two multiplied by two places in the alphabet
### The output should be 'ewhjklnop'
assert encrypt('asdfghjkl') == 'ewhjklnop', 'Failed to encrypt the input string.'

### The input string is 'gf'
### Each letter is shifted down by two multiplied by two places in the alphabet
### The output should be 'kj'
assert encrypt('gf') == 'kj', 'Failed to encrypt the input string.'

### The input string is 'et'
### Each letter is shifted down by two multiplied by two places in the alphabet
### The output should be 'ix'
assert encrypt('et') == 'ix', 'Failed to encrypt the input string.'

## Edge Cases
### The input string is empty, so the output should also be empty
assert encrypt('') == '', 'Failed to handle an empty input string.'

### The input string contains only alphabetic characters, so the output should be the encrypted string
assert encrypt('abcdefghijklmnopqrstuvwxyz') == 'efghijklmnopqrstuvwxyzabcd', 'Failed to encrypt the input string.'

#### The input string contains uppercase letters, so the function should handle them and return the encrypted string
assert encrypt('AbCdEfG') == 'EfGhIjK', 'Failed to handle uppercase letters.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input string contains 10^6 alphabetic characters
assert encrypt('a' * 10**6) == 'e' * 10**6, 'Failed to handle large input size.'

### The input string contains 10^6 non-alphabetic characters, so the output should be the same as the input
assert encrypt('abcdefghijklmnopqrstuvwxyz' * 10**5) == 'efghijklmnopqrstuvwxyzabcd' * 10**5, 'Failed to handle large input size.'

### The input string contains 26 * 10^5 characters
assert encrypt('a!' * 10**6) == 'a!' * 10**6, 'Failed to handle large input size with alternating alphabetic and non-alphabetic characters.'

## Specific Quality Requirements
### Robustness
#### The input is not a string, so the function should handle the case not to raise error
assert not encrypt(123), 'Failed to handle a non-string input.'

### The input string contains only non-alphabetic characters, so the output should be None
assert not encrypt('123!@#'), 'Failed to handle a string with only non-alphabetic characters.'

#### The input string contains Unicode characters, so the function should consider only alphabetic characters and ignore non-alphabetic characters
assert not encrypt('αβγδε'), 'Failed to handle Unicode characters.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 10
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(encrypt))
assert result.total_complexity <= 10, 'Failed to have a Cyclomatic Complexity less than or equal to 10 by Radon.'