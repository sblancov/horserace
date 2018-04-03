from random import randint
import os
import time
import petname


FINISH_LINE = 20


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


class HorseConsolePresenter(object):

    def __init__(self, horse):
        self.horse = horse

    def present(self):
        name = self.horse.name
        distance = self.horse.locate()
        position = '*' * distance
        status = '{}:\t{}\t{}\n'.format(name, distance, position)
        return status


class HorsesConsolePresenter(object):

    def __init__(self, horses):
        self.horses = horses

    def present(self):
        status = ''
        for horse in self.horses:
            horsep = HorseConsolePresenter(horse)
            status += horsep.present()
        return status


class WinnerHorseConsolePresenter(object):

    def __init__(self, horses):
        self.horses = horses

    def present(self):
        status = 'winner: {}!'
        winner = ''
        _max = 0
        for horse in self.horses:
            if horse.locate() > _max:
                _max = horse.locate()
                winner = horse.name
        return status.format(winner)


class HorsesConsoleViewer(object):

    def __init__(self, step, horsesp, winnerp):
        self.step = step
        self.horsesp = horsesp
        self.winnerp = winnerp

    def show(self):
        time.sleep(0.5)
        os.system('clear')
        screen = ''
        screeners = [
            self.step.current(),
            self.horsesp.present(),
            self.winnerp.present()
        ]
        for screener in screeners:
            screen += '{}\n'.format(screener)
        print(screen)


class Step(object):

    def __init__(self):
        self.step = 0

    def inc(self):
        self.step += 1

    def current(self):
        return self.step


def main():

    print('Make a bet!')

    horses = Horses()

    horse_names = [petname.generate() for i in range(4)]
    for name in horse_names:
        horse = Horse(name)
        horses.add_horse(horse)

    step = Step()

    horsesp = HorsesConsolePresenter(horses)
    winnerp = WinnerHorseConsolePresenter(horses)
    viewer = HorsesConsoleViewer(step, horsesp, winnerp)

    while not horses.first_arrive(FINISH_LINE):
        step.inc()
        horses.run()
        viewer.show()


if __name__ == '__main__':
    main()
