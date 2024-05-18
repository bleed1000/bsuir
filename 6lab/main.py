from HashTable import HashTable

if __name__ == '__main__':
    numbers = ''
    ht = HashTable(5)
    q = int(input("Введите шаг для разрешения колизии с помощью линейного поиска: "))
    ht.insert("абвоко", 3, q)
    ht.insert("абвоко", 2, q)
    ht.insert("абвоко", 5, q)

    ht.show()
    while True:
        print("\nOptions:\n 1) Adding\n 2) Searching\n 3) Deleting\n 4) Table view\n 5) Exit")
        key = input("Choose option:")
        if key == "1":
            name = input("Enter key name: ")
            info = input("Enter info: ")
            if name[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                print('Only words can be used')
            else:
                ht.insert(name, info, q)
        elif key == "2":
            info = input("Enter key_name for search: ")
            ht.search(info)
        elif key == "3":
            info = input("Enter key_name to delete: ")
            ht.remove(info)
        elif key == "4":
            ht.show()
        elif key == "5":
            break