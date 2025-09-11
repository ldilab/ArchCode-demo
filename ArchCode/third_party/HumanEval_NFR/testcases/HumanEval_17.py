from solutions.HumanEval_17 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The music string contains a whole note, a half note, a quarter note, and two whole notes
### The function should return the corresponding durations: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
assert parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4], 'Failed to parse the music string correctly.'

## Edge Cases
### The music string is empty, so the function should return an empty list
assert parse_music('') == [], 'Failed to handle an empty music string.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The music string contains 10^6 whole notes
### The function should return a list with 10^6 elements, all of which are 4
assert parse_music('o ' * 10**6) == [4] * 10**6, 'Failed to handle large input size.'

### The music string contains 10^6 half notes
### The function should return a list with 10^6 elements, all of which are 2
assert parse_music('o| ' * 10**6) == [2] * 10**6, 'Failed to handle large input size.'

### The music string contains 10^6 quarter notes
### The function should return a list with 10^6 elements, all of which are 1
assert parse_music('.| ' * 10**6) == [1] * 10**6, 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The music string input is not a string, so the function should return an empty list
assert not parse_music(12345), 'Failed to handle case where the input music_string is not a string.'

### The music string contains invalid characters 'a' and 'b'
### The function should skip these characters and return the durations of the valid notes: [4, 2, 1, 2]
assert not parse_music('o o| .| a| b| .| o|'), 'Failed to skip invalid characters in the music string.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(parse_music))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
