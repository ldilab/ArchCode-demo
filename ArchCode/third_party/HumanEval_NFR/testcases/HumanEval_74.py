from solutions.HumanEval_74 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The total number of characters in ['hi', 'admin'] is 7, which is larger than the total number of characters in ['hI', 'Hi'] (4)
### Therefore, the function should return ['hI', 'Hi']
assert total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi'], 'Failed to return the list with the lesser total number of characters.'

### The total number of characters in ['hi', 'admin'] is 7, which is less than the total number of characters in ['hi', 'hi', 'admin', 'project'] (16)
### Therefore, the function should return ['hi', 'admin']
assert total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin'], 'Failed to return the list with the lesser total number of characters.'

### The total number of characters in ['hi', 'admin'] is 7, which is the same as the total number of characters in ['hI', 'hello'] (7)
### Since they have the same total number of characters, the function should return the first list, which is ['hi', 'admin']
assert total_match(['hi', 'admin'], ['hI', 'hello']) == ['hi', 'admin'], 'Failed to return the first list when both lists have the same total number of characters.'

### The total number of characters in ['4'] is 1, which is less than the total number of characters in ['1', '2', '3', '4', '5'] (5)
### Therefore, the function should return ['4']
assert total_match(['4'], ['1', '2', '3', '4', '5']) == ['4'], 'Failed to return the list with the lesser total number of characters.'

## Edge Cases
### The first list is empty, so the function should return an empty list
assert total_match([], ['hI', 'Hi']) == [], 'Failed to handle case where the first list is empty.'

### The second list is empty, so the function should return an empty list
assert total_match(['hi', 'admin'], []) == [], 'Failed to handle case where the second list is empty.'

### Both lists are empty, so the function should return an empty list
assert total_match([], []) == [], 'Failed to handle case where both lists are empty.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The total number of characters in both lists is 10^6
assert total_match(['a'] * 10**6, ['b'] * 10**6) == ['a'] * 10**6, 'Failed to handle large input size.'

### The total number of characters is about 10^6
assert total_match(['a'] * 10**6, ['b'] * (1+10**6)) == ['b'] * (1+10**6), 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The first input is not a list, so the function should handle the case not to raise error
assert not total_match('invalid', ['hi', 'admin']), 'Failed to handle case where the first input is not a list.'

#### The second input is not a list, so the function should handle the case not to raise error
assert not total_match(['hi', 'admin'], 'invalid'), 'Failed to handle case where the second input is not a list.'

#### The first input list contains elements that are not strings, so the function should handle the case not to raise error
assert not total_match([1, 2, 3], ['hi', 'admin']), 'Failed to handle case where the first input list contains elements that are not strings.'

#### The second input list contains elements that are not strings, so the function should handle the case not to raise error
assert not total_match(['hi', 'admin'], [1, 2, 3]), 'Failed to handle case where the second input list contains elements that are not strings.'

#### The strings in the first input list contain non-alphabetic characters, so the function should return an empty list
assert total_match(['h1', 'admin'], ['hi', 'admin']) == [], 'Failed to handle case where the strings in the first input list contain non-alphabetic characters.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 10
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(total_match))
assert result.total_complexity <= 10, 'Failed to have a Cyclomatic Complexity less than or equal to 10 by Radon.'