import string
import random

def gen_random_string():
    "string of len 8 and it should contain alphabel and num"

    # print(random.choice(string.ascii_letters+string.digits))
    l1=[]
    for i in range(8):
        l1.append(random.choice(string.ascii_letters + string.digits))
    # print(l1)
    return "".join(l1)

# gen_random_string()