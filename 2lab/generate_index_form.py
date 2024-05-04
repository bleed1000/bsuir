def generate_index_form(truth_table):
    index_form = []
    decimal = 0
    for rows in truth_table:
        index_form.append(rows[-1])
    for i, number in enumerate(index_form):
        decimal += number * (2 ** (len(index_form) - i - 1)) 
    return decimal