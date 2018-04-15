import os
import time


# TODO: Probably this viewer needs a Layout, and Layout receive as parameters Presenters.
# Then, this class only show layout and data inside it.
class RaceViewer(object):

    def __init__(self, step, race, winner):
        self.step = step
        self.race = race
        self.winner = winner

    def show(self):
        time.sleep(0.5)
        os.system('clear')
        screen = ''
        screeners = [
            self.step.current(),
            self.race.present(),
            self.winner.present()
        ]
        for screener in screeners:
            screen += '{}\n'.format(screener)
        print(screen)
