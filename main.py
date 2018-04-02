from random import randint
import os
import time


STEPS = 20

class Horse(object):

    def __init__(self, name):
        self.name = name
        self.speed = 0
    
    def run(self):
        self.speed += randint(0, 1)

    def locate(self):
        return self.speed


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


class HorseConsolePresenter(object):

    def __init__(self, horse):
        self.horse = horse
    
    def present(self):
        name = self.horse.name
        position = '*' * self.horse.locate()
        status = '{}:\t{}\n'.format(name, position)
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

    def __init__(self, horsesp, winnerp):
        self.horsesp = horsesp
        self.winnerp = winnerp

    def show(self, step):
        time.sleep(0.5)
        os.system('clear')
        screen = '{}\n{}\n{}'.format(
                step, self.horsesp.present(), self.winnerp.present())
        print(screen)


def main():

    print('Make a bet!')

    horses = Horses()
    
    horse_names = ['ziupo', 'jioki', 'baerun']
    for name in horse_names:
        horse = Horse(name)
        horses.add_horse(horse)

    horsesp = HorsesConsolePresenter(horses)
    winnerp = WinnerHorseConsolePresenter(horses)

    viewer = HorsesConsoleViewer(horsesp, winnerp)
    for step in range(STEPS):
        horses.run()
        viewer.show(step)


if __name__ == '__main__':
    main()