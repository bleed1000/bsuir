from opz import *
from generate_truth_table import generate_combinations
from generate_sdnf import generate_sdnf
from generate_sknf import generate_sknf
from generate_numeric_form import generate_number_form
from generate_index_form import generate_index_form

variables = set()
expression = input()
#expression = "(!(A | B ) > ( A ~ C )) > (( A & D ) ~ ( A ~ !B ))"
rpn_expression = infix_to_rpn(expression, variables)
variables = sorted(variables)
print(variables)
print(rpn_expression)
string_form = ""
truth_table = generate_combinations(len(variables))
result = (evaluate_rpn(rpn_expression, truth_table))
for i in range(len(result)):
    if result[i] is True:
        result[i] = 1
    elif result[i] is False:
        result[i] = 0
    string_form += str(result[i])
for variable in variables:
    print(variable, end=' ')
print("res")
for i, rows in enumerate(truth_table):
    rows.append(result[i])
    for element in rows:
        print(element, end=' ')
    print()
    
print("SDNF: ", end='')
generate_sdnf(variables, truth_table)
print("SKNF: ", end='')
generate_sknf(variables, truth_table)
print()

sknf_num_form, sdnf_num_form = generate_number_form(truth_table)
print("Number forms:")
print(tuple(sknf_num_form), f"/\\")
print(tuple(sdnf_num_form), f"\/")
index_fo = generate_index_form(truth_table)
print(f"Index form: {index_fo} - {string_form}")

