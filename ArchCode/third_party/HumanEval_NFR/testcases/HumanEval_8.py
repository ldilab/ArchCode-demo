from solutions.HumanEval_8 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The sum of an empty list is 0 and the product is 1
assert sum_product([]) == (0, 1), 'Failed to handle an empty input list.'

### The sum of [1, 2, 3, 4] is 10 and the product is 24
assert sum_product([1, 2, 3, 4]) == (10, 24), 'Failed to calculate the sum and product correctly.'

### The sum of [0, 0, 0] is 0 and the product is 0
assert sum_product([0, 0, 0]) == (0, 0), 'Failed to calculate the sum and product correctly when all elements are 0.'

## Edge Cases
### The sum of an empty list is 0 and the product is 1
assert sum_product([]) == (0, 1), 'Failed to handle an empty input list.'

### The sum of [10^6] is 10^6 and the product is 10^6
assert sum_product([10**4]) == (10**4, 10**4), 'Failed to handle a list with a single element.'

### The sum of [0, 0, 0, ..., 0] (10^6 elements) is 0 and the product is 0
assert sum_product([0] * 10**6) == (0, 0), 'Failed to handle a list with multiple elements, all of which are 0.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The sum of [1, 2, 3, ..., 10^4] is 50005000 and the product is 100000!
import math
assert sum_product(list(range(1, 10**4 + 1))) == (50005000, math.factorial(10**4)), 'Failed to calculate the sum and product correctly for a large input size.'


## Specific Quality Requirements
### Robustness
#### The numbers input is not a list of integers, so the function should return an empty tuple
assert not sum_product('invalid'), 'Failed to handle case where the input numbers is not a list of integers.'

#### The numbers list contains elements that are not integers, so the function should return an empty tuple
assert not sum_product([1, 2, 'invalid', 4]), 'Failed to handle case where the input list contains elements that are not integers.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(sum_product))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
