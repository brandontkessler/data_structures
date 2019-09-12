from ..decorator import is_empty

class ArrayQueue:
    '''FIFO queue implementation using a python list as storage'''
    DEFAULT_CAPACITY = 10 # for initial capacity of queue

    def __init__(self):
        '''Create empty queue.'''
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0 # Index for front of queue

    def __len__(self):
        '''Return number of elements in queue.'''
        return self._size

    @is_empty
    def first(self):
        '''Return but not remove element at front of queue

        Raise Empty if queue is empty.
        '''
        return self._data[self._front]

    @is_empty
    def dequeue(self):
        '''Remove and return first element of queue (FIFO)

        Raise Empty if queue is empty.
        '''
        answer = self._data[self._front]
        self._data[self._front] = None # This is how we 'pop' from the queue
        self._front = (self._front + 1) % len(self._data) # set index to next val
        self._size -= 1
        return answer


    def enqueue(self, e):
        '''Add element to back of queue'''
        if self._size == len(self._data):
            self._resize(2 * len(self._data)) # Double size of array if capacity is full
        avail = (self._front + self._size) % len(self._data)
        # avail gets to next 'None' in queue which could be a wrap around back to index 0.
        # Ex. if capacity (len(self._data)) is 10, front is at 8 and size is 2, that means
        #   our list will be None for all except indexes 8 and 9 which are the last two
        #   places in the 10 cap list. (8 + 2) % 10 = 0 meaning it wraps back to the
        #   initial element in the list at 0.
        #   [None, None, ..., 'something', 'here'] will turn into:
        #   ['added', None, ..., 'something', 'here']
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        '''Resize to a new list of greater capacity'''
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk] # shift indeces back to 0
            walk = (1 + walk) % len(old)
        self._front = 0 # reset front since we shifted indeces to 0
