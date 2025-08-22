from solutions.HumanEval_101 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The input string contains words separated by commas and spaces
### The function should split the string and return an array of the words
assert words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"], 'Failed to split the string into words.'

### The input string contains words separated by commas
### The function should split the string and return an array of the words
assert words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"], 'Failed to split the string into words.'

## Edge Cases
### The input string is empty, so the function should return an empty list
assert words_string("") == [], 'Failed to handle an empty input string.'

### The input string contains only spaces, so the function should return an empty list
assert words_string("   ") == [], 'Failed to handle a string with only spaces.'

### The input string contains only commas, so the function should return an empty list
assert words_string(",,,") == [], 'Failed to handle a string with only commas.'

### The input string contains consecutive commas and spaces
assert words_string("Hi,,my,   ,name, ") == ["Hi", "my", "name"], 'Failed to handle consecutive commas and spaces.'

### The input string contains only one word, so the function should return a list with that word
assert words_string("Hello") == ["Hello"], 'Failed to handle a string with only one word.'

### The input string contains special characters, so the function should return an empty list
assert words_string("Hello #World!") == ["Hello", "#World!"], 'Failed to handle case where the input string contains special characters.'

### The input string has leading and trailing spaces, so the function should remove them and return the array of words
assert words_string("  Hello, my name is John  ") == ['Hello', 'my', 'name', 'is', 'John'], 'Failed to handle leading and trailing spaces.'

### The input string has spaces and commas as the first or last character, so the function should remove them and return the array of words
assert words_string(",Hello, my name is John") == ['Hello', 'my', 'name', 'is', 'John'], 'Failed to handle commas as the first character.'
assert words_string("Hello, my name is John,") == ['Hello', 'my', 'name', 'is', 'John'], 'Failed to handle commas as the last character.'


# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input string contains 10^5 words separated by commas
### The function should split the string and return an array of the words
assert words_string(','.join(str(x) for x in range(10**5))) == [str(x) for x in range(10**5)], 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The input is not a string, so the function should handle the case not to raise error
assert not words_string(123), 'Failed to handle case where the input is not a string.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(words_string))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'