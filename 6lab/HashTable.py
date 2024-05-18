from Node import Node

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity
        print(self.table)

    def _hash(self, key):
        return hash(key) % self.capacity

    def get_numeric_value(self, key_name):
        a = ord('а')
        alphabet = ''.join([chr(i) for i in range(a, a + 32)])
        alphabet = list(alphabet)
        return alphabet.index(key_name[0].lower()) * 33 + alphabet.index(key_name[1].lower())

    def get_hash_address(self, value):
        result = value % self.capacity
        return result

    def show(self):
        for i in range(len(self.table)):
            if self.table[i] is not None:
                print(f'Hash-address: {i} key_name: {self.table[i].key_name}')

    def insert(self, key_name, information, q):
        value = self.get_numeric_value(key_name)
        hash_address = self.get_hash_address(value)
        i = 1
        temp_hash_address = hash_address
        while self.table[hash_address] is not None:
            hash_address = (temp_hash_address + (i * q)) % self.capacity
            i += 1
        self.table[hash_address] = Node(key_name, information, value, hash_address)
        self.size += 1

    def search(self, key_name):
        for i in range(len(self.table)):
            if self.table[i] is not None:
                if self.table[i].key_name == key_name:
                    print(
                        f' key_name: {self.table[i].key_name}\n Hash-address: {self.table[i].hash_address}\n number: {self.table[i].value}\n collisium: {1 if self.table[i].next is not None else 0}\n info: {self.table[i].information}')
                    return
                elif self.table[i].next is not None:
                    current = self.table[i]
                    while True:
                        if current.key_name == key_name:
                            print(
                                f' key_name: {current.key_name}\n Hash-address: {current.hash_address}\n number: {current.value}\n collisium: 1\n info: {current.information}')
                            return
                        elif current.next is None:
                            break
                        else:
                            current = current.next

    def remove(self, key_name):
        for i in range(len(self.table)):
            if self.table[i] is not None:
                if self.table[i].key_name == key_name:
                    if self.table[i].next is not None:
                        self.table[i] = self.table[i].next
                        return
                    else:
                        self.table[i] = None
                        return
                else:
                    if self.table[i].next is not None:
                        previous = None
                        current = self.table[i]
                        while current:
                            if current.key_name == key_name:
                                previous.next = current.next
                                self.size -= 1
                                return
                            elif current.next is None:
                                break
                            else:
                                previous = current
                                current = current.next
