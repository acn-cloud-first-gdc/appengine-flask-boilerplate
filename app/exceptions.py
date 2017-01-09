class TestException(Exception):
    def __init__(self, code, desc):
        self.code = code
        self.description = desc

    def __str__(self):
        return self.description


class KeyNotFoundException(TestException):
    def __init__(self, key_name=''):
        self.code = 404
        self.description = "Service error during key retrieval: key not found ({0}).".format(key_name)
