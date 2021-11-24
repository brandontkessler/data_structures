from ..decorators import is_empty
from .doubly_linked_base import _DoublyLinkedBase
from ..position.position import Position

class PositionalList(_DoublyLinkedBase):

    def _validate(self, p):
        '''Return position's node, or raise appropriate error if invalid'''
        if not isinstance(p, Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node

    #------------- utility method ------------------
    def _make_position(self, node):
        '''Return Position instance for given node (or None if sentinel)'''
        if node is self._header or node is self._trailer:
            return None
        else:
            return Position(self, node)

    #--------------- accessors ---------------------
    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        '''Generate a forward iteration of elements of the list'''
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    #--------------- mutators ------------------
    # override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        '''Add element between existing nodes and return new Position'''
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        '''Replace element as Position p with e

        Return element formerly at position p.
        '''

        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value
