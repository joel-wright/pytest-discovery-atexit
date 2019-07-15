import atexit

def foo_bar(x, y):
    return x + y


def run_me():
    print("I ran")


atexit.register(run_me)
