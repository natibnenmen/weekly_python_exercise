

def myrange2(*args):
    '''
    a = [0, 0, 1]

    for arg in args:
        a[args.index(arg)] = arg

    start, end, jump = a
    '''
    jump = 1
    if len(args) == 1:
        start = 0
        end = args[0]
    if len(args) > 1:
        if args[1] != None:
            start = args[0]
            end = args[1]
        else:
            start = 0
            end = args[0]
    if len(args) == 3:
        jump = args[2]

    ret_list = []
    current_element = start
    while current_element < end:
        ret_list.append(current_element)
        current_element += jump

    return ret_list


def myrange3(*args):
    jump = 1
    if len(args) == 1:
        start = 0
        end = args[0]
    if len(args) > 1:
        if args[1] != None:
            start = args[0]
            end = args[1]
        else:
            start = 0
            end = args[0]
    if len(args) == 3:
        jump = args[2]

    current_element = start
    while current_element < end:
        yield current_element
        current_element += jump
