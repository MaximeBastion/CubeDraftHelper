class m:

    @staticmethod
    def computeSumFrom1ToN(n: int) -> int:
        """
        Computes the sum of the first n integers.
        :param n: high value
        :return: float
        """
        return int(0.5 * n * (n + 1))

    @staticmethod
    def computeSumFromUtoN(u: int, n: int) -> int:
        """
        Computes the sum of the integers between u and n. [u ... n]
        :param u: low value
        :param n: high value
        :return: float
        """
        return m.computeSumFrom1ToN(n) - m.computeSumFrom1ToN(u - 1)

    @staticmethod
    def getV1ToY(p: int, pP: int, y: int) -> [int]:
        out = [0 for i in range(y)]
        for n in range(1, y + 1):
            out[n - 1] = m.computeVn(p, pP, n)
        return out

    @staticmethod
    def computeVn(p: int, pP: int, n: int) -> int:
        """
        Computes the amount of packs that are seen n times in a round.
        :param p: Number of players
        :param pP: Picks per pack
        :param n: Exact amount of times a pack has to be seen to be counted
        :return: int
        """
        if pP <= (n - 1) * p or pP >= (n + 1) * p:
            return 0
        return p - abs(pP - (n * p))
