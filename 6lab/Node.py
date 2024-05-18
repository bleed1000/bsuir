class Node:
    def __init__(self, key_name, information, value, hash_address):
        self.information = information
        self.key_name = key_name
        self.value = value
        self.next = None
        self.hash_address = hash_address
        
        