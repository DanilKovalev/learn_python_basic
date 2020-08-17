import time
from enum import Enum


def perfomance_decorator(func):
    def _wrapper(*args, **kwargs):
        ts = time.time()
        result = func(*args, **kwargs)
        te = time.time()
        print(func.__name__, ":", te - ts)
        return result

    return _wrapper


@perfomance_decorator
def exponentiation(nums, times=2):
    result = list()
    for num in nums:
        result.append(num ** times)

    return result


def filter_even(number):
    return number % 2 == 0


def filter_odd(number):
    return not filter_even(number)


def filter_simple(number):
    # stupid alg
    is_prime = True
    d = 2
    while d * d <= number:
        if number % d == 0:
            return False
        d += 1

    return True


class FilterType(Enum):
    EVEN = filter_even
    ODD = filter_odd
    SIMPLE = filter_simple


@perfomance_decorator
def list_filter(nums, filter_type):
    return list(filter(filter_type, nums))



