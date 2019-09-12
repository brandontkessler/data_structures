from functools import wraps

from ..exception import Empty

def is_empty(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args[0]._size == 0:
             raise Empty('Data storage is empty')
        return func(*args, **kwargs)
    return wrapper
