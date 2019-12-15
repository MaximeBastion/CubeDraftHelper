class CurrentSettings:
    nPlayers = 4
    minPicksPerPlayer = 45
    maxPicksPerPlayer = 50
    minPackWheel = 1.7
    maxPackWheel = 2.3
    minBurn = 0
    maxBurn = 46

    @staticmethod
    def display():
        print(
            "\nCurrent settings:"
            + "\nPlayers: " + str(CurrentSettings.nPlayers)
            + "\nPicks per player: " + str(CurrentSettings.minPicksPerPlayer) + " - " + str(CurrentSettings.maxPicksPerPlayer)
            + "\nPack wheels: " + str(CurrentSettings.minPackWheel) + " - " + str(CurrentSettings.maxPackWheel)
            + "\nBurn: " + str(CurrentSettings.minBurn) + " - " + str(CurrentSettings.maxBurn)
        )
