
class StepCounter(object):

    def __init__(self):
        self.__step = 0

    def inc(self):
        self.__step += 1

    def current(self):
        return self.__step
