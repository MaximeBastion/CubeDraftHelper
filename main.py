from Constants import ConsoleColors
from CurrentSettings import CurrentSettings
from Terminal import Terminal


def main():
    print("\n" + ConsoleColors.getColoredStr("Cube Draft Mode Helper v1.0", ConsoleColors.BOLD))
    print("Use this program to decide which parameters you want for your draft.")
    print("Give him a cube size (360 by default) and a number of players and he will tell you the best draft options "
          "in order to optimize a given parameter.\nBy default it will try to emulate the experience of a classic "
          "draft which is a draft with 8 players and 3 packs of 15 cards per player.")

    recommended = input("\n" + ConsoleColors.getColoredStr("Do you want to go for the recommended execution? (yes or "
                                                           "no): ", ConsoleColors.ASKING_INPUT))
    recommended = True if recommended.lower() == "yes" else False

    if recommended:
        players = int(input(ConsoleColors.getColoredStr("How many players? ", ConsoleColors.ASKING_INPUT)))
        CurrentSettings.nPlayers = players
        Terminal.processCmd("process")
        Terminal.processCmd("results")

    print("\nTerminal mode\nUse 'help'. Arguments are given as follow: cmd -arg1 -arg2")
    while True:
        cmd = input(ConsoleColors.getColoredStr("cmd: ", ConsoleColors.ASKING_INPUT))
        Terminal.processCmd(cmd)


main()
