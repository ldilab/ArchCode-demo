from solutions.HumanEval_48 import *
# Test Cases Regarding Functional Requirements
## General Cases
### An empty string is a palindrome, so the function should return True
assert is_palindrome('') == True, 'Failed to handle an empty string.'

### 'aba' is a palindrome, so the function should return True
assert is_palindrome('aba') == True, 'Failed to handle a palindrome string.'

### 'aaaaa' is a palindrome, so the function should return True
assert is_palindrome('aaaaa') == True, 'Failed to handle a palindrome string.'

### 'zbcd' is not a palindrome, so the function should return False
assert is_palindrome('zbcd') == False, 'Failed to handle a non-palindrome string.'

## Edge Cases
### An empty string is a palindrome, so the function should return True
assert is_palindrome('') == True, 'Failed to handle an empty string.'

### A single-character string is a palindrome, so the function should return True
assert is_palindrome('a') == True, 'Failed to handle a single-character string.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input string contains 10^6 characters, all of which are 'a'
### The string is a palindrome, so the function should return True
assert is_palindrome('a' * 10**6) == True, 'Failed to handle large input size.'

### The input string contains 10^6 characters, all of which are 'a'
### The string is not a palindrome, so the function should return False
assert is_palindrome('a' * 10**6 + 'b') == False, 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The input is not a string, so the function should handle the case not to raise error
assert not is_palindrome(123), 'Failed to handle case where the input is not a string.'

#### The input string contains special characters and spaces, and it is not a palindrome, so the function should return False
assert is_palindrome('A man, a plan, a canal, Panama!') == False, 'Failed to handle case with special characters and spaces.'

#### The input string contains non-alphanumeric characters, but the function should return True
assert is_palindrome('123@321') == True, 'Failed to handle case with non-alphanumeric characters.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(is_palindrome))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
