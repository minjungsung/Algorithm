class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        result = [[1], [1, 1]]
        while len(result) != rowIndex+1:
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
        return result[-1]
                    