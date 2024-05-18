def is_subsequance(substring, string):
    i = 0
    for char in string:
        if i < len(string) and char == substring[i]:
            i += 1
    return i == len(substring)

def ras_tab_minimization(ans: str, sdnf: list, letters: dict, choice: str):
    if choice == "2":
        empty_matrix = [[0] * (len(sdnf) + 1) for _ in range(ans.count("|") + 2)]
    else:
        empty_matrix = [[0] * (len(sdnf) + 1) for _ in range(ans.count("&") + 2)]
    if choice == "2":
        for i, row in enumerate(sdnf):
            for index, el in enumerate(row):
                if el == "0":
                    sdnf[i][index] = f"!{letters[index]}"
                else:
                    sdnf[i][index] = letters[index]
    else:
        for i, row in enumerate(sdnf):
            for index, el in enumerate(row):
                if el == "0":
                    sdnf[i][index] = f"{letters[index]}"
                else:
                    sdnf[i][index] = f"!{letters[index]}"
    if choice == "2":
        ans_temp = ans.replace("&", "")
        ans_temp1 = ans_temp.replace("(", "")
        ans_temp2 = ans_temp1.replace(")", "")
        variatis = ans_temp2.split("|")
    else:
        ans_temp = ans.replace("|", "")
        ans_temp1 = ans_temp.replace("(", "")
        ans_temp2 = ans_temp1.replace(")", "")
        variatis = ans_temp2.split("&")
        
    for i in range(1, len(sdnf) + 1):
        empty_matrix[0][i] = ''.join(sdnf[i - 1]) 
    for i, row in enumerate(empty_matrix):
        if i == 0:
            continue
        empty_matrix[i][0] = variatis[i - 1]
        for index, el in enumerate(row):
            if index == 0:
                continue
            if len(variatis[i - 1]) > 2:
                temp = ""
                tempbool = True
                for el in variatis[i - 1]:
                    if el == "!":
                        temp += "!"
                        continue
                    temp += el
                    if "!" in temp:
                        if temp in empty_matrix[0][index]:
                            temp = ""
                            continue
                        else:
                            tempbool = False
                    if el in empty_matrix[0][index] and f"!{el}" not in empty_matrix[0][index]:
                        temp = ""      
                    else: 
                        tempbool = False  
                if tempbool is True:
                    empty_matrix[i][index] = "+"  
            elif variatis[i - 1] in empty_matrix[0][index] and f"!{variatis[i - 1]}" not in empty_matrix[0][index]:
                empty_matrix[i][index] = "+"
        
    for row in empty_matrix:
        for el in row:
            print(el, end="\t")
        print()
    
    print(ans)
    """ for row in empty_matrix:
        for index, el in empty_matrix:
            el = sdnf[index] """
                           
    