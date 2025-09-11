from solutions.HumanEval_66 import *
# Test Cases Regarding Functional Requirements
## General Cases
### The input string is empty, so the function should return 0
assert digitSum("") == 0, 'Failed to handle an empty input string.'

### The sum of the ASCII codes of the uppercase characters in "abAB" is 131
assert digitSum("abAB") == 131, 'Failed to calculate the sum of ASCII codes of the uppercase characters.'

### The sum of the ASCII codes of the uppercase characters in "abcCd" is 67
assert digitSum("abcCd") == 67, 'Failed to calculate the sum of ASCII codes of the uppercase characters.'

### The sum of the ASCII codes of the uppercase characters in "helloE" is 69
assert digitSum("helloE") == 69, 'Failed to calculate the sum of ASCII codes of the uppercase characters.'

### The sum of the ASCII codes of the uppercase characters in "woArBld" is 131
assert digitSum("woArBld") == 131, 'Failed to calculate the sum of ASCII codes of the uppercase characters.'

### The sum of the ASCII codes of the uppercase characters in "aAaaaXa" is 153
assert digitSum("aAaaaXa") == 153, 'Failed to calculate the sum of ASCII codes of the uppercase characters.'

## Edge Cases
### The input string contains only lowercase characters, so the function should return 0
assert digitSum("abcd") == 0, 'Failed to handle case where there are no uppercase characters in the input string.'

### The input string contains only uppercase characters, so the function should return the sum of their ASCII codes
assert digitSum("ABC") == 198, 'Failed to calculate the sum of ASCII codes of the uppercase characters.'

# Test Cases Regarding Non-functional Requirements
## Performance Requirements
### The input string contains 10^6 uppercase characters
### The sum of the ASCII codes of the uppercase characters in the input string should be 65*10^6
assert digitSum("A" * 10**6) == 65 * 10**6, 'Failed to handle large input size.'

## Specific Quality Requirements
### Robustness
#### The input is not a string, so the function should handle the case not to raise error
assert not digitSum(123), 'Failed to handle case where the input is not a string.'

#### The input string contains invalid characters, so the function should ignore them
assert digitSum("A@B*C") == 198, 'Failed to handle case where the input string contains invalid characters.'

### Maintainability
#### Calculate Cyclomatic Complexity using Radon
#### Check if the Cyclomatic Complexity is less than or equal to 5
import inspect
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(inspect.getsource(digitSum))
assert result.total_complexity <= 5, 'Failed to have a Cyclomatic Complexity less than or equal to 5 by Radon.'
