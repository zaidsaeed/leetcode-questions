class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        for i in range(0, len(nums)-1):
            pre.append((pre[-1] * nums[i]))
        post = [1]
        for i in range(len(nums)-1, 0, -1):
            post.insert(0, post[0]*nums[i])
        return [(pre[i] * post[i]) for i in range(len(nums))]