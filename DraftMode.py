from Constants import Constants
from InitialParameters import InitialParameters
from m import m


class DraftMode:

    def __init__(self, initialParameters: InitialParameters):
        self.i = initialParameters
        self.picksPerPack = int
        self.nPicks = -1
        self.nPicksTotal = -1
        self.totalSelection = -1
        self.totalSelectionUnique = -1
        self.avgSelection = -1
        self.avgSelectionUnique = -1
        self.avgWheel: float = 0
        self.wheels = []
        self.compute()

    def compute(self):
        i = self.i
        if i.burn <= 0:
            self.picksPerPack = i.packSize
            self.nPicks = self.picksPerPack * i.nPacksPerPlayer
            self.nPicksTotal = self.nPicks * i.nPlayers
            self.totalSelection = m.computeSumFrom1ToN(i.packSize) * i.nPacksPerPlayer
            self.totalSelectionUnique = m.computeSumFromUtoN(i.packSize - i.nPlayers + 1,
                                                             i.packSize) * i.nPacksPerPlayer
            self.avgSelection = self.totalSelection / self.nPicks
            self.avgSelectionUnique = self.totalSelectionUnique / self.nPicks
            self.avgWheel = i.packSize / i.nPlayers
            self.wheels = m.getV1ToY(self.i.nPlayers, self.picksPerPack, Constants.MAX_WHEELS_COMPUTED)
        else:
            self.picksPerPack = i.packSize - i.burn
            self.nPicks = i.nPacksPerPlayer * self.picksPerPack
            self.nPicksTotal = self.nPicks * i.nPlayers
            self.totalSelection = m.computeSumFromUtoN(i.burn + 1, i.packSize) * i.nPacksPerPlayer
            self.totalSelectionUnique = m.computeSumFromUtoN(i.packSize - i.nPlayers + 1,
                                                             i.packSize) * i.nPacksPerPlayer
            self.avgSelection = self.totalSelection / self.nPicks
            self.avgSelectionUnique = self.totalSelectionUnique / self.nPicks
            self.avgWheel = self.picksPerPack / i.nPlayers
            self.wheels = m.getV1ToY(self.i.nPlayers, self.picksPerPack, Constants.MAX_WHEELS_COMPUTED)

    def getDifferenceFactor(self, otherDraftMode):
        avgSelunique = DraftMode.getDifference(self.avgSelectionUnique, otherDraftMode.avgSelectionUnique)
        distanceToPerfectWheels: float = abs((self.avgWheel - 2) / 2)
        return avgSelunique + distanceToPerfectWheels

    def getComputedValuesStr(self):
        return "\n--Computed Values:" + "\nPicks per pack: " + str(self.picksPerPack) \
               + "\nPicks per player: " + str(self.nPicks) \
               + "\nTotal picks: " + str(self.nPicksTotal) \
               + "\nTotal Selection: " + str(self.totalSelection) \
               + "\nTotal Selection Unique: " + str(self.totalSelectionUnique) \
               + "\nAverage Selection per pick: " + str(self.avgSelection) \
               + "\nAverage Selection Unique per pick: " + str(self.avgSelectionUnique) \
               + "\nAverage Wheel per pack: " + str(self.avgWheel) \
               + "\nWheels: " + str(self.wheels)

    def display(self, comparer=None):
        coreMsg = self.i.getStr() + self.getComputedValuesStr() if comparer is None else self.i.getStr() + self.getComparisonStr(comparer)
        print("\n--------------------" + coreMsg)

    def displaySimple(self):
        msg = "Each player will have " + str(self.i.nPacksPerPlayer) \
            + " packs of " + str(self.i.packSize) + " cards."
        if self.i.burn > 0:
            msg += "\nWhen a pack has exactly " + str(self.i.burn) \
                   + " cards left in it, discard it."
        print(msg)

    def getComparisonStr(self, otherMode) -> str:
        d = DraftMode.getDifferenceStr
        o = otherMode
        return "\n--Computed Values: difference with optimal = " + str(round(self.getDifferenceFactor(o) * 100, 1)) + "%\nPicks per pack: " + str(self.picksPerPack) + d(self.picksPerPack,
                                                                                          o.picksPerPack) \
               + "\nPicks per player: " + str(self.nPicks) + d(self.nPicks, o.nPicks) \
               + "\nTotal picks: " + str(self.nPicksTotal) + d(self.nPicksTotal, o.nPicksTotal) \
               + "\nTotal Selection: " + str(self.totalSelection) + d(self.totalSelection, o.totalSelection) \
               + "\nTotal Selection Unique: " + str(self.totalSelectionUnique) + d(self.totalSelectionUnique, o.totalSelectionUnique) \
               + "\nAverage Selection per pick: " + str(self.avgSelection) + d(self.avgSelection, o.avgSelection) \
               + "\nAverage Selection Unique per pick: " + str(self.avgSelectionUnique) + d(self.avgSelectionUnique, o.avgSelectionUnique) \
               + "\nAverage Wheel per pack: " + str(self.avgWheel) + d(self.avgWheel, 2) \
            + "\nWheels: " + str(self.wheels) + " (" + str(o.wheels) + ")"

    @staticmethod
    def getDifference(x, y):
        """
        Get a difference in percentage between two values.
        :param x: low value.
        :param y: high value, referent.
        :return:
        """
        return abs(y - x) / y

    @staticmethod
    def getDifferenceStr(x, y) -> str:
        """
        Get a difference in percentage between two values, displayed in str.
        This time it can be negative
        :param x: low value.
        :param y: high value, referent.
        :return:
        """
        return str(" (" + str(round((x - y) / y * 100)) + "%)")

    @staticmethod
    def orderModesBy(modes, propertyToSortBy="diffToClassic"):
        sortedModes = []

        if propertyToSortBy == "diffToClassic":
            classicMode = DraftMode(InitialParameters.getClassicParams())

            while modes:
                minDiff = 100000
                minMode = None
                for dM in modes:
                    diff = dM.getDifferenceFactor(classicMode)
                    if diff < minDiff:
                        minDiff = diff
                        minMode = dM
                sortedModes.append(minMode)
                modes.remove(minMode)
        return sortedModes

    @staticmethod
    def filterModes(modes, minPicksPerPlayer, maxPicksPerPlayer, minPackWheel, maxPackWheel):
        filteredModes = []
        totalPicksRange = range(minPicksPerPlayer,
                                maxPicksPerPlayer + 1) if minPicksPerPlayer < maxPicksPerPlayer else [minPicksPerPlayer]
        for m in modes:
            if m.nPicks in totalPicksRange and minPackWheel <= m.avgWheel <= maxPackWheel:
                filteredModes.append(m)
        print("Filtered down to " + str(len(filteredModes)) + " modes")
        return filteredModes

    @staticmethod
    def getClassic():
        return DraftMode(InitialParameters.getClassicParams())