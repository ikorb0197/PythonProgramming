from time import time, sleep

# measure is a decorator
def measure(func):
    def wrapper(*args, **kwargs):
        t = time() # starting time
        func(*args, **kwargs) # function call
        print(func.__name__, "took:", time() - t)
    return wrapper

@measure
def f2(sleep_time = 0.1):
    sleep(sleep_time) # stops the execution on the given number of seconds

if __name__ == "__main__":
    print("HELLO")

# Practice
# Create a file: string_utils.py
# Contains a function make_palindrome(text) that takes a string and returns a palindrome by appending its reverse (eg, "abc" -> "abccba")


# Create file: main.py
# 1. Import string_utils
# 2. Import only make_palindrome