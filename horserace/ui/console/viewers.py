import os
import time


# TODO: Probably this viewer needs a Layout, and Layout receive as parameters Presenters.
# Then, this class only show layout and data inside it.
class RaceViewer(object):

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
