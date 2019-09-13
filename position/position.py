class Position:
    '''an abstraction representing the location of a single element'''

    def __init__(self, container, node):
        '''constructor should not be invoked by user'''
        self._container = container
        self._node = node

    def element(self):
        return self._node._element

    def __eq__(self, other):
        '''return true if other is a position representing the same location'''
        return type(other) is type(self) and other._node is self._node

    def __ne__(self, other):
        '''return True if other does not represent the same location'''
        return not (self == other)

    
