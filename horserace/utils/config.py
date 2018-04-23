from configparser import ConfigParser


DEFAULT_DISTANCE = 10
DEFAULT_PARTICIPANTS = 3
SECTION = 'horserace'


class Loader(object):

    def distance(self):
        handler = self.next_handler()
        return handler.distance()

    def participants(self):
        handler = self.next_handler()
        return handler.participants()


class FileLoader(Loader):

    def __init__(self):
        self.config = ConfigParser()
        self.config.read(['horserace.cfg', 'setup.cfg'])

    def distance(self):
        field = 'distance'
        value = self.config.getint(
            SECTION, field, fallback=DEFAULT_DISTANCE)
        return value

    def participants(self):
        field = 'participants'
        value = self.config.getint(
            SECTION, field, fallback=DEFAULT_PARTICIPANTS)
        return value


class CommandLoader(Loader):

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.next_handler = FileLoader

    def distance(self):
        value = self.kwargs.get('distance')
        if value is not None:
            return int(value)
        else:
            return super().distance()

    def participants(self):
        value = self.kwargs.get('participants')
        if value is not None:
            return int(value)
        else:
            return super().participants()


class ConfigLoader(object):

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.loader = CommandLoader(**kwargs)

    def distance(self):
        result = self.loader.distance()
        return result

    def participants(self):
        result = self.loader.participants()
        return result
