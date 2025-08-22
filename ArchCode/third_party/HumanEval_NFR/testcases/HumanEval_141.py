from solutions.HumanEval_141 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The file name is valid, satisfies all conditions
assert file_name_check("example.txt") == 'Yes', 'Failed to validate a valid file name.'

### The file name does not start with a letter
assert file_name_check("1example.dll") == 'No', 'Failed to invalidate a file name that does not start with a letter.'

### The file name has more than three digits
assert file_name_check("file_12345.txt") == 'No', 'Failed to invalidate a file name with more than three digits.'

### The file name has more than one dot
assert file_name_check("file.name.txt") == 'No', 'Failed to invalidate a file name with more than one dot.'

### The file name has an empty substring before the dot
assert file_name_check(".txt") == 'No', 'Failed to invalidate a file name with an empty substring before the dot.'

### The file name has an invalid extension
assert file_name_check("example.jpeg") == 'No', 'Failed to invalidate a file name with an invalid extension.'

## Edge Cases
### The file name is an empty string, so it should return 'No'
assert file_name_check("") == 'No', 'Failed to handle an empty file name.'

### The file name has exactly three digits, so it is valid
assert file_name_check("file_123.txt") == 'Yes', 'Failed to validate a file name with exactly three digits.'

### The file name has exactly one digit, so it is valid
assert file_name_check("file_1.txt") == 'Yes', 'Failed to validate a file name with exactly one digit.'

### The file name has exactly one letter before the dot, so it is valid
assert file_name_check("a.txt") == 'Yes', 'Failed to validate a file name with exactly one letter before the dot.'

### The file name has an uppercase letter before the dot, so it is valid
assert file_name_check("A.txt") == 'Yes', 'Failed to validate a file name with an uppercase letter before the dot.'

### The file name has an extension of 'txt', so it is valid
assert file_name_check("example.txt") == 'Yes', 'Failed to validate a file name with a valid extension.'

### The file name has an extension of 'exe', so it is valid
assert file_name_check("example.exe") == 'Yes', 'Failed to validate a file name with a valid extension.'

### The file name has an extension of 'dll', so it is valid
assert file_name_check("example.dll") == 'Yes', 'Failed to validate a file name with a valid extension.'

### The file name has an extension that is not 'txt', 'exe', or 'dll', so it is invalid
assert file_name_check("example.pdf") == 'No', 'Failed to invalidate a file name with an invalid extension.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The file name has a length of 10^6 characters and satisfies all conditions, so it is valid
assert file_name_check("a" * 10**6 + ".txt") == 'Yes', 'Failed to validate a file name with a large length.'

### The file name has a length of 10^6 characters and does not satisfy the condition of having exactly one dot, so it is invalid
assert file_name_check("a" * 10**6) == 'No', 'Failed to invalidate a file name with a large length and missing dot.'

## Specific Quality Requirements
### Robustness
#### The file name input is not a string, so it should handle the case not to raise error
assert not file_name_check(123), 'Failed to handle a non-string file name input.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(file_name_check))
assert result.total_complexity <= 10, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'