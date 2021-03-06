from functools import wraps


def print_indent(indent, times):
    for i in range(0, times):
        print(indent, end='')

    print(end=' ')


def trace_decorator(indent):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            print_indent(indent, wrapper._depth)

            print("-->", function.__name__, "(", *args, ")", sep='')

            wrapper._depth += 1
            result = function(*args, **kwargs)
            wrapper._depth -= 1

            print_indent(indent, wrapper._depth)
            print("<--", function.__name__, "(", *args, ") == ", result, sep='')
            return result

        wrapper._depth = 0
        return wrapper

    return decorator


@trace_decorator("___")
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


fib(3)
