# read all files except "__init__.py" in testcases directory
# and convert them to json format

import re
import os
import json



def replace_pattern(test):
    pattern = r"import inspect\nfrom radon.visitors import ComplexityVisitor\nresult = ComplexityVisitor.from_code\(inspect.getsource\([a-zA-Z0-9_]+\)\)"

    replacement = """\
from radon.visitors import ComplexityVisitor
result = ComplexityVisitor.from_code(${candidate})"""

    return re.sub(pattern, replacement, test)


def to_json():
    testcases = []
    for filename in os.listdir("testcases"):
        if filename.endswith(".py") and not filename.startswith("__"):
            with open("testcases/" + filename) as f:
                id = filename[:-3].replace("_", "/")
                test = f.read()

                # remove first line of test
                test = test[test.find("\n") + 1 :]

                # replace pattern
                test = replace_pattern(test)

                testcases.append({"id": id, "test": test})

    with open("humaneval_nf.json", "w") as f:
        json.dump(testcases, f, indent=4)


if __name__ == "__main__":
    to_json()
