class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(0,len(s)):
            stack.append(s[i])
        
        ans = []
        i = 0
        while(i <= len(stack)):
            bracket = stack[i]
            print(bracket)
            if bracket == "(":
                ans.append(bracket)
            elif bracket == "[":
                ans.append(bracket)
            elif bracket == "{":
                ans.append(bracket)
            elif bracket == ")":
                if(len(ans)==0):
                    return False
                open_bracket = ans.pop()
                if open_bracket != "(":
                    return False
            elif bracket == "]":
                if(len(ans)==0):
                    return False
                open_bracket = ans.pop()
                if open_bracket != "[":
                    return False
            elif bracket == "}":
                if(len(ans)==0):
                    return False
                open_bracket = ans.pop()
                if open_bracket != "{":
                    return False

                

        if(len(ans)!=0):
            return False
        return True
