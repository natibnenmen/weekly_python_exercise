import random
import re


def get_rand_int_list_between(min, max, ammount):
    return [random.randint(min, max) for p in range(ammount)]


def get_rand_plus_and_minus_list(ammount):
    operator_list = []
    x = [random.randint(0, 1) for p in range(ammount)]
    for i in x:
        if i == 0:
            operator_list.append("-")
        else:
            operator_list.append("+")
    return operator_list



def create_math_problems(file_path, ammount, num_oprands, min, max):

    with open(file_path, 'w') as f:
        for i in range(1, ammount):
            operand_list = [random.randint(min, max) for p in range(num_oprands)]
            operator_list = get_rand_plus_and_minus_list(num_oprands - 1)
            deco_line = "[{{:>{0}}}]".format(len(str(ammount))+1)
            line = deco_line.format(i)
            line += "{:>6}".format(str(operand_list[0]))
            for an_operand in operand_list[1:]:
                line += " {0} ".format(operator_list[operand_list.index(an_operand) - 1]) + "({0:>{1}})".format(str(an_operand), len(str(max))+2)
            line += " = ______"
            f.write(line + "\n")


def process_line(line):
    try:
        # this is line format:
        # [  1]   19 - (   1) - (   4) + (  28) = ______
        res_string = re.sub('_', '', line).rstrip()
        m = re.sub(r'\[([^\]]+)\]','' , line)
        m = re.sub('[()_=]', '', m)
        m = m.split()
        return res_string + " " + str(eval(''.join(m)))

    except Exception as e:
        print(e.message)


def solve_math_problems(file_path_source, file_path_answered):
    with open(file_path_source, 'r') as fs:
        with open(file_path_answered, 'w') as fa:
            for i in fs:
                dst_line = process_line(i)
                fa.write(dst_line + "\n")



if __name__ == "__main__":
    creat_file_name = "test1.txt"
    solve_file_name = "test2.txt"
    create_math_problems(creat_file_name, 10, 4, -20, 20)
    solve_math_problems(creat_file_name, solve_file_name)