from solutions.HumanEval_107 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The input is 3, so there is one even palindrome (2) and two odd palindromes (1, 3)
assert even_odd_palindrome(3) == (1, 2), 'Failed to count even and odd palindromes correctly.'

### The input is 12, so there are four even palindromes (2, 4, 6, 8) and six odd palindromes (1, 3, 5, 7, 9, 11)
assert even_odd_palindrome(12) == (4, 6), 'Failed to count even and odd palindromes correctly.'

### The input is 1000, so there are 48 even palindromes and 60 odd palindromes.
assert even_odd_palindrome(1000) == (48, 60), 'Failed to count even and odd palindromes correctly.'

## Edge Cases
### The input is 1, so there are no even palindromes and one odd palindrome (1)
assert even_odd_palindrome(1) == (0, 1), 'Failed to handle the case where n is 1.'

### The input is 2, so there is one even palindrome (2) and one odd palindrome (1)
assert even_odd_palindrome(2) == (1, 1), 'Failed to handle the case where n is 2.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input is 10^4, so there are 88 even palindromes and 110 odd palindromes.
assert even_odd_palindrome(10**4) == (88, 110), 'Failed to handle large input size.'

### The input is 10^5, so there are 488 even palindromes and 610 odd palindromes.
assert even_odd_palindrome(10**5) == (488, 610), 'Failed to handle large input size.'

### The input is 10^6 + 1, so there are 888 even palindromes and 1111 odd palindromes.
assert even_odd_palindrome(10**6 + 1) == (888, 1111), 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The input n is not an integer, so the function should handle the case not to raise error
assert not even_odd_palindrome('invalid'), 'Failed to handle the case where the input n is not an integer.'

#### The input n is a negative number, so the function should handle the case not to raise error
assert not even_odd_palindrome(-10), 'Failed to handle the case where the input n is a negative number.'

#### The input n is a float, so the function should handle the case not to raise error
assert not even_odd_palindrome(3.5), 'Failed to handle the case where the input n is not an integer.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 10
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(even_odd_palindrome))
assert result.total_complexity <= 10, 'Failed to have a Cyclomatic Complexity less than or equal to 10 by Radon.'