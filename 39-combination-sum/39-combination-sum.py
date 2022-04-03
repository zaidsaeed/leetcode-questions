class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        for i in range(0, len(candidates)):
            if candidates[i] == target:
                ans.append([candidates[i]])
            elif candidates[i] < target:
                queue = [([candidates[i]], candidates[i], i)]
                while queue:
                    elem = queue.pop(0)
                    if elem[1] == target:
                        ans.append(elem[0])
                    elif elem[1] < target:
                        for j in range(elem[2], len(candidates)):
                            elemToAdd = candidates[j]
                            newArr = elem[0][:]
                            newArr.append(elemToAdd)
                            queue.append((newArr, (elem[1] + elemToAdd), j))
        return ans
            
        
                 #                      [2,3,5]
          #         [2]                 [3]             [5]
          #  [2,2]  [2,3] [2,5]