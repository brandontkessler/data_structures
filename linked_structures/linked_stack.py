from ..decorators import is_empty
from ..nodes import _Node

class LinkedStack:
    '''LIFO Stack implementation using singly linked list for storage'''

    def __init__(self):
        '''create an empty stack'''
        self._head = None # reference to head node
        self._size = 0 # number of stack elements

    def __len__(self):
        '''Return number of elements in stack'''
        return self._size

    def push(self, e):
        '''add element to top of stack'''
        self._head = _Node(e, self._head) # Create and link a new node
        self._size += 1

    @is_empty
    def top(self):
        '''Return but not remove element at top of stack

        Raise Empty exception if stack is empty
        '''
        return self._head._element # top of stack is at head of list

    @is_empty
    def pop(self):
        '''Remove and return element from top of stack (LIFO)

        Raise Empty if stack is empty.
        '''
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
