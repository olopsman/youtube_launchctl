import string
import random

def get_random_string(length):
    #Random string combination
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    print('random string =>' , result_str)

get_random_string(10)
