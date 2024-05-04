def generate_sdnf(variables, truth_table):
    result = ""
    new_truth_table = []
    for rows in truth_table:
        if rows[-1] == 1:
            new_truth_table.append(rows)
    print("(", end="")
    result += "("
    for rows in new_truth_table:
        if rows[-1] == 1:
            for element in range(len(rows) - 1):
                if rows[element] == 0:
                    print(f"!{variables[element]}", end="")
                    result += f"!{variables[element]}"
                elif rows[element] == 1:
                    print(variables[element], end="")
                    result += variables[element]
            if rows != new_truth_table[-1]:
                print("\/", end="")
                result += "\/"
    print(")")
    result += ")"
    return result
        
