from ..exception import Empty
from ..node import _Node

class LinkedStack:
    '''LIFO Stack implementation using singly linked list for storage'''

    def __init__(self):
        '''create an empty stack'''
        self._head = None # reference to head node
        self._size = 0 # number of stack elements

    def __len__(self):
        '''Return number of elements in stack'''
        return self._size

    def is_empty(self):
        '''Return true if stack is empty'''
        return self._size == 0

    def push(self, e):
        '''add element to top of stack'''
        self._head = _Node(e, self._head) # Create and link a new node
        self._size += 1

    def top(self):
        '''Return but not remove element at top of stack

        Raise Empty exception if stack is empty
        '''
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element # top of stack is at head of list

    def pop(self):
        '''Remove and return element from top of stack (LIFO)

        Raise Empty if stack is empty.
        '''
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
