from solutions.HumanEval_118 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The closest vowel that stands between two consonants from the right side is "u"
assert get_closest_vowel("yogurt") == "u", 'Failed to find the closest vowel.'

### The closest vowel that stands between two consonants from the right side is "U"
assert get_closest_vowel("FULL") == "U", 'Failed to find the closest vowel when the word contains uppercase letters.'

### There is no vowel that satisfies the condition, so the function should return an empty string
assert get_closest_vowel("quick") == "", 'Failed to handle case where no vowel satisfies the condition.'

### There is no vowel that satisfies the condition, so the function should return an empty string
assert get_closest_vowel("apple") == "", 'Failed to handle case where the word contains only one vowel.'

### The word contains only two characters, neither of which is a vowel, so the function should return an empty string
assert get_closest_vowel("ab") == "", 'Failed to handle case where the word contains only two characters.'

## Edge Cases
### The word is empty, so the function should return an empty string
assert get_closest_vowel("") == "", 'Failed to handle an empty word.'

### The word contains only one vowel, which is at the end of the word, so the function should return an empty string
assert get_closest_vowel("she") == "", 'Failed to handle case where only one vowel is placed at the end.'

### The word contains only one vowel, which is at the beginning of the word, so the function should return an empty string
assert get_closest_vowel("ant") == "", 'Failed to handle case where only one vowel is placed at the beginning.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The word contains 10^6 characters, all of which are consonants
### There is no vowel that satisfies the condition, so the function should return an empty string
assert get_closest_vowel("z" * 10**6) == "", 'Failed to handle large input size.'

### The word contains 10^6 characters, all of which are vowels
### There is no consonant that satisfies the condition, so the function should return an empty string
assert get_closest_vowel("a" * 10**6) == "", 'Failed to handle large input size.'

### The word contains 10^6 characters
assert get_closest_vowel("bab" + "c" * (10**6 - 3)) == "a", 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The word input is not a string, so the function should handle the case not to raise error
assert not get_closest_vowel(1234), 'Failed to handle case where the input word is not a string.'

#### The word contains non-English letters, so the function should handle the case not to raise error
assert not get_closest_vowel("こんにちは"), 'Failed to handle case where the word contains non-English letters.'

### Reliability
#### Satisfied if no errors occur across all test cases

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 10
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(get_closest_vowel))
assert result.total_complexity <= 10, 'Failed to have a Cyclomatic Complexity less than or equal to 10 by Radon.'