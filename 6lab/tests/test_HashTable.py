import unittest
from unittest.mock import patch
from HashTable import HashTable 
from io import StringIO

class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.ht = HashTable(5)
        self.q = 1

    def test_insert(self):
        self.ht.insert("абвоко", "info1", self.q)
        self.assertIsNotNone(self.ht.table[self.ht.get_hash_address(self.ht.get_numeric_value("абвоко"))])
        self.assertEqual(self.ht.table[self.ht.get_hash_address(self.ht.get_numeric_value("абвоко"))].information, "info1")

    def test_search(self):
        self.ht.insert("абвоко", "info1", self.q)
        self.ht.insert("гдеёжз", "info2", self.q)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.ht.search("абвоко")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, f"key_name: абвоко\n Hash-address: {1}\n number: 1\n collisium: 0\n info: info1")

    def test_remove(self):
        self.ht.insert("абвоко", "info1", self.q)
        self.ht.insert("гдеёжз", "info2", self.q)
        self.ht.remove("абвоко")
        self.assertIsNone(self.ht.table[self.ht.get_hash_address(self.ht.get_numeric_value("абвоко"))])
        self.assertIsNotNone(self.ht.table[self.ht.get_hash_address(self.ht.get_numeric_value("гдеёжз"))])
        
    def test_get_numeric_value(self):
        numeric_value = self.ht.get_numeric_value("абвоко")
        self.assertEqual(numeric_value, 1)  # 'а' -> 0, 'б' -> 1 => 0*33 + 1 = 1

    def test_show(self):
        # Создаем объект HashTable и добавляем некоторые элементы для отображения
        self.ht.insert("абвоко", "info1", self.q)
        self.ht.insert("гдеёжз", "info2", self.q)
        
        # Ожидаемый вывод
        expected_output = "Hash-address: 1 key_name: абвоко\nHash-address: 3 key_name: гдеёжз"
        
        # Создаем объект StringIO для перехвата вывода
        with patch('sys.stdout', new=StringIO()) as fake_out:
            # Вызываем метод show
            self.ht.show()
            # Получаем вывод
            output = fake_out.getvalue().strip()
            # Сравниваем вывод с ожидаемым результатом
            self.assertEqual(output, expected_output)
        

    def test_get_hash_address(self):
        value = self.ht.get_numeric_value("абвоко")
        hash_address = self.ht.get_hash_address(value)
        self.assertEqual(hash_address, value % self.ht.capacity)

    def test_collision_resolution(self):
        self.ht.insert("абвоко", "info1", self.q)
        self.ht.insert("абвоко", "info2", self.q)
        first_address = self.ht.get_hash_address(self.ht.get_numeric_value("абвоко"))
        second_address = (first_address + self.q) % self.ht.capacity
        self.assertIsNotNone(self.ht.table[first_address])
        self.assertIsNotNone(self.ht.table[second_address])
        self.assertEqual(self.ht.table[first_address].information, "info1")
        self.assertEqual(self.ht.table[second_address].information, "info2")
        

if __name__ == '__main__':
    unittest.main()
