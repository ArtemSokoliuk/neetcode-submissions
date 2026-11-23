class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_normalised = "".join([i.lower() for i in s if i.isalnum()])
        str_rev = str_normalised[::-1]

        if str_normalised == str_rev:
            return True

        return False