class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxi = max(piles)
        
        def check(piles,h,a):
            
            count = 0
            for i in range(len(piles)):
                count += math.ceil(float(piles[i]/a))
            if count <= h:
                return True
            return False



        # print(check(piles,h,6))
        start = 1
        while start < maxi:
            mid = (start + maxi)//2
            if check(piles,h,mid) == True:
                maxi = mid
            else:
                start = mid+1
                
        return start
