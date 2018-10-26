#!/usr/bin/env python3
import re
#from datetime import strptime
import datetime
import operator
import time


class LogDicts:

    def comp_time(self, element1, element2):
        time_format = '%d/%b/%Y:%H:%M:%S'
        return int(time.mktime(time.strptime(element1['timestamp'][:-6], time_format))) - int(time.mktime(time.strptime(element2['timestamp'][:-6], time_format)))


    def __init__(self, log_file_name):
        self.list_of_dicts = self.logtolist(log_file_name)

    def dicts(self, key=None):
        return sorted(self.list_of_dicts, key=key)

    def earliest(self):
        #sort_key = operator.itemgetter('timestamp')
        return sorted(self.list_of_dicts, self.comp_time)[0]

    def latest(self):
        return sorted(self.list_of_dicts, self.comp_time)[-1]

    def for_ip(self, ip):
        return [i for i in self.list_of_dicts if ip in i['ip_address']]

    def for_request(self, text):
        return [i for i in self.list_of_dicts if text in i['request']]
        #return sum(1 for p in self.list_of_dicts if p['request'] == text)

    def iterdicts(self):
        for line in self.list_of_dicts:
            yield line


    def line_to_dict(self, line):
        ip_address = line.split()[0]

        timestamp_start = line.index('[') + 1
        timestamp_end = line.index(']')
        timestamp = line[timestamp_start:timestamp_end]

        request_start = line.index('"') + 1
        request_end = line[request_start:].index('"')
        request = line[request_start:request_start + request_end]

        return {'ip_address': ip_address,
                'timestamp': timestamp,
                'request': request}

    def logtolist(self, filename):
        return [re_line_to_dict(line)
                for line in open(filename)]



def re_line_to_dict(line):
    regexp = r'''
((?:\d{1,3}\.){3}\d{1,3})       # IP addresses contain four numbers (each with 1-3 digits)
.*                              # Junk between IP address and timestamp
\[([^\]]+)\]                    # Timestamp, defined to be anything between [ and ]
.*                              # Junk between timestamp and request
"(GET[^"]+)"                    # Request, starting with GET
'''
    m = re.search(regexp, line, re.X)

    if m:
        ip_address = m.group(1)
        timestamp = m.group(2)
        request = m.group(3)

    else:
        ip_address = 'No IP address found'
        timestamp = 'No timestamp found'
        request = 'No request found'

    output = {'ip_address': ip_address,
              'timestamp': timestamp,
              'request': request}
    return output






