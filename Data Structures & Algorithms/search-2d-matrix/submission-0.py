class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            mid_matrix = (top + bot) // 2

            if matrix[mid_matrix][0] > target:
                bot = mid_matrix - 1
            elif matrix[mid_matrix][-1] < target:
                top = mid_matrix + 1
            else:

                l, r = 0, len(matrix[mid_matrix]) - 1

                while l <= r:
                    mid = (l + r) // 2
                    curr_val = matrix[mid_matrix][mid]

                    if curr_val > target:
                        r = mid - 1
                    elif curr_val < target:
                        l = mid + 1
                    else:
                        return True
                
                return False
        
        return False
