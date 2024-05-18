from sources import find_vars
from sources import count_entries


class Minimization:

    @classmethod
    def minimize_sknf(cls, sknf):
        sknf_clear = sknf.replace(' ', '').replace('|', '')
        sknf_list = sknf_clear.split('&')
        old_sknf = sknf_list.copy()
        sknf_list = cls._gluing(sknf_list)
        dead_end_sknf = cls._dead_end(old_sknf, sknf_list)
        sknf_str = cls._customize_min_sknf(dead_end_sknf)
        return sknf_str

    @classmethod
    def _gluing(cls, snf_list):
        minimize_list = []
        transformed_brackets = []
        while True:
            minimize_list.clear()
            transformed_brackets.clear()
            for index1, term1 in enumerate(snf_list):
                for index2, term2 in enumerate(snf_list):
                    if find_vars(term1) == find_vars(term2) and term1 != term2:
                        buffer = 0
                        index = 0
                        for i in range(len(term1)):
                            for j in range(len(term2)):
                                if term1[i] == term2[j] and term1[i].isalpha():
                                    if term1[i - 1] != term2[j - 1]:
                                        if term1[i - 1] == '!' or term2[j - 1] == '!':
                                            # Handle negated variables
                                            if term1[i - 1] == '!':
                                                new_term1 = term1[:i - 1] + term1[i + 1:]
                                            else:
                                                new_term1 = term1
                                            if term2[j - 1] == '!':
                                                new_term2 = term2[:j - 1] + term2[j + 1:]
                                            else:
                                                new_term2 = term2
                                        else:
                                            # No negation
                                            new_term1 = term1.replace(term1[i], '')
                                            new_term2 = term2.replace(term2[j], '')
                                        buffer += 1
                                        index = i
                        if buffer == 1:
                            if index1 not in transformed_brackets and index2 not in transformed_brackets:
                                transformed_brackets.append(index2)
                                transformed_brackets.append(index1)
                            if new_term1 not in minimize_list:
                                minimize_list.append(new_term1)
            if not minimize_list:
                break
            else:
                for i in range(len(snf_list)):
                    if i not in transformed_brackets:
                        minimize_list.append(snf_list[i])
                snf_list = minimize_list.copy()
        return snf_list

    @classmethod
    def _customize_min_sknf(cls, min_sknf: list):
        min_sknf_str = ''
        index_c = 0
        for item in min_sknf:
            min_sknf_str += item + '&'
        variables = ['a', 'b', 'c']
        for index, token in enumerate(min_sknf_str):
            if token in variables and min_sknf_str[index_c + 1] != ')':
                min_sknf_str = min_sknf_str[:index_c + 1] + '|' + min_sknf_str[index_c + 1:]
                index_c += 1
            index_c += 1
        min_sknf_str = min_sknf_str[:-1]
        return min_sknf_str

    @classmethod
    def _dead_end(cls, snf: list, min_snf: list):
        new_min_sknf = []
        constituents = cls.build_table(snf, min_snf)
        entry = count_entries(constituents)
        transposed_constituents = [list(row) for row in zip(*constituents)]
        uses = []
        for k in range(len(transposed_constituents)):
            count = 0
            uses.clear()
            for g in range(len(transposed_constituents[k])):
                if transposed_constituents[k][g] == '   ✦    ':
                    count += 1
                    uses.append(g)
            if count == 1:
                if min_snf[uses[0]] not in new_min_sknf:
                    new_min_sknf.append(min_snf[uses[0]])
            if count >= 2:
                flag = True
                for use in uses:
                    if min_snf[use] in new_min_sknf:
                        flag = False
                if flag:
                    if not all(entry[uses[0]] == entry[use] for use in uses):
                        max_entry = uses[0]
                        for use in uses:
                            if entry[max_entry] < entry[use]:
                                max_entry = use
                        new_min_sknf.append(min_snf[max_entry])
                    else:
                        temporary_snf = []
                        for use in uses:
                            temporary_snf.append(len(find_vars(min_snf[use])))
                        if not all(len(find_vars(min_snf[use2])) == len(find_vars(min_snf[0])) for use2 in uses):
                            min_use = uses[temporary_snf.index(min(temporary_snf))]
                            new_min_sknf.append(min_snf[min_use])
        return new_min_sknf

    @classmethod
    def build_table(cls, snf: list, min_snf: list):
        constituents: list[list[str]] = [['        '] * len(snf) for i in range(len(min_snf))]
        for index1, term1 in enumerate(min_snf):
            for index2, term2 in enumerate(snf):
                flag = True
                for i in range(len(term1)):
                    for j in range(len(term2)):
                        if term1[i] == term2[j] and term1[i].isalpha():
                            if term1[i - 1] != term2[j - 1]:
                                if term1[i - 1] == '!' or term2[j - 1] == '!':
                                    flag = False
                if flag:
                    constituents[index1][index2] = '   ✦    '
        return constituents
    

