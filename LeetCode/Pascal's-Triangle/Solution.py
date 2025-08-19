class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        result = [[1], [1, 1]]
        print(len(result), numRows)
        while len(result) != numRows:
            target = result[-1]
            new = []
            for i in range(len(target)):
                if i == 0:
                    new.append(1)
                elif i == len(target) - 1:
                    new.append(1 + target[i - 1])
                    new.append(1)
                else:
                    new.append(target[i - 1] + target[i])
            result.append(new)
            print(result)
        return result
                    




        