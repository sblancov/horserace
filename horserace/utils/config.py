from configparser import ConfigParser


class ConfigLoader(object):

    def __init__(self):
        self.config = ConfigParser()
        self.config.read(['horserace.cfg', 'setup.cfg'])

    def distance(self):
        distance = self.config.getint('horserace', 'distance')
        return distance

    def participants(self):
        participants = self.config.getint('horserace', 'participants')
        return participants
