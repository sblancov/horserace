from random import randint


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


class Horses(object):

    def __init__(self):
        self.horses = []

    def __iter__(self):
        return self.horses.__iter__()

    def __next__(self):
        return self.horses.__next__()

    def add_horse(self, horse):
        self.horses.append(horse)

    def run(self):
        for horse in self.horses:
            horse.run()

    def first_arrive(self, finish_line_distance):
        for horse in self.horses:
            if horse.has_arrive(finish_line_distance):
                return True
        return False
