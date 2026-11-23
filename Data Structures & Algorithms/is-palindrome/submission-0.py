class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleared_s_list = [i.lower() for i in s if i.isalnum()]
        return cleared_s_list == cleared_s_list[::-1]