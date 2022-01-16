class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [[], nums.copy()]
        elem = nums.pop(len(nums)-1)
        subsets = self.subsets(nums)

        subsetsDup = [subset.copy() for subset in subsets]
        for subset in subsetsDup:
            subset.append(elem)
        subsets = subsets + subsetsDup
        return subsets