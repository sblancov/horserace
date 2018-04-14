import petname

from utils.common import StepCounter
from viewers import HorsesConsoleViewer
from presenters import (
    HorsesConsolePresenter, WinnerHorseConsolePresenter)
from models import Horse, Horses


FINISH_LINE = 20


def main():

    horses = Horses()

    horse_names = [petname.generate() for i in range(4)]
    for name in horse_names:
        horse = Horse(name)
        horses.add_horse(horse)

    step = StepCounter()
    horsesp = HorsesConsolePresenter(horses)
    winnerp = WinnerHorseConsolePresenter(horses)
    viewer = HorsesConsoleViewer(step, horsesp, winnerp)

    while not horses.first_arrive(FINISH_LINE):
        step.inc()
        horses.run()
        viewer.show()


if __name__ == '__main__':
    main()
