from .nodes import _NodeDoublyLinked
from ..decorators import is_empty

class _DoublyLinkedBase:
    def __init__(self):
        self._header = _NodeDoublyLinked(None, None, None) # left edge
        self._trailer = _NodeDoublyLinked(None, None, None) # right edge
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def _insert_between(self, e, predecessor, successor):
        newest = _NodeDoublyLinked(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None # deprecate node
        return element
