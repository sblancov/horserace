
class HorseConsolePresenter(object):

    def __init__(self, horse):
        self.horse = horse

    def present(self):
        name = self.horse.name
        distance = self.horse.locate()
        position = '*' * distance
        status = '{}:\t{}\t{}\n'.format(name, distance, position)
        return status


class RacePresenter(object):

    def __init__(self, race):
        self.race = race

    def present(self):
        status = ''
        for horse in self.race:
            horsep = HorseConsolePresenter(horse)
            status += horsep.present()
        return status


class WinnerHorsePresenter(object):

    def __init__(self, race):
        self.race = race

    def present(self):
        status = 'winner: {}!'
        winner = ''
        _max = 0
        for horse in self.race:
            if horse.locate() > _max:
                _max = horse.locate()
                winner = horse.name
        return status.format(winner)
