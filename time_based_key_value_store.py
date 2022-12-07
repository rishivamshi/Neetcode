class TimeMap:

    def __init__(self):
        
        self.table = {}
        self.maxf = 0

    def set(self, key: str, value: str, timestamp: int) -> None:
        pair = (key, timestamp)
        self.table[pair] = value
        self.maxf = max(self.maxf,timestamp)
        # print(self.table)

    def get(self, key: str, timestamp: int) -> str:
        start = 1
        end = self.maxf
       
        if timestamp > end:
            while(end > 0):
                if (key,end) in self.table:
                    return self.table[(key,end)]
                else:
                    end-=1


        while(timestamp > 0):
            if (key,timestamp) in self.table:
                
                return self.table[(key,timestamp)]
            else:
                timestamp-=1
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
