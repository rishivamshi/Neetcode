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

from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        # adding number into dictionary
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num] = 1
        #finding the highest most repeated element to get the size of the array
        maxRepeat = 0
        for key in d:
            if d[key]>=maxRepeat:
                maxRepeat = d[key]
        # print(maxRepeat)
        # creating a dictionary of values to key and key to values of d
        d1= defaultdict(list)
        for key in d:
            if d[key] in d1:
                d1[d[key]] = d1[d[key]] + [key]
            else:
                d1[d[key]] = [key]
        # print(d1)
        
        #initiating the final sorted array of bucket sort
        n = [[]]*(maxRepeat+1)
        for key in d1:
            n[key] = d1[key]
        ans = []
        print(n)
        count = 0
        # to append and return the final answer
        for i in range(len(n)-1,0,-1):
            if count==k:
                break
            for j in range(len(n[i])):
                ans.append(n[i][j])
                count+=1

        return ans



from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #my code
#         d = {}
#         # adding number into dictionary
#         for num in nums:
#             if num in d:
#                 d[num]+=1
#             else:
#                 d[num] = 1
#         #finding the highest most repeated element to get the size of the array
#         maxRepeat = 0
#         for key in d:
#             if d[key]>=maxRepeat:
#                 maxRepeat = d[key]
#         # print(maxRepeat)
#         # creating a dictionary of values to key and key to values of d
#         d1= defaultdict(list)
#         for key in d:
#             if d[key] in d1:
#                 d1[d[key]] = d1[d[key]] + [key]
#             else:
#                 d1[d[key]] = [key]
#         # print(d1)
        
#         #initiating the final sorted array of bucket sort
#         n = [[]]*(maxRepeat+1)
#         for key in d1:
#             n[key] = d1[key]
#         ans = []
#         print(n)
#         count = 0
#         # to append and return the final answer
#         for i in range(len(n)-1,0,-1):
#             if count==k:
#                 break
#             for j in range(len(n[i])):
#                 ans.append(n[i][j])
#                 count+=1

#         return ans


        # neetcode code 
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            count[n] = 1+count.get(n,0)
        for n,c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
