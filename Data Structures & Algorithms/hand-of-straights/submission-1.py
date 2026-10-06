class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False

        frequencies = Counter(hand)

        for k in sorted(frequencies.keys()):
            if frequencies[k] == 0:
                continue
            while frequencies[k] > 0:
                for num in range(k + 1, k + groupSize):
                    if num not in frequencies:
                        return False
                    frequencies[num] -= 1
                frequencies[k] -= 1
        return True