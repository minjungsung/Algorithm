class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = 0
        if len(digits) == 0:
            return result
        for index in range(len(digits)):
            result += digits[-index -1] * (10**index)
        result += 1
        final = []

        while result >= 10:
            remaining = result % 10
            final.insert(0,remaining)
            result = result // 10
        final.insert(0,result)
        return final
            

        