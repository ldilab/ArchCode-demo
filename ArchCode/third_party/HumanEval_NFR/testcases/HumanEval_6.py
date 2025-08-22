from solutions.HumanEval_6 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The input string contains multiple groups of nested parentheses.
### The deepest level of nesting for each group is [2, 3, 1, 3]
assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3], 'Failed to parse nested parentheses.'

## Edge Cases
### The input string is empty, so the function should return an empty list
assert parse_nested_parens('') == [], 'Failed to handle an empty input string.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input string contains 10^6 characters, all of which are '('
### The deepest level of nesting for each group is [10^6]
assert parse_nested_parens('(' * 10**6 + ')' * 10**6) == [10**6], 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The input is not a string, so the function should return an empty list
assert not parse_nested_parens(123), 'Failed to handle case where the input is not a string.'

#### The input string contains unbalanced parentheses, so the function should return an empty list
assert not parse_nested_parens('(()()) (((())()())'), 'Failed to handle case where the input string contains unbalanced parentheses.'

#### The input string contains invalid characters ('A', 'B', 'C'), so the function should return an empty list
assert not parse_nested_parens('(()A()) ((B())()())'), 'Failed to handle case where the input string contains invalid characters.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(parse_nested_parens))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
