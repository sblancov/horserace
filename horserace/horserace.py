import petname

from configparser import ConfigParser

from horserace.utils.common import StepCounter
from horserace.ui.console.viewers import RaceViewer
from horserace.ui.console.presenters import (
    RacePresenter, WinnerHorseConsolePresenter)
from horserace.models import Horse, Race


def main():
    config = ConfigParser()
    config.read('horserace.ini')
    distance = int(config['horserace']['distance'])
    participants = int(config['horserace']['participants'])

    step_counter = StepCounter()
    race = Race(step_counter, distance)

    # TODO: Refactor this create a HorseFactory with:
    #  HorseFactory.random() and HorseFactory.named(name)
    horse_names = [petname.generate() for i in range(participants)]
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
