class Solution:
    

    
    def numberOfSteps(self, num: int) -> int:
        def helpers(num,count):
            if(num == 0):
                return count
            if (num%2==0):
                count+=1
                return helpers(num//2,count)
            else:
                count+=1
                return helpers(num-1,count)
        count = 0
        n = helpers(num,count)
        print(n)
        return n
        
