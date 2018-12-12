

class Tee(object):

    def __init__(self, *files):
        self.files = files


    def write(self, text):
        for file in self.files:
            file.write(text)


    def writelines(self, lines):
        for line in lines:
            self.write(line)


    def __enter__(self):
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        for file in self.files:
            file.close()



