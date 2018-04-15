from random import randint


class StartedRace(Exception):
    pass


class NotStartedRace(Exception):
    pass


class Horse(object):

    def __init__(self, name):
        self.name = name
        self.location = 0

    def run(self):
        speed = randint(0, 1)
        self.location += speed

    def locate(self):
        return self.location

    def has_arrive(self, finish_line_distance):
        return self.location == finish_line_distance


class Race(object):

    def __init__(self, step_counter, distance):
        self.started = False
        self.distance = distance
        self.horses = []
        self.step_counter = step_counter

    def __iter__(self):
        return self.horses.__iter__()

    def __next__(self):
        return self.horses.__next__()

    def add_horse(self, horse):
        if self.started:
            raise StartedRace()
        self.horses.append(horse)

    def start(self):
        self.started = True

    def run(self):
        if not self.started:
            raise NotStartedRace()
        for horse in self.horses:
            horse.run()
        self.step_counter.inc()

    def has_finished(self):
        for horse in self.horses:
            if horse.has_arrive(self.distance):
                return True
        return False
