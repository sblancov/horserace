import click

from horserace.utils.common import StepCounter
from horserace.utils.config import ConfigLoader
from horserace.ui.console.viewers import RaceViewer
from horserace.ui.console.presenters import (
    RacePresenter, WinnerHorsePresenter)
from horserace.models.race import HorseFactory, Race


@click.command()
@click.option('--distance', help='Number of steps to reach the finish line.')
@click.option('--participants', help='Number of participants in the race!')
def main(**kwargs):
    config = ConfigLoader(**kwargs)
    distance = config.distance()
    participants = config.participants()

    step_counter = StepCounter()
    race = Race(step_counter, distance)

    horse_factory = HorseFactory()
    for i in range(participants):
        horse = horse_factory.random()
        race.add_horse(horse)

    race.start()

    # TODO: Create layer...
    racep = RacePresenter(race)
    winnerp = WinnerHorsePresenter(race)
    viewer = RaceViewer(step_counter, racep, winnerp)

    while not race.has_finished():
        race.run()
        viewer.show()


if __name__ == '__main__':
    main()
