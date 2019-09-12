from ..exception import Empty

class ArrayStack:
    '''LIFO stack implementation using a python list as storage'''

    def __init__(self):
        '''Create empty stack'''
        self._data = []

    def __len__(self):
        '''Return number of elements in stack.'''
        return len(self._data)

    def is_empty(self):
        '''Return True if stack is empty'''
        return len(self._data) == 0

    def push(self, e):
        '''Add element e to top of stack.'''
        self._data.append(e)

    def top(self):
        '''Return but do not remove element at top of stack.

        Raise exception if stack is empty.
        '''
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        '''Remove and return the element from top of stack (LIFO)

        Raise Empty if stack is empty.
        '''
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()
