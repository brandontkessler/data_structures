from ..decorators import is_empty


class CircularQueue:
    '''Queue implementation using circularly linked list'''

    class _Node:
        '''lightweight, nonpublic class for storing a singly linked node.'''
        __slots__ = '_element', '_next' # Prevent dynamic attribute creation (memory efficiency)

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        '''Create empty queue'''
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    @is_empty
    def first(self):
        head = self._tail._next
        return head._element

    @is_empty
    def dequeue(self):
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None # queue becomes empty
        else:
            self._tail._next = oldhead._next
        self._size -= 1

        return oldhead._element

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self._size == 0:
            newest._next = newest # refers to itself
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next    
