from solutions.HumanEval_91 import *
# Test Cases Regarding Functional Requirements
## General Cases
### There are no boredoms in the string, so the function should return 0
assert is_bored("Hello world") == 0, 'Failed to handle case where there are no boredoms in the string.'

### There is one boredom in the string, so the function should return 1
assert is_bored("The sky is blue. The sun is shining. I love this weather") == 1, 'Failed to count the number of boredoms correctly.'

### The input string contains multiple boredoms, so the function should return the correct count
assert is_bored("I am bored! I hate this. I need something to do.") == 3, 'Failed to count the number of boredoms correctly.'

## Edge Cases
### The input string is empty, so the function should return 0
assert is_bored("") == 0, 'Failed to handle an empty input string.'

### The entire input string is a boredom, so the function should return 1
assert is_bored("I am bored?") == 1, 'Failed to handle case where the entire string is a boredom.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input string contains 10^6 characters, all of which are the letter 'I'
### The entire string is a boredom, so the function should return 1
assert is_bored("I" * 10**6) == 1, 'Failed to handle large input size.'

### The input string contains 10^6 characters, all of which are the letter 'A'
### There are no boredoms in the string, so the function should return 0
assert is_bored("A" * 10**6) == 0, 'Failed to handle large input size.'

### The input string contains 3 * 10^5 sentences, all of which start with letter 'I'
### so the function should return 3 * 10^5
assert is_bored("I? I! I. " * 10**5) == 3 * 10**5, 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The input is not a string, so the function should return 0
assert not is_bored(12345), 'Failed to handle case where the input is not a string.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 10
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(is_bored))
assert result.total_complexity <= 10, 'Failed to have a Cyclomatic Complexity less than or equal to 10 by Radon.'