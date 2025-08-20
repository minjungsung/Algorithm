class Solution:
    def reverseBits(self, n: int) -> int:       
        temp1 =  f"{n:032b}"
        rev = temp1[::-1]
        return int(rev,2)
