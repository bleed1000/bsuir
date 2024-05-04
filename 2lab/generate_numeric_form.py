def generate_number_form(truth_table):
    sdnf_num_form = []
    sknf_num_form = []
    for i, rows in enumerate(truth_table):
        if rows[-1] == 0:
            sknf_num_form.append(i)
        elif rows[-1] == 1:
            sdnf_num_form.append(i)
    return sknf_num_form, sdnf_num_form