def parse_to_list(problem):
    return problem.split()

def appropriate_operator(operator):
    if operator == "*" or operator == "/":
        print("Error: Operator must be '+' or '-'.")
        return False
    else:
        return True

def are_digits(numbers):
    for number in numbers:
        for char in number:
            if char.isalpha():
                print('Error: Numbers must only contain digits.')
                return False
            else:
                continue
    return True

def appropriate_length(numbers):
    for number in numbers:
        if len(str(number)) > 4:
            print('Error: Numbers cannot be more than four digits.')
            return False
        else:
            continue
    return True

def valid_problems(problems):
    if problem_counter(problems) is False:
        return False

    for problem in problems:
        problem_as_list = parse_to_list(problem)
        operator = problem_as_list[1]
        operands = problem_as_list[0:3:2]

        if appropriate_operator(operator) and are_digits(operands) and appropriate_length(operands):
            continue
    return True

def solve_problem(terms):
    if "-" in terms:
        return int(terms[0]) - int(terms[2])
    else:
        return int(terms[0]) + int(terms[2])
def problem_counter(problems):
    if len(problems) > 5:
        print('Error: Too many problems.')
        return False
    else:
        return True
def format_length (x,y):
    return max(len(str(x)), len(str(y)))

def longest_num(x,y):
    longest = max(len(str(x)), len(str(y)))
    if len(x) == longest:
        return x
    else:
        return y

def add_padding(x,y):
    max_digits = max(len(x), len(y))
    min_digits = min(len(x), len(y))
    
    padding_amt = max_digits - min_digits

    return add_char(" ", padding_amt)

def add_char(character,amount):
    return character * amount

def arithmetic_arranger(problems, show_answers=False):
    #return problems

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    solution = 0

    if valid_problems(problems) != True:
        return "";
    else:
        for problem in problems:
            terms = parse_to_list(problem)
            solution = solve_problem(terms)
            length = format_length(terms[0], terms[2])

            longest = longest_num(terms[0], terms[2])
            
            line1 += f'{add_char(" ",2)}{terms[0]}' if terms[0] == longest else f'{add_char(" ",2)}{add_padding(terms[0], terms[2])}{terms[0]}'
            line2 += f'{terms[1]}{add_char(" ",1)}{terms[2]}' if terms[2] == longest else f'{terms[1]}{add_char(" ",1)}{add_padding(terms[0], terms[2])}{terms[2]}'
            bar_length = len(f'{terms[1]}{add_char(" ",1)}{terms[2]}' if terms[2] == longest else f'{terms[1]}{add_char(" ",1)}{add_padding(terms[0], terms[2])}{terms[2]}')

            line4 +=f'{add_char(" ",2)}{solution}' if len(longest) >= len(str(solution)) else f'{add_padding(longest, str(solution))}{solution}'
            line3 += add_char("-", bar_length)
            
            line1 += f'{add_char(" ",4)}'
            line2 += f'{add_char(" ",4)}'
            line3 += f'{add_char(" ",4)}'
            line4 += f'{add_char(" ",4)}'
        if show_answers:

            return f'{line1}\n{line2}\n{line3}\n{line4}'
        else:
            return f'{line1}\n{line2}\n{line3}'





