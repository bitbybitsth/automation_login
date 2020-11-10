from functools import wraps
import time

def timer(func):   # name to be given for deorator and function as argument

    @wraps(func)# mandatory line to writtern above wrapper
    def wrapper(*args, **kwargs):  # wrapper function  must accept *args, **kwargs
        t1 = time.perf_counter()
        func(*args, **kwargs)       # there should be a call to original function or original function should be returned from warpper
        t2 = time.perf_counter()
        print("total time taken for addition to complete is: ", t2-t1)
    return wrapper

def slow_dwon_for_2secs(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        time.sleep(2)
        func(*args, **kwargs)
    return wrapper

@slow_dwon_for_2secs
def addition(n1, n2):
    print(n1+n2)

addition(10,20)

@timer
@slow_dwon_for_2secs
def division(dividen, divisor):
    """use for division"""
    print(dividen/divisor)

division()

div = division
# print(div.__doc__)
# print(div.__name__)

# division(10,5)
# division(20,5)


def repeat(func=None, num_times=2):
    """Run the decorated function the given number of times"""

    def decorator_repeat(func):
        @wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper_repeat

    if func is None:
        return decorator_repeat
    else:
        return decorator_repeat(func)


@repeat(num_times=10)
def display():
    print("***")

x = repeat(num_times=10)
@x
def display():
    print("############")


# @app.route("/edit", methods=["POST"])
# def edit_student():
#     pass

display()