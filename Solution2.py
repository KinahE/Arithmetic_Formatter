def arithmetic_arranger(problems, show_answers=False):
    #return problems

    ####VALIDATION#####
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        if '/' in problem or '*' in problem:
            return "Error: Operator must be '+' or '-'."
        for char in problem:
            if char.isalpha():
                return 'Error: Numbers must only contain digits.'
        operands = []
        if '+' in problem:
            operands = problem.split('+')
        elif '-' in problem:
            operands = problem.split('-')
        for operand in operands:
            operand = operand.strip()
            if len(operand) > 4:
                print(operands)
                return 'Error: Numbers cannot be more than four digits.'
    ###################
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    operands_as_ints = []
    operands_cleaned = []
    operator = ''
    for i in range(len(problems)):
        for problem in problems:
            if '+' in problem:
                operands = problem.split('+')
                operator = '+'
            elif '-' in problem:
                operands = problem.split('-')
                operator = '-'
            for operand in operands:
                operand = operand.strip()
                operands_cleaned.append(operand)
                operands_as_ints.append(int(operand))
            #####################
            if operator == '+':
                solution = operands_as_ints[0] + operands_as_ints[1]
            else:
                solution = operands_as_ints[0] - operands_as_ints[1]
            #####################
            padding_amt = max(len(operands_cleaned[0]), len(operands_cleaned[1])) - min(len(operands_cleaned[0]), len(operands_cleaned[1]))
            #####################
            if len(operands_cleaned[0]) > len(operands_cleaned[1]):
                longest_length = len(operands_cleaned[0])
                line1 += f'{" "*2}{operands_cleaned[0]}'
                line2 += f'{operator}{" "*(1+padding_amt)}{operands_cleaned[1]}'
            else:
                longest_length = len(operands_cleaned[1])
                line1 += f'{" "*(2+padding_amt)}{operands_cleaned[0]}'
                line2 += f'{operator}{" "*(1)}{operands_cleaned[1]}'
            line3 += f'{"-"*(2 + longest_length)}'
            #####################
            if len(str(solution)) == longest_length:
                line4 += f'{" "*(2)}{solution}'
            elif len(str(solution)) > longest_length:
                line4 += f'{" "*(1)}{solution}'
            else:
                line4 += f'{" "*(longest_length - len(str(solution)))}{solution}'

            ######################
            if i != len(problems) - 1:
                line1 += f'{" "* 4}'
                line2 += f'{" "* 4}'
                line3 += f'{" "* 4}'
                line4 += f'{" "* 4}'
            ######################
            operands_cleaned.clear()
            operands_as_ints.clear()
            longest_length = 0
            solution = 0
        return line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 if show_answers == True else line1 + "\n" + line2 + "\n" + line3


print(arithmetic_arranger(["3801 - 2", "123 + 49"]))


