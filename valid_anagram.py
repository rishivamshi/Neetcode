class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # using hashmap of array of size ascii characters
        
        # hashMap = [0]*128
        # for letter in s:
        #     hashMap[ord(letter)]+=1
        # for letter in t:
        #     hashMap[ord(letter)]-=1
        # for asci in hashMap:
        #     if asci != 0:
        #         return False
        # return True
        
        # using dictionary
        d = {}
        for letter in s:
            if letter in d:
                d[letter]+=1
            else:
                d[letter] =1
        for letter in t:
            if letter in d:
                d[letter]-=1
            else:
                d[letter]=1
        
        for key in d:
            if d[key] != 0:
                return False
        return True
