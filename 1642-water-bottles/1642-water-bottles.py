class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles

        while numBottles >= numExchange:
            refill = numBottles // numExchange
            result += refill
            empty = numBottles % numExchange
            numBottles = refill + empty
        return int(result)