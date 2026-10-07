class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        remaining_triplets = []
        
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            remaining_triplets.append(t)
        
        for i,num in enumerate(target):
            found = False
            for t in remaining_triplets:
                if t[i] == num:
                    found = True
            if not found:
                return False
        
        return True