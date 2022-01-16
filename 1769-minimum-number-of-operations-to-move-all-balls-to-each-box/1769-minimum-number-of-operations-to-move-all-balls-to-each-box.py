class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0 for i in range(len(boxes))]
        for i in range(0, len(boxes)):
            for j in range(0, len(boxes)):
                if j != i and boxes[j] == '1':
                    res[i] += abs(j-i)
        return res