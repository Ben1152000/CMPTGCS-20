
# Use this function to submit your answers:
#   Usage: submit(<problem#>, <answer>)
import hashlib
def submit(problem, answer):
    b = hashlib.sha224(bytes(f"{problem}:{answer}", 'utf-8')).hexdigest()
    if b in ["2ecfe8897c3fd00ed90d0ffb8841b8c79e97acdaf940fc60e206f1e6", 
        "5d642adf4066d1248dbde7f2988f4662a75c0728e4904fe0e1bd775f",
        "e036540aed9e15c7662ba1d93df1ae219c38a2abb492bd4e867772ea",
        "64ba22e77acc1f8ddd05b8c0123d0396580dd91974e7678a792e016b",
        "7ebe1075385ba7fd75d86212beede93b1b8ff444fcc7994a8f4ff69c"]: 
        print(f"The answer to problem #{problem} is correct.")
    else: print(f"The answer to problem #{problem} is incorrect.")

def hashed(problem, answer):
    print(hashlib.sha224(bytes(f"{problem}:{answer}", 'utf-8')).hexdigest())
