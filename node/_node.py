class _Node:
    '''lightweight, nonpublic class for storing a singly linked node.'''
    __slots__ = '_element', '_next' # Prevent dynamic attribute creation (memory efficiency)

    def __init__(self, element, next):
        self._element = element
        self._next = next
