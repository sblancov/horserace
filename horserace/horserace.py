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
    race = Race(step_counter, FINISH_LINE)

    horse_names = [petname.generate() for i in range(4)]
    for name in horse_names:
        horse = Horse(name)
        race.add_horse(horse)

    race.start()

    racep = RacePresenter(race)
    winnerp = WinnerHorseConsolePresenter(race)
    viewer = RaceViewer(step_counter, racep, winnerp)

    while not race.has_finished():
        race.run()
        viewer.show()


if __name__ == '__main__':
    main()
