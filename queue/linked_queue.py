from ..exception import Empty
from ..node import _Node

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

    def is_empty(self):
        '''Return True if queue is empty'''
        return self._size == 0

    def first(self):
        '''Return but not remove element at front of queue'''
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element

    def dequeue(self):
        '''Remove return first element of queue (FIFO)'''
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty(): # Special case if queue is empty
            self._tail = None
        return answer

    def enqueue(self, e):
        '''add element to back of queue'''
        newest = _Node(e, None) # node will point to none
        if self.is_empty():
            self._head = newest # special case
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
