class Matrix:
    
    def __init__(self):
        self.row = 16
        self.column = 16
        self.matrix = self.__create_matrix()
        
    def __create_matrix(self):
        matrix = [
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
        [1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
        [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
        [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1],
        [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
        [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]]
        
        return matrix
    
    def load_element(self, row, column):
        return self.matrix[row][column]
    
    def change_element(self, row, column, value):
        self.matrix[row][column] = value
        
    def return_matrix(self):
        for row in self.matrix:
            for char in row:
                print(char, end = ' ')
            print()
            
    def word_from_matrix(self, index):
        word = ""
        for i in range(self.row):
            x = (index + i) % self.row
            word += str(self.matrix[x][index])
        return word
        
    def adres_row_from_matrix(self, index):
        row = ""
        for i in range(self.row):
            indx = (index + i) % self.row
            row += str(self.matrix[indx][i])
        return row
    
    def make_word(self, index, new_word):
        for i in range(self.column):
            self.matrix[i][index] = int(new_word[i])
            
    def locate_string_position(self, target_string, criteria):
        target_number = int(target_string, 2)
        print(target_number)

        smallest_value = float('inf')
        largest_value = float('-inf')
        smallest_index = -1
        largest_index = -1

        greater_found = False
        lesser_found = False

        for idx in range(16):
            matrix_string = self.word_from_matrix(idx)
            matrix_number = int(matrix_string, 2)
            print(matrix_number)

            if criteria and matrix_number > target_number:
                if matrix_number < smallest_value:
                    smallest_value = matrix_number
                    smallest_index = idx
                    greater_found = True
            elif not criteria and matrix_number < target_number:
                if matrix_number > largest_value:
                    largest_value = matrix_number
                    largest_index = idx
                    lesser_found = True

        if greater_found and smallest_index != -1:
            return smallest_index
        elif lesser_found and largest_index != -1:
            return largest_index

        return -1
    
    def conjuction(self, actor, actored):
        result = ""
        for i in range(len(actor)):
            if actor[i] == '1' and actored[i] == '1':
                result += "1"
            else:
                result += "0" 
        return result
    
    def not_conjuction(self, actor, actored):
        result = ""
        for i in range(len(actor)):
            if actor[i] == '1' and actored[i] == '1':
                result += "0"
            else:
                result += "1" 
        return result
    
    def act(self, actor, actored):
        return actor

    def not_act(self, actor, actored):
        result = ""
        for i in actor:
            if i == "1":
                result += "0"
            else:
                result += "1"
        return result
    
    def aggregate(self, identifier):
        combined_string = ""
        position = 0
        for row_index in range(self.row):
            matrix_word = self.word_from_matrix(row_index)
            if matrix_word[0:3] == identifier:
                combined_string += matrix_word + " "
                position = row_index
        
        if len(combined_string) > 16:
            combined_string = combined_string[0:16]
        
        prefix = combined_string[0:3]
        middle_a = combined_string[3:7]
        middle_b = combined_string[7:11]
        
        int_middle_a = int(middle_a, 2)
        int_middle_b = int(middle_b, 2)
        
        total = int_middle_a + int_middle_b
        
        binary_total = format(total, '05b')
        combined_string = prefix + middle_a + middle_b + binary_total
        self.make_word(position, combined_string)
        
        return combined_string