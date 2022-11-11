    def removeElement(self, nums: List[int], val: int) -> int:
        count = nums.count(val)
        for i in range(0,count):
            nums.remove(val)

        return len(nums)
