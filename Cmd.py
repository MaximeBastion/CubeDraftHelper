import Terminal
from Constants import Constants
from CurrentData import CurrentData
from CurrentSettings import CurrentSettings
from DraftMode import DraftMode
from InitialParameters import InitialParameters
from ModeCollection import ModeCollection


class Cmd:

    def __init__(self, trigger: str, description: str, minArguments: int = 0, maxArguments: int = 0):
        self.trigger = trigger
        self.description = description
        self.minArguments = minArguments
        self.maxArguments = maxArguments

    def triggers(self, parsedCmd: [str]):
        return parsedCmd[0] == self.trigger \
               and self.minArguments <= len(parsedCmd) - 1 <= self.maxArguments

    def execute(self, parsedCmd: [str]):
        c = parsedCmd
        if self.trigger == "exit":
            print()
            exit()
            return
        if self.trigger == "setPlayers":
            try:
                CurrentSettings.nPlayers = int(c[1])
            except:
                print("Error while setting nPlayers. Probably because of the arg type.")
            return
        if self.trigger == "setPicks":
            maxV = c[1] if len(c) == 2 else c[2]
            CurrentSettings.minPicksPerPlayer = int(c[1])
            CurrentSettings.maxPicksPerPlayer = int(maxV)
            return
        if self.trigger == "setWheels":
            maxV = c[1] if len(c) == 2 else c[2]
            CurrentSettings.minPackWheel = float(c[1])
            CurrentSettings.maxPackWheel = float(maxV)
            return
        if self.trigger == "setBurn":
            maxV = c[1] if len(c) == 2 else c[2]
            CurrentSettings.minBurn = int(c[1])
            CurrentSettings.maxBurn = int(maxV)
            return
        if self.trigger == "process":
            CurrentData.initialParameters = InitialParameters.getAllParamsThatRespectConstraints(
                Constants.CUBE_SIZE,
                CurrentSettings.nPlayers,
                Constants.MIN_PACK_SIZE,
                Constants.MAX_PACK_SIZE,
                Constants.MIN_PACK_PER_PLAYER,
                Constants.MAX_PACK_PER_PLAYER,
                CurrentSettings.minBurn,
                CurrentSettings.maxBurn
            )

            draftModes = []
            for iP in CurrentData.initialParameters:
                draftModes.append(DraftMode(iP))
            CurrentData.modeCollection = ModeCollection(draftModes)

            CurrentData.filteredModes = CurrentData.modeCollection.getFilteredModes()

            CurrentData.orderedModes = ModeCollection.orderModesBy(CurrentData.filteredModes)
        if self.trigger == "help":
            print("\nCommands:")
            for cmd in Terminal.Terminal.rcmds:
                print("-" + cmd.trigger + ": " + cmd.description)
            print()
        if self.trigger == "constants":
            Constants.display()
        if self.trigger == "settings":
            CurrentSettings.display()
        if self.trigger == "results":
            details = True if len(c) > 1 and c[1][0] == "d" else False
            if details:
                if len(c[1]) > 1:
                    size = int(c[1][1])
                    CurrentData.display(details, size)
                else:
                    CurrentData.display(details)
            else:
                CurrentData.display(details)
