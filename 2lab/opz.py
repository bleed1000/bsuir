def infix_to_rpn(expression, variables : set):
    priority = {"!": 4, "&": 3, "|": 2, "~": 2, ">": 1}

    def greater_priority(op1, op2):
        return priority[op1] > priority[op2]

    output = []
    operator_stack = []

    expression = expression.replace(" ", "")

    for token in expression:
        if token.isalpha():
            output.append(token)
            variables.add(token)
        elif token in priority:
            while operator_stack and operator_stack[-1] != "(" and greater_priority(operator_stack[-1], token):
                output.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == "(":
            operator_stack.append(token)
        elif token == ")":
            while operator_stack and operator_stack[-1] != "(":
                output.append(operator_stack.pop())
            operator_stack.pop()
        else:
            raise ValueError("Invalid token")

    while operator_stack:
        output.append(operator_stack.pop())

    return ' '.join(output)

def evaluate_rpn(expression, truth_table):
    fourthrow = []
    for i in range(len(truth_table)):
        stack = []
        operators = {'&': lambda x, y: x and y,
                    '|': lambda x, y: x or y,
                    '>': lambda x, y: not(x) or y,
                    '!': lambda x: not(x),
                    '~': lambda x, y: x == y}

        for token in expression.split():
            if token.isalpha():
                if token == 'A':
                    stack.append(truth_table[i][0])
                elif token == 'B':
                    stack.append(truth_table[i][1])
                elif token == 'C':
                    stack.append(truth_table[i][2])
                elif token == 'D':
                    stack.append(truth_table[i][3])
                elif token == 'E':
                    stack.append(truth_table[i][4])
            elif token in operators:
                if len(stack) < 1:
                    raise ValueError("Not enough operands for operator %s" % token)
                operand = stack.pop()
                if token is "!":
                    result = operators[token](operand)
                else:
                    operand2 = stack.pop()
                    result = operators[token](operand2, operand)
                stack.append(result)
            else:
                raise ValueError("Invalid token: %s" % token)

        if len(stack) != 1:
            raise ValueError("Invalid expression")
        
        fourthrow.append(stack[0])
    return fourthrow
