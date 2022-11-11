class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(0,len(nums)-1):
            if (nums[i] == nums[i+1]):
                nums[i]='dummy'
        i = 0
        j = 1
        while i < len(nums) and j < len(nums):
            if nums[i] == 'dummy':
                if nums[j] != 'dummy':
                    nums[i] = nums[j]
                    nums[j] = 'dummy'
                    
                    j+=1
                    i+=1
                else:
                    j+=1
            else:
                i+=1
                j+=1
        count = 0
        for i in range(0,len(nums)):
            if nums[i] != 'dummy':
                
                count+=1
                
        # print(nums)
        # print(count)
        return count
