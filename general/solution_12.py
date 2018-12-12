import os
from hashlib import md5


class DirFileHash(object):

    def __init__(self, dir_name):
        self.dirname = dir_name
        self.file_dict = {}

        if not os.path.exists(self.dirname):
            return

        for one_filename in os.listdir(self.dirname):
            with open(os.path.join(self.dirname, one_filename), 'r') as f:
                m = md5()
                m.update(f.read().encode())
                self.file_dict[one_filename] = m.hexdigest()


    def dirname(self):
        return self.dirname


    def __getitem__(self, item):
        return self.file_dict.get(item, None)