from configparser import ConfigParser


class ConfigLoader(object):

    def __init__(self):
        self.config = ConfigParser()
        self.config.read(['horserace.cfg', 'setup.cfg'])

    def distance(self):
        section = 'horserace'
        field = 'distance'
        default = 10
        distance = self.config.getint(section, field, fallback=default)
        return distance

    def participants(self):
        section = 'horserace'
        field = 'participants'
        default = 3
        participants = self.config.getint(section, field, fallback=default)
        return participants
