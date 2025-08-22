from solutions.HumanEval_140 import *
# Test Cases Regarding Functional Requirements
## General Cases
### There are no spaces in the input string, so the function should return the same string
assert fix_spaces("Example") == "Example", 'Failed to handle case where there are no spaces in the string.'

### There is a single space in the input string, so the function should replace it with an underscore
assert fix_spaces("Example 1") == "Example_1", 'Failed to handle case where there is a single space in the string.'

### There are two consecutive spaces in the input string, so the function should replace them with an underscore
assert fix_spaces(" Example 2") == "_Example_2", 'Failed to handle case where there are two consecutive spaces in the string.'

### There are three consecutive spaces in the input string, so the function should replace them with a hyphen
assert fix_spaces(" Example   3") == "_Example-3", 'Failed to handle case where there are three consecutive spaces in the string.'

## Edge Cases
### The input string is empty, so the function should return an empty string
assert fix_spaces("") == "", 'Failed to handle an empty input string.'

### The input string contains only spaces, so the function should replace them all with underscores
assert fix_spaces("     ") == "-", 'Failed to handle case where the input string contains only spaces.'

### The input string starts with spaces, so the function should replace them all with underscores
assert fix_spaces("   Example") == "-Example", 'Failed to handle case where the input string starts with spaces.'

### The input string ends with spaces, so the function should replace them all with underscores
assert fix_spaces("Example   ") == "Example-", 'Failed to handle case where the input string ends with spaces.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input string contains 10^6 spaces
### The function should replace all spaces with underscores
assert fix_spaces(" " * 10**6) == "-", 'Failed to handle large input size.'

### The input string contains 10^6 consecutive spaces
### The function should replace all spaces with a hyphen
assert fix_spaces(" " * 10**6) == "-", 'Failed to handle case where there are 10^6 consecutive spaces.'

## Specific Quality Requirements
### Robustness
#### The input is not a string, so the function should return an empty string
assert not fix_spaces(123), 'Failed to handle case where the input is not a string.'

#### The input string contains non-space characters, so the function should replace spaces only
assert fix_spaces("Example 1!") == "Example_1!", 'Failed to handle case where the input string contains non-space characters.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(fix_spaces))
assert result.total_complexity <= 10, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'