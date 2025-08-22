from solutions.HumanEval_124 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The date string is valid, so the function should return True
assert valid_date('03-11-2000') == True, 'Failed to validate a valid date.'

### The date string has an invalid month, so the function should return False
assert valid_date('15-01-2012') == False, 'Failed to invalidate a date with an invalid month.'

### The date string has an invalid day, so the function should return False
assert valid_date('04-0-2040') == False, 'Failed to invalidate a date with an invalid day.'

### The date string is valid, so the function should return True
assert valid_date('06-04-2020') == True, 'Failed to validate a valid date.'

### The date string has an invalid format, so the function should return False
assert valid_date('06/04/2020') == False, 'Failed to invalidate a date with an invalid format.'

## Edge Cases
### The date string is empty, so the function should return False
assert valid_date('') == False, 'Failed to handle an empty date string.'

### The date string has an invalid format, so the function should return False
assert valid_date('2020-06-04') == False, 'Failed to handle an invalid date format.'

### The date string has an invalid month, so the function should return False
assert valid_date('13-04-2020') == False, 'Failed to invalidate a date with an invalid month.'

### The date string has an invalid day, so the function should return False
assert valid_date('02-30-2020') == False, 'Failed to invalidate a date with an invalid day.'

### The date string has an invalid year format, so the function should return False
assert valid_date('02-04-20') == False, 'Failed to handle an invalid year format.'

### The date string has a non-integer value for days, so the function should return False
assert valid_date('02-aa-2020') == False, 'Failed to handle a non-integer value for days.'

### The date string has a non-integer value for months, so the function should return False
assert valid_date('bb-04-2020') == False, 'Failed to handle a non-integer value for months.'

### The date string has a non-integer value for years, so the function should return False
assert valid_date('02-04-cccc') == False, 'Failed to handle a non-integer value for years.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The date string is valid, so the function should return True
assert valid_date('12-31-9999') == True, 'Failed to validate a valid date with the maximum possible values.'

### The date string is valid, so the function should return True
assert valid_date('01-01-0001') == True, 'Failed to validate a valid date with the minimum possible values.'

## Specific Quality Requirements
### Robustness
#### The date input is not a string, so the function should handle the case not to raise error
assert not valid_date(123), 'Failed to handle a non-string date input.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 10
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(valid_date))
assert result.total_complexity <= 10, 'Failed to have a Cyclomatic Complexity less than or equal to 10 by Radon.'