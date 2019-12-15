class InitialParameters:

    def __init__(self, cubeSize, nPlayers, nPacksPerPlayer, packSize, burn):
        self.cubeSize = cubeSize
        self.nPlayers = nPlayers
        self.nPacksPerPlayer = nPacksPerPlayer
        self.packSize = packSize
        self.burn = burn

    def getStr(self):
        return "\n--InitialParameters:\nCube Size: " + str(self.cubeSize) \
               + "\nPlayers: " + str(self.nPlayers) \
               + "\nPacks per player: " + str(self.nPacksPerPlayer) \
               + "\nPack size: " + str(self.packSize) \
               + "\nBurn: " + str(self.burn)

    @staticmethod
    def askInitialParameters():
        cubeSize = int(input("Cube size: "))
        nPlayers = int(input("Players: "))
        nPacksPerPlayer = int(input("PacksPerPlayer: "))
        packSize = int(input("Pack size: "))
        burn = int(input("Burn: "))
        return InitialParameters(cubeSize, nPlayers, nPacksPerPlayer, packSize, burn)

    @staticmethod
    def getClassicParams():
        return InitialParameters(360, 8, 3, 15, 0)

    @staticmethod
    def getAllParamsThatRespectConstraints(cubeSize: int, nPlayers: int, minPackSize: int, maxPackSize: int, minPackPerPlayer: int, maxPackPerPlayer: int, minBurn: int, maxBurn: int):
        initialParams = []
        pPPRange = range(minPackPerPlayer, maxPackPerPlayer + 1) if minPackPerPlayer < maxPackPerPlayer else [minPackPerPlayer]
        paSizeRange = range(minPackSize, maxPackSize + 1) if minPackSize < maxPackSize else [minPackSize]
        burnRange = range(minBurn, maxBurn + 1) if minBurn < maxBurn else [minBurn]
        for pPP in pPPRange:
            for paSize in paSizeRange:
                for burn in burnRange:
                    if paSize > burn and paSize * pPP * nPlayers <= cubeSize:
                        initialParams.append(InitialParameters(cubeSize, nPlayers, pPP, paSize, burn))
        print("Generated " + str(len(initialParams)) + " params with these constraints")
        return initialParams

