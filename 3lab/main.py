from transformation import *
from ras_tab_minim_sdnf import *
from karnough import generate_map_karnough
from copy import deepcopy
from minimization import *

used_indxs = []
letters = {0: "a",
        1: "b",
        2: "c",
        3: "d",
        4: "e",
        5: "f"}
print("1. Минимизация СКНФ")
print("2. Минимизация СДНФ")
choice = input("Выберите действие: ")
sdnf = []
if choice == "2":
    string = input("Введите СДНФ: ")
    minimized_sdnf = MinimizationDNF.minimize_dnf(string)
    print(minimized_sdnf)
    ans = minimized_sdnf
    temp_sdnf_list = transform_sdnf(string)
    new_list = deepcopy(temp_sdnf_list)
    ras_tab_minimization(minimized_sdnf, temp_sdnf_list, letters, choice)
    generate_map_karnough(new_list, ans, choice, letters)
elif choice == "1":
    string = input("Введите СКНФ: ")
    minimized_sknf = Minimization.minimize_sknf(string)
    print(minimized_sknf)
    print()
    temp_sdnf_list = transform_sknf(string)
    new_list = deepcopy(temp_sdnf_list)
    ras_tab_minimization(minimized_sknf, temp_sdnf_list, letters, choice)
    generate_map_karnough(new_list, minimized_sknf, choice, letters)
