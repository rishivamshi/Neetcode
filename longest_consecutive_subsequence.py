class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # res = 0
        # c = 1
        # count = {}
        # d = {}
        # for i in nums:
        #     d[i] = i+1
        # for i in d:
        #     tmp = i
        #     c = 1
        #     while True:
        #         if d[tmp] in count:
        #             c += count[d[tmp]]
        #             break
        #         if d[tmp] in d:
        #             c+=1
        #         else:
        #             break
        #         tmp = d[tmp]
        #     count[i] = c
        #     if res<c:
        #         res = c
        # return res

        longest = 0
        numSet = set(nums)

        for n in nums:
            if n-1 not in numSet:
                length = 0
                while n+length in numSet:
                    length+=1
                longest = max(longest,length)
        return longest
