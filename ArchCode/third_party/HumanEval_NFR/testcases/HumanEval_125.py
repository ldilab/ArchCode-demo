from solutions.HumanEval_125 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The input string has whitespaces, so the function should split the words on whitespaces
assert split_words("Hello world!") == ["Hello", "world!"], 'Failed to split the words on whitespaces.'

### The input string has commas, so the function should split the words on commas
assert split_words("Hello,world!") == ["Hello", "world!"], 'Failed to split the words on commas.'

### The input string has no whitespaces or commas, so the function should return the count of lowercase letters with odd order
### The lowercase letters with odd order in the alphabet are 'b', 'd', 'f', so the function should return 3
assert split_words("abcdef") == 3, 'Failed to return the count of lowercase letters with odd order.'

## Edge Cases
### The input string is empty, so the function should return an empty list or 0 depending on the situation
assert split_words("") == [], 'Failed to handle an empty input string.'

### The input string has only whitespaces, so the function should return an empty list
assert split_words("   ") == [], 'Failed to handle an input string with only whitespaces.'

### The input string has only commas, so the function should return an empty list
assert split_words(",,,") == [], 'Failed to handle an input string with only commas.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input string is very long with no whitespaces or commas, so the function should return the count of lowercase letters
### The lowercase letters with even order in the alphabet are 'a', 'c', 'e', 'g', 'i', 'k', 'm', 'o', 'q', 's', 'u', 'w', 'y', so the function should return 13
assert split_words("acegikmoqsuwy") == 0, 'Failed to handle even order alphabets.'

### The input string is very long with alternating whitespaces and commas, so the function should split the words on whitespaces
### The expected result is a list of 10^6 words, each word containing one lowercase letter
expected_result = [chr(97 + i) for i in range(26)] * (10**6 // 26)
assert split_words(" ".join(expected_result)) == expected_result, 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The txt input is not a string, so the function should handle the case not to raise error
assert not split_words(12345), 'Failed to handle case where the input txt is not a string.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 10
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(split_words))
assert result.total_complexity <= 10, 'Failed to have a Cyclomatic Complexity less than or equal to 10 by Radon.'