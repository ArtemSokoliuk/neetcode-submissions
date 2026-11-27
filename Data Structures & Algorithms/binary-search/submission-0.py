class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1

        while start <= end:
            mid_index = (start+end)//2
            curr_val = nums[mid_index]

            if curr_val == target:
                return mid_index
            elif curr_val > target:
                end = mid_index-1
            elif curr_val < target:
                start = mid_index+1
        
        return -1
