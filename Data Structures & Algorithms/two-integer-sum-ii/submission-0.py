class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_idx_map = {}
        for idx, num in enumerate(numbers):
            if target-num in num_idx_map: 
                return [num_idx_map[target-num]+1, idx+1]
            else:
                num_idx_map[num] = idx
        