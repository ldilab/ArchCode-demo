from solutions.HumanEval_143 import *
# Test Cases Regarding Functional Requirements
## General Cases
### There is one word in the sentence whose length is a prime number: "is"
assert words_in_sentence("This is a test") == "is", 'Failed to return the correct string with words of prime lengths.'

### There are two words in the sentence whose lengths are prime numbers: "go" and "for"
### The order of the words in the new string should be the same as the original one: "go for"
assert words_in_sentence("lets go for swimming") == "go for", 'Failed to return the correct string with words of prime lengths.'

## Edge Cases
### The sentence is empty, so the function should return an empty string
assert words_in_sentence("") == '', 'Failed to handle an empty sentence.'

### None of the words in the sentence have a length that is a prime number
### The function should return an empty string
assert words_in_sentence("This isnott a primee") == '', 'Failed to handle case where no word has a prime length.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The sentence contains 10^6 words, all of which have a length of 10
### The function should return an empty string since there are no words with prime lengths
assert words_in_sentence(" ".join(["a" * 10] * 10**6)) == '', 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The sentence input is not a string, so the function should handle the case not to raise error
assert not words_in_sentence(12345), 'Failed to handle case where the input sentence is not a string.'

#### The sentence input contains characters other than letters, so the function should handle the case not to raise error
assert not words_in_sentence("This is a sentence with special characters!"), 'Failed to handle case where the input sentence contains non-letter characters.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 10
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(words_in_sentence))
assert result.total_complexity <= 10, 'Failed to have a Cyclomatic Complexity less than or equal to 10 by Radon.'