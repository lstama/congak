import re
import random

def next_possible(arr: list, type_arr: list):
    now = len(arr) - 1
    plus = True
    while now >= 0:
        if plus:
            plus = False
            arr[now] += 1
            if arr[now] == 10:
                if type_arr[now] == 'x':
                    arr[now] = 1
                else:
                    arr[now] = 0
                plus = True
        now -= 1
    if plus:
        return -1
    return arr

def combine_pattern_with_arr(pattern: str, arr: list):
    result = ''
    now = 0
    for element in pattern:
        if element == 'x' or element == 'y':
            result += str(arr[now])
            now += 1
        else:
            result += element
    return result

def generate_possible_number(pattern: str):
    generated_list = []

    type_arr = []
    arr = []
    for element in pattern:
        if element == 'x':
            type_arr.append('x')
            arr.append(1)
        if element == 'y':
            type_arr.append('y')
            arr.append(0)

    if len(arr) == 0:
        return [pattern]

    generated_list.append(combine_pattern_with_arr(pattern, arr))
    arr = next_possible(arr, type_arr)
    while arr != -1:
        generated_list.append(combine_pattern_with_arr(pattern, arr))
        arr = next_possible(arr, type_arr)
    return generated_list

def generate_all_sum_problem (pattern: str):
    first, second = pattern.split('+', 2)
    generated_first = generate_possible_number(first)
    generated_second = generate_possible_number(second)
    generated_first_int = [int(x) for x in generated_first]
    generated_second_int = [int(x) for x in generated_second]
    generated_problem_and_answer = []
    for x in range(len(generated_first)):
        for y in range(len(generated_second)):
            generated_problem_and_answer.append((
                f'{generated_first[x]} + {generated_second[y]} =',
                generated_first_int[x] + generated_second_int[y]
                ))
    return generated_problem_and_answer

def generate_all_substract_problem (pattern: str):
    first, second = pattern.split('-', 2)
    generated_first = generate_possible_number(first)
    generated_second = generate_possible_number(second)
    generated_first_int = [int(x) for x in generated_first]
    generated_second_int = [int(x) for x in generated_second]
    generated_problem_and_answer = []
    for x in range(len(generated_first)):
        for y in range(len(generated_second)):
            if generated_first_int[x] > generated_second_int[y]:
                generated_problem_and_answer.append((
                    f'{generated_first[x]} - {generated_second[y]} =',
                    generated_first_int[x] + generated_second_int[y]
                    ))
    return generated_problem_and_answer

def generate_sum_problem(pattern: str, count : int = 0):
    # x/X : 1-9, y/Y : 0-9
    if not re.match(r"^[1-9xX][0-9xyXY]*\+[1-9xX][0-9xyXY]*$", pattern):
        return -1
    pattern = pattern.lower()
    generated_problem = generate_all_sum_problem(pattern)
    if generated_problem == -1:
        return -1
    if count <= 0 or count > len(generated_problem):
        count = len(generated_problem)
    random.shuffle(generated_problem)
    return generated_problem[:count]

def generate_substract_problem(pattern: str, count : int = 0):
    # x/X : 1-9, y/Y : 0-9
    if not re.match(r"^[1-9xX][0-9xyXY]*\-[1-9xX][0-9xyXY]*$", pattern):
        return -1
    pattern = pattern.lower()
    generated_problem = generate_all_substract_problem(pattern)
    if generated_problem == -1:
        return -1
    if count <= 0 or count > len(generated_problem):
        count = len(generated_problem)
    random.shuffle(generated_problem)
    return generated_problem[:count]
