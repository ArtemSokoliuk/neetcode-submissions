class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num1_index = 0
        num2_index = len(numbers)-1 
        while num1_index < num2_index:
            curr_sum = numbers[num1_index] + numbers[num2_index]
            if curr_sum == target:
                return [num1_index+1, num2_index+1]
            elif curr_sum > target:
                num2_index -= 1
            else:
                num1_index += 1
        return [num1_index+1, num2_index+1]