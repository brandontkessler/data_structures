class _Node:
        __slots__ = '_element', '_prev', '_next'
        def __init__(self, e, prev, next):
            self._element = e
            self._prev = prev
            self._next = next

class _DoublyLinkedBase:
    def __init__(self):
        self._header = _Node(None, None, None)
        self._trailer = _Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = _Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    
    def _delete_node(self, node):
        node._prev._next = node._next
        node._next._prev = node._prev
        self._size -= 1
        e = node._element
        node._prev = node._next = node._element = None # deprecate
        return e