class _NodeDoublyLinked:
    '''Lightweight, nonpublic class for doubly linked nodes'''
    __slots__ = '_element', '_prev', '_next'

    def __init__(self, element, prev, next):
        self._element = element
        self._prev = prev
        self._next = next
