class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # my solution using division
#         product = 1
#         zeroCount = 0
#         for number in nums:
#             if number != 0:
#                 product = product * number
#             else:
#                 zeroCount+=1
#         ans = []
#         if zeroCount >1:
#             return [0]*len(nums)
#         elif zeroCount == 1:
#             for number in nums:
#                 if number != 0:
#                     ans.append(0)
#                 else:
#                     ans.append(product)
#         else:
            
#             for number in nums:
#                 ans.append(product//number)
#         return ans

        # using the prefix and postfix method to compute the product. neetcode solution.
        result = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= postfix
            postfix *= nums[i]
        return result
