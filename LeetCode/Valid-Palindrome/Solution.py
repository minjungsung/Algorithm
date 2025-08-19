class Solution:
    def isPalindrome(self, s: str) -> bool:
        small = s.lower()
        filtered = []
        for char in small:
            if char.isalnum():
                filtered.append(char)
        for index in range(len(filtered)//2):
            if filtered[index] != filtered[-index-1]:
                return False
            
        return True
        