class MinimizationDNF:

    @classmethod
    def minimize_dnf(cls, dnf):
        dnf_clear = dnf.replace(' ', '').replace('&', '')
        dnf_list = dnf_clear.split('|')
        old_dnf = dnf_list.copy()
        dnf_list = cls._gluing(dnf_list)
        dead_end_dnf = cls._dead_end(old_dnf, dnf_list)
        dnf_str = cls._customize_min_dnf(dead_end_dnf)
        return dnf_str

    @classmethod
    def _gluing(cls, dnf_list):
        minimize_list = []
        transformed_brackets = []
        while True:
            minimize_list.clear()
            transformed_brackets.clear()
            for index1, term1 in enumerate(dnf_list):
                for index2, term2 in enumerate(dnf_list):
                    if find_vars(term1) == find_vars(term2) and term1 != term2:
                        buffer = 0
                        index = 0
                        for i in range(len(term1)):
                            for j in range(len(term2)):
                                if term1[i] == term2[j] and term1[i].isalpha():
                                    if term1[i - 1] != term2[j - 1]:
                                        if term1[i - 1] == '!' or term2[j - 1] == '!':
                                            # Handle negated variables
                                            if term1[i - 1] == '!':
                                                new_term1 = term1[:i - 1] + term1[i + 1:]
                                            else:
                                                new_term1 = term1
                                            if term2[j - 1] == '!':
                                                new_term2 = term2[:j - 1] + term2[j + 1:]
                                            else:
                                                new_term2 = term2
                                        else:
                                            # No negation
                                            new_term1 = term1.replace(term1[i], '')
                                            new_term2 = term2.replace(term2[j], '')
                                        buffer += 1
                                        index = i
                        if buffer == 1:
                            if index1 not in transformed_brackets and index2 not in transformed_brackets:
                                transformed_brackets.append(index2)
                                transformed_brackets.append(index1)
                            if new_term1 not in minimize_list:
                                minimize_list.append(new_term1)
            if not minimize_list:
                break
            else:
                for i in range(len(dnf_list)):
                    if i not in transformed_brackets:
                        minimize_list.append(dnf_list[i])
                dnf_list = minimize_list.copy()
        return dnf_list

    @classmethod
    def _customize_min_dnf(cls, min_dnf: list):
        min_dnf_str = ''
        index_c = 0
        for item in min_dnf:
            min_dnf_str += item + '|'
        variables = ['a', 'b', 'c']
        for index, token in enumerate(min_dnf_str):
            if token in variables and min_dnf_str[index_c + 1] != ')':
                min_dnf_str = min_dnf_str[:index_c + 1] + '&' + min_dnf_str[index_c + 1:]
                index_c += 1
            index_c += 1
        min_dnf_str = min_dnf_str[:-1]
        return min_dnf_str

    @classmethod
    def _dead_end(cls, dnf: list, min_dnf: list):
        new_min_dnf = []
        constituents = cls.build_table(dnf, min_dnf)
        entry = count_entries(constituents)
        transposed_constituents = [list(row) for row in zip(*constituents)]
        uses = []
        for k in range(len(transposed_constituents)):
            count = 0
            uses.clear()
            for g in range(len(transposed_constituents[k])):
                if transposed_constituents[k][g] == '   ✦    ':
                    count += 1
                    uses.append(g)
            if count == 1:
                if min_dnf[uses[0]] not in new_min_dnf:
                    new_min_dnf.append(min_dnf[uses[0]])
            if count >= 2:
                flag = True
                for use in uses:
                    if min_dnf[use] in new_min_dnf:
                        flag = False
                if flag:
                    if not all(entry[uses[0]] == entry[use] for use in uses):
                        max_entry = uses[0]
                        for use in uses:
                            if entry[max_entry] < entry[use]:
                                max_entry = use
                        new_min_dnf.append(min_dnf[max_entry])
                    else:
                        temporary_dnf = []
                        for use in uses:
                            temporary_dnf.append(len(find_vars(min_dnf[use])))
                        if not all(len(find_vars(min_dnf[use2])) == len(find_vars(min_dnf[0])) for use2 in uses):
                            min_use = uses[temporary_dnf.index(min(temporary_dnf))]
                            new_min_dnf.append(min_dnf[min_use])
        return new_min_dnf

    @classmethod
    def build_table(cls, dnf: list, min_dnf: list):
        constituents: list[list[str]] = [['        '] * len(dnf) for i in range(len(min_dnf))]
        for index1, term1 in enumerate(min_dnf):
            for index2, term2 in enumerate(dnf):
                flag = True
                for i in range(len(term1)):
                    for j in range(len(term2)):
                        if term1[i] == term2[j] and term1[i].isalpha():
                            if term1[i - 1] != term2[j - 1]:
                                if term1[i - 1] == '!' or term2[j - 1] == '!':
                                    flag = False
                if flag:
                    constituents[index1][index2] = '   ✦    '
        return constituents