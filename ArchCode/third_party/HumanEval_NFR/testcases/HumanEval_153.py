from solutions.HumanEval_153 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The strongest extension is 'SErviNGSliCes' with a strength of -1
assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes', 'Failed to find the strongest extension.'

### The strongest extension is 'AA' with a strength of 2
assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA', 'Failed to find the strongest extension.'

## Edge Cases
### Two or more extensions have the same strength, so the function should return the first one in the list
assert Strongest_Extension('my_class', ['AA', 'Be', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 'II', 'JJ', 'KK']) == 'my_class.AA', 'Failed to return the first extension in the list when two or more extensions have the same strength.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The extensions list contains 10^6 elements, all of which are 'AA'
### The strength of each extension is 0
### The function should return 'Slices.AA'
assert Strongest_Extension('Slices', ['AA'] * 10**6) == 'Slices.AA', 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
### The class_name is not a string, so the function should handle the case not to raise error
assert not Strongest_Extension(123, ['SErviNGSliCes', 'Cheese', 'StuFfed']), 'Failed to handle case where the class_name is not a string.'

### The class_name is an empty string, so the function should handle the case not to raise error
assert not Strongest_Extension('', ['SErviNGSliCes', 'Cheese', 'StuFfed']), 'Failed to handle case where the class_name is an empty string.'

### The extensions list is empty, so the function should handle the case not to raise error
assert not Strongest_Extension('Slices', []), 'Failed to handle an empty extensions list.'

#### The class_name input is not a string, so the function should handle the case not to raise error
assert not Strongest_Extension(123, ['AA', 'Be', 'CC']), 'Failed to handle case where the class_name is not a string.'

#### The extensions input is not a list, so the function should handle the case not to raise error
assert not Strongest_Extension('my_class', 'AA'), 'Failed to handle case where the extensions is not a list.'

#### The extensions list contains elements that are not strings, so the function should handle the case not to raise error
assert not Strongest_Extension('my_class', ['AA', 'Be', 123]), 'Failed to handle case where the extensions list contains elements that are not strings.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 10
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(Strongest_Extension))
assert result.total_complexity <= 10, 'Failed to have a Cyclomatic Complexity less than or equal to 10 by Radon.'