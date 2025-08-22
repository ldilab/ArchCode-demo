from solutions.HumanEval_117 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The word "little" contains exactly 4 consonants
assert select_words("Mary had a little lamb", 4) == ["little"], 'Failed to select the word with the specified number of consonants.'

### The words "Mary" and "lamb" both contain exactly 3 consonants
### The function should return them in the order they appear in the string
assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"], 'Failed to select multiple words with the specified number of consonants.'

### None of the words in the string contain exactly 2 consonants
### The function should return an empty list
assert select_words("simple white space", 2) == [], 'Failed to handle case where no word satisfies the condition.'

### The word "world" contains exactly 4 consonants
assert select_words("Hello world", 4) == ["world"], 'Failed to select the word with the specified number of consonants.'

### The word "Uncle" contains exactly 3 consonants
assert select_words("Uncle sam", 3) == ["Uncle"], 'Failed to select the word with the specified number of consonants.'

## Edge Cases
### The input string is empty, so the function should return an empty list
assert select_words("", 5) == [], 'Failed to handle an empty input string.'

### None of the words in the string contain exactly 5 consonants
### The function should return an empty list
assert select_words("Hello world", 5) == [], 'Failed to handle case where no word satisfies the condition.'

### The input string consists of a single word with exactly 1 consonant
### The function should return the word as the only element in the list
assert select_words("Goa", 1) == ["Goa"], 'Failed to handle case where the word has the specified number of consonants.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input string contains 10^6 characters, all of which are consonants
### The input n is 1, so all the words in the string should be selected
### The function should return a list with 10^6 words
assert select_words(" ".join(['a'] * 10**6), 0) == ['a'] * 10**6, 'Failed to handle large input size.'

### The input string contains 10^6 characters, all of which are spaces
### The function should return an empty list since there are no words in the string
assert select_words(" ".join(['a'] * 10**6), 1) == [], 'Failed to handle large input size.'

### The input string contains 10^5 characters, alternating between consonants and vowels
assert select_words("bcdfghjklmnpqrstvwxyz aeiou " * (10**5 // 26), 21) == ["bcdfghjklmnpqrstvwxyz"] * (10**5 // 26), 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The input s is not a string, so the function should handle the case not to raise error
assert not select_words(12345, 5), 'Failed to handle case where the input s is not a string.'

#### The input n is not an integer, so the function should handle the case not to raise error
assert not select_words("hello world", "invalid"), 'Failed to handle case where the input n is not an integer.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 10
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(select_words))
assert result.total_complexity <= 10, 'Failed to have a Cyclomatic Complexity less than or equal to 10 by Radon.'