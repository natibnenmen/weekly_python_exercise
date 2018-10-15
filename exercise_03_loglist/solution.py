import re

def logtolist(logfilename):
    list_of_dicts = []
    for line in open(logfilename):
        #m = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*(\[.*?\])', line)
        m = re.search(r'([\d\.]+)[\-\s]+\[(.*?)\]\s*"(.*?(?<!\\))"', line)
        list_of_dicts.append({'ip_address': m.group(1),
                              'timestamp': m.group(2),
                              'request': m.group(3)
                              })

    return list_of_dicts