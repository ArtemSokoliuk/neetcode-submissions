class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_normalised = "".join([i.lower() for i in s if i.isalnum()])

        if str_normalised == str_normalised[::-1]:
            return True

        return False