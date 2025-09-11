from solutions.HumanEval_148 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The planets between Jupiter and Neptune are Saturn and Uranus
assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus"), 'Failed to return the planets between Jupiter and Neptune.'

### The planets between Earth and Mercury are Venus
assert bf("Earth", "Mercury") == ("Venus", ), 'Failed to return the planets between Earth and Mercury.'

### The planets between Mercury and Uranus are Venus, Earth, Mars, Jupiter, and Saturn
assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn"), 'Failed to return the planets between Mercury and Uranus.'

## Edge Cases
### The planets between Earth and Earth are none, so the function should return an empty tuple
assert bf("Earth", "Earth") == (), 'Failed to handle case where planet1 and planet2 are the same planet.'

### Case-insensitive planet names: the planets between jupiter and nEPTune are Saturn and Uranus
assert bf("jupiter", "nEPTune") == ("Saturn", "Uranus"), 'Failed to handle case-insensitive planet names.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### Satisfied if no errors occur across all test cases

## Specific Quality Requirements
### Robustness
#### Invalid planet names: the function should handle the case not to raise error
assert not bf("Earth", "Pluto"), 'Failed to handle case where planet1 is an invalid planet name.'
assert not bf("Pluto", "Mars"), 'Failed to handle case where planet2 is an invalid planet name.'

#### Non-string inputs: the function should handle the case not to raise error
assert not bf(123, "Jupiter"), 'Failed to handle case where planet1 is not a string.'
assert not bf("Saturn", None), 'Failed to handle case where planet2 is not a string.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 10
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(bf))
assert result.total_complexity <= 10, 'Failed to have a Cyclomatic Complexity less than or equal to 10 by Radon.'
