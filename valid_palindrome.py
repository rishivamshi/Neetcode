class Solution:
    def isPalindrome(self, s: str) -> bool:
        procString = ""
        # print(ord("A"))
        # print(ord("Z"))
        # print(ord("a"))
        # print(ord("z"))
        print(ord("9"))
        for i in range(len(s)):
            if (ord(s[i])>=65 and ord(s[i])<=90):
                procString += chr(ord(s[i])+32)
            elif (ord(s[i])>=97 and ord(s[i])<=122):
                procString += s[i]
            elif (ord(s[i])>=48 and ord(s[i])<=57):
                procString += s[i]
        for i in range(len(procString)//2):
            if(procString[i]!=procString[len(procString)-1-i]):
                return False
            
        
        return True
