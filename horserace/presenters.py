
class HorseConsolePresenter(object):

    def __init__(self, horse):
        self.horse = horse

    def present(self):
        name = self.horse.name
        distance = self.horse.locate()
        position = '*' * distance
        status = '{}:\t{}\t{}\n'.format(name, distance, position)
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
