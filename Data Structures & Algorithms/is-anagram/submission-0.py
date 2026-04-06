class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_int_array = sorted([ord(k) for k in s]) 
        second_int_array = sorted([ord(k) for k in t])

        if first_int_array == second_int_array: 
            return True
        return False

        