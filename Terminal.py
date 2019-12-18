from Cmd import Cmd
from Constants import ConsoleColors


class Terminal:
    exitCmd = Cmd("exit", "Exits the program", 0, 40)
    displayConstantsCmd = Cmd("constants", "Displays the constants used")
    displaySettingsCmd = Cmd("settings", "Displays the current settings")
    displayResultsCmd = Cmd("results", "Displays the last computed results. Add '-d' to get details, or replace by "
                                       "'-dn' to show the n first results (n between 1 and 9)", 0, 1)
    setPlayersCmd = Cmd("setPlayers", "Sets the number of players, needs one argument", 1, 1)
    setPicksCmd = Cmd("setPicks", "Sets the total number of picks per players, needs one to two arguments to "
                                  "specify a value or a range", 1, 2)
    setWheelsCmd = Cmd("setWheels", "Sets the min and max number of times a given pack is seen by a player, needs one "
                                    "to two "
                                    "arguments (ints or floats) to specify a value or range", 1, 2)
    setBurnCmd = Cmd("setBurn", "Sets the burn value or a range (cards discarded per pack) with one or two arguments",
                     1, 2)
    process = Cmd("process", "Processes the different possibilities according to all the parameters and filters, "
                             "and orders them", 0,
                  1)
    helpCmd = Cmd("help", "Displays the description of each command")
    setCubeSizeCmd = Cmd("setCubeSize", "Sets the size of the cube", 1, 1)
    rcmds = [process, displayResultsCmd, displayConstantsCmd, displaySettingsCmd, setCubeSizeCmd,
             setPlayersCmd, setPicksCmd, setWheelsCmd, setBurnCmd, helpCmd, exitCmd]

    @staticmethod
    def parseCmd(cmd: str) -> [str]:
        return cmd.replace(' ', '').split("-")

    @staticmethod
    def processCmd(line: str):
        c = Terminal.parseCmd(line)
        for rc in Terminal.rcmds:
            if rc.triggers(c):
                rc.execute(c)
                return
        print(ConsoleColors.getColoredStr("Invalid command", ConsoleColors.FAIL))
