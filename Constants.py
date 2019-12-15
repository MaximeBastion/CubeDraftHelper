class Constants:
    CUBE_SIZE = 360
    MIN_PACK_SIZE = 2
    MAX_PACK_SIZE = 50
    MIN_PACK_PER_PLAYER = 2
    MAX_PACK_PER_PLAYER = 25
    MAX_WHEELS_COMPUTED = 3  # Defines what wheels are computed (x packs are seen 1 time, x packs are seen 2 times)

    @staticmethod
    def display():
        print(
            "\nConstants:"
            + "\nCube size: " + str(Constants.CUBE_SIZE)
            + "\nPack size: " + str(Constants.MIN_PACK_SIZE) + " - " + str(Constants.MAX_PACK_SIZE)
            + "\nPacks per player: " + str(Constants.MIN_PACK_PER_PLAYER) + " - " + str(Constants.MAX_PACK_PER_PLAYER)
        )


class ConsoleColors:
    HEADER = '\033[95m'
    BOLD = '\033[1m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    ASKING_INPUT = BOLD
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    RESULT = OKBLUE
    UNDERLINE = '\033[4m'

    @staticmethod
    def getColoredStr(msg, consoleColor) -> str:
        return consoleColor + msg + ConsoleColors.ENDC
