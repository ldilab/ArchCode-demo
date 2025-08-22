from solutions.HumanEval_111 import *
# Test Cases Regarding Functional Requirements
## General Cases
### Each letter in the string appears once, so the dictionary should have a count of 1 for each letter
assert histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}, 'Failed to count each letter with a count of 1.'

### Both 'a' and 'b' appear twice in the string, so the dictionary should have a count of 2 for both letters
assert histogram('a b b a') == {'a': 2, 'b': 2}, 'Failed to count letters with multiple occurrences.'

### Both 'a' and 'b' appear twice in the string, so the dictionary should have a count of 2 for both letters
assert histogram('a b c a b') == {'a': 2, 'b': 2}, 'Failed to count letters with multiple occurrences.'

### 'b' appears four times in the string, so the dictionary should have a count of 4 for 'b'
assert histogram('b b b b a') == {'b': 4}, 'Failed to count letter with the most occurrences.'

### The string is empty, so the dictionary should be empty as well
assert histogram('') == {}, 'Failed to handle an empty string.'

## Edge Cases
### The string contains only spaces, so the dictionary should be empty
assert histogram('    ') == {}, 'Failed to handle a string with only spaces.'

### All letters in the string have the same count of 1, so the dictionary should have a count of 1 for each letter
assert histogram('a b c d e f g') == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1}, 'Failed to handle case where all letters have the same count.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The string contains 10^4 + 1 lowercase letters 'a'
assert histogram(' '.join(list('a b c d e f g h i j k l m n o p q r s t u v w x y z') * 10**4) + ' a') == {'a': 10**4 + 1}, 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The input is not a string, so the function should handle the case not to raise error
assert not histogram(123), 'Failed to handle case where the input is not a string.'

#### The string contains no lowercase letters, so the function should handle the case not to raise error
assert not histogram('1234567890'), 'Failed to handle a string with no lowercase letters.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 10
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(histogram))
assert result.total_complexity <= 10, 'Failed to have a Cyclomatic Complexity less than or equal to 10 by Radon.'