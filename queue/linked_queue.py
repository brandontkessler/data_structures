from ..node import _Node
from ..decorator import is_empty

class LinkedQueue:
    '''FIFO queue implementation using linked list'''

    def __init__(self):
        '''create empty queue'''
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        '''Return number of elements in queue'''
        return self._size

    @is_empty
    def first(self):
        '''Return but not remove element at front of queue'''
        return self._head._element

    @is_empty
    def dequeue(self):
        '''Remove return first element of queue (FIFO)'''
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self._size == 0: # Special case if queue is empty
            self._tail = None
        return answer

    def enqueue(self, e):
        '''add element to back of queue'''
        newest = _Node(e, None) # node will point to none
        if self._size == 0:
            self._head = newest # special case
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
