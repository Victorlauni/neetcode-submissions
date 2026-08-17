class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productPre = [1]*len(nums)
        productPost = [1]*len(nums)
        for i in range(len(nums)-1):
            productPre[i+1] = productPre[i] * nums[i]
            productPost[-(i+2)] = productPost[-i-1] * nums[-i-1]

        result = []
        for i in range(len(nums)):
            result.append(productPre[i] * productPost[i])
        return result