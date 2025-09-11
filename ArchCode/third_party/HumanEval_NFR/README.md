# HumanEval_NF

### Prerequisite

- Install python packages.

```commandline
$ pip install -r requirements.txt
```

### How to run test case
```commandline
$ python run.py <id> 
```

#### Example
```commandline
$ python run.py 0
Traceback (most recent call last):
  File "/Users/jaeseok/git/HumanEval_NF/run.py", line 9, in <module>
    new_module = __import__(f"testcases.HumanEval_{id}")
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/jaeseok/git/HumanEval_NF/testcases/HumanEval_0.py", line 18, in <module>
    assert has_close_elements([1.0, 1.0, 1.0, 1.0], 0.5) == False, 'Failed to handle case where all numbers in the list are the same.'
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Failed to handle case where all numbers in the list are the same.
```
