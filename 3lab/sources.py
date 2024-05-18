def truth_table(num_args):
    arguments = [False, True]
    table = []

    def generate_combinations(index, current):
        if index == num_args:
            table.append(tuple(current))
            return
        for arg in arguments:
            current[index] = arg
            generate_combinations(index + 1, current)

    generate_combinations(0, [None] * num_args)
    return table


def count_entries(constituents):
    entry = {}
    for i in range(len(constituents)):
        count = 0
        for j in range(len(constituents[i])):
            if constituents[i][j] == '   ✦    ':
                count += 1
        entry[i] = count
    return entry


def find_vars(implicant: str):
    variables = []
    for token in implicant:
        if token.isalpha():
            if token not in variables:
                variables.append(token)
    return variables
