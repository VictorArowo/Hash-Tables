# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        hash_value = self._hash_mod(key)
        if not self.storage[hash_value]:
            self.storage[hash_value] = LinkedPair(key, value)
        else:
            current_node = self.storage[hash_value]
            while current_node:
                if current_node.key == key:
                    current_node.value = value
                    break
                elif current_node.next:
                    current_node = current_node.next
                else:
                    break
            current_node.next = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hash_value = self._hash_mod(key)

        if not self.storage[hash_value]:
            print('key doesn\'t exist')
            return

        previous_node = None
        current_node = self.storage[hash_value]
        next_node = current_node.next

        searching = True

        while searching:
            if current_node.key == key:
                if not previous_node:
                    self.storage[hash_value] = next_node
                    searching = False

                elif previous_node and not next_node:
                    previous_node.next = None
                    searching = False

            elif current_node.next:
                previous_node = current_node
                current_node = next_node
                next_node = current_node.next

            else:
                print('key doesn\'t exist')
                searching = False

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hash_value = self._hash_mod(key)
        if not self.storage[hash_value]:
            return None
        curr_node = self.storage[hash_value]
        while True:
            if curr_node.key == key:
                return curr_node.value
            elif curr_node.next != None:
                curr_node = curr_node.next
            else:
                return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        new_storage = HashTable(self.capacity * 2)

        for i in range(self.capacity):
            curr_node = self.storage[i]

            while curr_node is not None:
                new_storage.insert(curr_node.key, curr_node.value)
                curr_node = curr_node.next
        self.storage = new_storage.storage
        self.capacity = new_storage.capacity


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
