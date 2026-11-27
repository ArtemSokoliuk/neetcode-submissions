class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1

        while start <= end:
            mid = (start+end)//2
            curr_vals = matrix[mid]

            if curr_vals[0] <= target <= curr_vals[-1]:
                start_i = 0
                end_i = len(curr_vals) - 1

                while start_i <= end_i:
                    mid_i = (start_i+end_i)//2
                    curr_val = curr_vals[mid_i]

                    if curr_val == target:
                        return True
                    elif curr_val < target:
                        start_i = mid_i+1
                    elif curr_val > target:
                        end_i = mid_i-1
                
                return False

            elif target < curr_vals[0]:
                end = mid-1 
            elif target > curr_vals[-1]:
                start = mid+1 

        return False
        