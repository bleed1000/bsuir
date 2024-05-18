import unittest
from Node import Node


class TestNode(unittest.TestCase):
    
    def setUp(self):
        # This method will run before each test
        self.node = Node("test_key", "test_info", 42, "0x123")

    def test_initialization(self):
        self.assertEqual(self.node.key_name, "test_key")
        self.assertEqual(self.node.information, "test_info")
        self.assertEqual(self.node.value, 42)
        self.assertIsNone(self.node.next)
        self.assertEqual(self.node.hash_address, "0x123")
    
    def test_next_node(self):
        next_node = Node("next_key", "next_info", 43, "0x456")
        self.node.next = next_node
        self.assertIs(self.node.next, next_node)
        self.assertEqual(self.node.next.key_name, "next_key")
        self.assertEqual(self.node.next.information, "next_info")
        self.assertEqual(self.node.next.value, 43)
        self.assertEqual(self.node.next.hash_address, "0x456")
    
if __name__ == '__main__':
    unittest.main()