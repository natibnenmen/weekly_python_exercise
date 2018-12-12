import os
import pprint

pp = pprint.PrettyPrinter(indent = 4)

def file_length(filename):
    return os.stat(filename).st_size

def filefunc(dir_name, func):

    res_dict = {}
    err_dict = {}

    for f in os.listdir(dir_name):
        try:
            file_pull_path = os.path.join(dir_name, f)
            if os.path.isfile(file_pull_path):  # join('.',f):os.path.join(path, item)
                res_dict[f] = func(file_pull_path)
        except Exception as e:
                err_dict[f] = e
                print(e.message)

    return res_dict, err_dict


if __name__ == "__main__":
    pp.pprint(filefunc(r'C:/Users/nbenmena/Documents', file_length))
    pp.pprint(filefunc(os.getcwd() + '/..', file_length))
