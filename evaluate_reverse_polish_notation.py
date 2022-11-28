class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbols = ["+","*","-","/"]
        stack = []
        for token in tokens:
            if token not in symbols:
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                if token == "+":
                    a = a+b
                elif token == "*":
                    a = a*b
                elif token == "/":
                    if a > 0 and b>0:
                        a = b//a
                    else:
                        a = b/a
                        if a > 0:
                            a = math.floor(a)
                        else:
                            a = math.ceil(a) 
                elif token == "-":
                    a = b-a
                stack.append(a)
            
        
        return stack.pop()
