from solutions.HumanEval_80 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The string has length less than 3, so it is not happy
assert is_happy('a') == False, 'Failed to handle case where the string has length less than 3.'

### The string has consecutive repeating characters, so it is not happy
assert is_happy('aa') == False, 'Failed to handle case where the string has consecutive repeating characters.'

### The string has distinct consecutive characters, so it is happy
assert is_happy('abcd') == True, 'Failed to handle case where the string has distinct consecutive characters.'

### The string has consecutive repeating characters, so it is not happy
assert is_happy('aabb') == False, 'Failed to handle case where the string has consecutive repeating characters.'

### The string has distinct consecutive characters, so it is happy
assert is_happy('adb') == True, 'Failed to handle case where the string has distinct consecutive characters.'

### The string has consecutive repeating characters, so it is not happy
assert is_happy('xyy') == False, 'Failed to handle case where the string has consecutive repeating characters.'

## Edge Cases
### The string is empty, so it is not happy
assert is_happy('') == False, 'Failed to handle an empty string.'

### The string does not have any consecutive repeating characters, but it is not happy
assert is_happy('aba') == False, 'Failed to handle case where the string has repeating characters that are not adjacent to each other.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The string has length 3 * 10^5 and every 3 consecutive letters are distinct
### The function should return True
assert is_happy('abc' * 10**5) == True, 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The input is not a string, so the function should return False
assert not is_happy(123), 'Failed to handle case where the input is not a string.'

#### The input contains non-alphabetic characters
assert is_happy('ab1ab') == True, 'Failed to handle case where the input contains non-alphabetic characters.'

#### The input contains whitespaces
assert is_happy('   abc   ') == False, 'Failed to handle case where the input has whitespaces.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(is_happy))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'