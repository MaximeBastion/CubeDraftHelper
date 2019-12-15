from copy import deepcopy
from Constants import ConsoleColors
from CurrentSettings import CurrentSettings
from DraftMode import DraftMode
from InitialParameters import InitialParameters


class ModeCollection:

    def __init__(self, modes: [DraftMode]):
        self.modes = modes
        self.lastFilteredModes = []

    def getFilteredModes(self):
        filteredModes = []
        totalPicksRange = range(CurrentSettings.minPicksPerPlayer, CurrentSettings.maxPicksPerPlayer + 1) \
            if CurrentSettings.minPicksPerPlayer < CurrentSettings.maxPicksPerPlayer else [
            CurrentSettings.minPicksPerPlayer]
        for m in self.modes:
            if m.nPicks in totalPicksRange and CurrentSettings.minPackWheel <= m.avgWheel <= CurrentSettings.maxPackWheel:
                filteredModes.append(m)
        print("Filtered down to " + str(len(filteredModes)) + " modes")
        self.lastFilteredModes = filteredModes
        return filteredModes

    @staticmethod
    def orderModesBy(modes, propertyToSortBy="diffToClassic"):
        if len(modes) == 0:
            return []
        print("Ordering modes")
        sortedModes = []
        tempModes = deepcopy(modes)
        if propertyToSortBy == "diffToClassic":
            classicMode = DraftMode(InitialParameters.getClassicParams())

            while tempModes:
                minDiff = 100000
                minMode = None
                for dM in tempModes:
                    diff = dM.getDifferenceFactor(classicMode)
                    if diff < minDiff:
                        minDiff = diff
                        minMode = dM
                sortedModes.append(minMode)
                tempModes.remove(minMode)
        return sortedModes

    @staticmethod
    def displaySimple(modes):
        if len(modes) == 0:
            print(ConsoleColors.getColoredStr("No result found", ConsoleColors.FAIL))
            return
        for i, mode in enumerate(modes):
            if i > 0:
                seeNext = input(ConsoleColors.getColoredStr("\nDisplay the next one? (enter for yes, no otherwise): ",
                                                            ConsoleColors.ASKING_INPUT))
                seeNext = True if seeNext == "" else False
                if not seeNext:
                    break
            print(ConsoleColors.RESULT)
            print("Proposition n°" + str(i + 1) + ":")
            mode.displaySimple()

        print(ConsoleColors.ENDC)
