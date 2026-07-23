class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                while left <= right:
                    col_mid = (left + right) // 2
                    if matrix[mid][col_mid] == target:
                        return True
                    elif matrix[mid][col_mid] > target:
                        right = col_mid - 1
                    else:
                        left = col_mid + 1
                return False
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                top = mid + 1
        return False