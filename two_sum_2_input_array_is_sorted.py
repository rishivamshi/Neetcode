class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # my solution
        first = 0
        last = len(numbers)-1
        ans = []
        prevLast = last
        while(first < last):
            diff = target - numbers[first]
            if diff > numbers[last]:
                prevLast = last
                last+=1
                
                if last ==len(numbers):
                    last-=1
                    first+=1
            elif diff < numbers[last]:
                
                last-=1
                if last == prevLast:
                    first +=1
                    
                if last==first:
                    last = len(numbers)-1
                    first+=1
            else:
                ans.append(first+1)
                ans.append(last+1)
                break

        return ans
