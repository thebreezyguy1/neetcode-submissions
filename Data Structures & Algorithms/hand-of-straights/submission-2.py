class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False

        frequencies = Counter(hand)

        for num in sorted(hand):
            if not frequencies[num]:
                continue
            for i in range(num, num + groupSize):
                if not frequencies[i]:
                    return False
                frequencies[i] -= 1
        
        return True