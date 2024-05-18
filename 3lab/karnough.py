from generate_comb import generate_combinations
from itertools import product
from copy import deepcopy

def generate_map_karnough(sdnf_f: list, ans: str, choice: str, letters: dict):
    if choice == "2":
        variaties = ans.split("\\/")
    else:
        temp_sdnf_f = deepcopy(sdnf_f)
        sdnf_f = []
        truth_table = generate_combinations(len(temp_sdnf_f[0]))
        for row in truth_table:
            row_strs = list(map(str, row))
            if row_strs not in temp_sdnf_f:
                sdnf_f.append(row)
        variaties = ans.split("/\\")
        
    temp_variaties = []
    for index, el in enumerate(variaties):
        #temp_variaties.append([])
        temp_str = ""
        for char in el:
            if char == "!":
                continue
            temp_str += char
        temp_variaties.append(temp_str)
        
    temp_zero_row_col = []
    for row in sdnf_f:
        for index, el in enumerate(row):
            temp_zero_row_col.append(letters[index])
        break
    
    temp_variaties = []
    
    temp_variaties.append([])
    temp_variaties.append([])
    temp_variaties[0] = "a"
    temp_variaties[1] = "bc"
    
    empty_matrix = [[0] * (len(temp_variaties[1]) ** 2 + 1)  for _ in range(len(temp_variaties) + 1)]
    empty_matrix[0][0] = temp_variaties[0] + "/" + temp_variaties[1]
    
    comb_gen_for_row = generate_combinations(len(temp_variaties[1]))
    comb_gen_for_row[2], comb_gen_for_row[3] = comb_gen_for_row[3], comb_gen_for_row[2]
    comb_gen_for_col = generate_combinations(len(temp_variaties[0]))
    
    for index, row in enumerate(empty_matrix):
        for index_el, el in enumerate(row):
            if index == 0 and index_el > 0:
                res = ""
                for char in comb_gen_for_row[index_el - 1]:
                    res += str(char)
                empty_matrix[index][index_el] = res
            if index > 0 and index_el == 0:
                res = ""
                for char in comb_gen_for_col[index - 1]:
                    res += str(char)
                empty_matrix[index][index_el] = res
    
    new_sdnf = []
    for row in sdnf_f:
        temp = ""
        for el in row:
            temp += str(el)
        new_sdnf.append(temp)
        temp = ""
        
    print()
    
    for index, row in enumerate(empty_matrix):
        for index_el, el in enumerate(row):
            if index == 0 or index_el == 0:
                continue
            temp = str(empty_matrix[index][0]) + str(empty_matrix[0][index_el])
            if temp in new_sdnf:
                empty_matrix[index][index_el] = "1"
    
    
    for row in empty_matrix:
        for el in row:
            print(el, end="\t")
        print()
                
        print()
        
    variables = [0, 1]
    combinations = list(product(variables, repeat=2))
    
    # Создаем матрицу Пайопа
    pion_matrix = [[boolean_function(a, b) for a, b in combinations]]   
        
    for i in range(len(pion_matrix)):
        row = []
        for j in range(len(pion_matrix[i])):
            neighbors = [(i, j)]
            if j+1 < len(pion_matrix[i]):
                neighbors.append((i, j+1))
            if i+1 < len(pion_matrix):
                neighbors.append((i+1, j))
            if i+1 < len(pion_matrix) and j+1 < len(pion_matrix[i]):
                neighbors.append((i+1, j+1))
            
            if all(pion_matrix[x][y] == pion_matrix[i][j] for x, y in neighbors):
                row.append(pion_matrix[i][j])
            else:
                row.append(None)
    
    print(ans)
    


def boolean_function(a, b):
    return a and b