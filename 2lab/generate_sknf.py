def generate_sknf(variables, truth_table):
    result = ""
    new_truth_table = []
    for rows in truth_table:
        if rows[-1] == 0:
            new_truth_table.append(rows)
    for rows in new_truth_table:
        if rows[-1] == 0:
            print("(", end="")
            result += "("
            for element in range(len(rows) - 1):
                if rows[element] == 1:
                    if variables[element] != variables[-1]:
                        print(f"!{variables[element]}", end="\/")
                        result += f"!{variables[element]}" + "\/"
                    else:
                        print(f"!{variables[element]}", end='')
                        result += f"!{variables[element]}"
                elif rows[element] == 0:
                    if variables[element] != variables[-1]:
                        print(variables[element], end="\/")
                        result += variables[element] + "\/"
                    else:
                        print(variables[element], end='')
                        result += variables[element]
            print(")", end='')
            result += ")"
            if rows != new_truth_table[-1]:
                print(f"/\\", end="")
                result += "/\\"
    return result
    
        
