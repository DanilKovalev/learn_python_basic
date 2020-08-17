from functools import wraps


def print_indent(indent, times):
    for i in range(0, times):
        print(indent, end='')

    print(end=' ')


def decorator_factory(indent):
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


@decorator_factory("___")
def fib(n):
    cur = 1
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)


fib(3)
