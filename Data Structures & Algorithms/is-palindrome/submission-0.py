class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = [c.lower() for c in s if c.isalnum()]
        reverse_list = s_list.copy()
        reverse_list.reverse()
        return s_list == reverse_list

    