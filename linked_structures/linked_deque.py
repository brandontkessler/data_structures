from .doubly_linked_base import _DoublyLinkedBase
from ..decorators import is_empty

class LinkedDeque(_DoublyLinkedBase):
    '''Double-ended queue implementation based on a doubly linked list'''

    @is_empty
    def first(self):
        return self._header._next._element

    @is_empty
    def last(self):
        return self._trailer._prev._element

    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)

    @is_empty
    def delete_first(self):
        return self._delete_node(self._header._next)

    @is_empty
    def delete_last(self):
        return self._delete_node(self._trailer._prev)
