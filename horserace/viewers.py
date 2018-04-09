import os
import time


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
