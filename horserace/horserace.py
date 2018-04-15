import petname

from horserace.utils.common import StepCounter
from horserace.ui.console.viewers import RaceViewer
from horserace.ui.console.presenters import (
    RacePresenter, WinnerHorseConsolePresenter)
from horserace.models import Horse, Race


# TODO: Extract this variable as configuration.
FINISH_LINE = 10


def main():

    step_counter = StepCounter()
    horses = Race(step_counter)

    horse_names = [petname.generate() for i in range(4)]
    for name in horse_names:
        horse = Horse(name)
        horses.add_horse(horse)

    horsesp = RacePresenter(horses)
    winnerp = WinnerHorseConsolePresenter(horses)
    viewer = RaceViewer(step_counter, horsesp, winnerp)

    while not horses.first_arrive(FINISH_LINE):
        horses.run()
        viewer.show()


if __name__ == '__main__':
    main()
