from ..decorators import is_empty

class ArrayStack:
    '''LIFO stack implementation using a python list as storage'''

    def __init__(self):
        '''Create empty stack'''
        self._data = []
        self._size = 0

    def __len__(self):
        '''Return number of elements in stack.'''
        return self._size

    def push(self, e):
        '''Add element e to top of stack.'''
        self._data.append(e)
        self._size += 1

    @is_empty
    def top(self):
        '''Return but do not remove element at top of stack.

        Raise exception if stack is empty.
        '''
        return self._data[-1]

    @is_empty
    def pop(self):
        '''Remove and return the element from top of stack (LIFO)

        Raise Empty if stack is empty.
        '''
        self._size -= 1
        return self._data.pop()
