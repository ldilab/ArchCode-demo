import argparse

parser = argparse.ArgumentParser()
parser.add_argument('id')

args = parser.parse_args()
id = args.id

new_module = __import__(f"testcases.HumanEval_{id}")
