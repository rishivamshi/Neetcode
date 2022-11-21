from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num] = 1
        ans = []
        q = PriorityQueue()
        for key in d:
            q.put((-1*d[key],key))
        
        while k >0:
            ans.append(q.get()[1])
            k-=1
        return ans
