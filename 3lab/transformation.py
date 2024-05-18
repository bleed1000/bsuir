def transform(sdnf: list):
    while True:
        extension = input()
        if extension == "":
            return sdnf
        new_extension = []
        skip_next = False
        for i in range(len(extension)):
            if skip_next:
                skip_next = False
                continue
            if extension[i] == "!":
                new_extension.append("0")
                skip_next = True
            else:
                new_extension.append("1")
        sdnf.append(new_extension)
        
def transform_sknf(sdnf: str):
    result = []
    temp = sdnf.replace("|", "")
    new_temp = temp.replace("&", " ")
    ans = new_temp.split()
    for row in ans:
        temp_res = []
        skip_next = False
        for c in row:
            if skip_next:
                skip_next = False
                continue
            if c == "(" or c == ")":
                continue
            elif c == "!":
                temp_res.append("1")
                skip_next = True
            else:
                temp_res.append("0")
        result.append(temp_res)
    return result

def transform_sdnf(sdnf: str):
    result = []
    temp = sdnf.replace("|", " ")
    ans = temp.split()
    for row in ans:
        temp_res = []
        skip_next = False
        for c in row:
            if skip_next:
                skip_next = False
                continue
            if c == "(" or c == ")":
                continue
            elif c == "!":
                temp_res.append("0")
                skip_next = True
            else:
                temp_res.append("1")
        result.append(temp_res)
    return result
            
            
