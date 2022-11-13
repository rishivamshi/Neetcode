    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            if operation == "C":
                stack.pop()
            elif operation == "D":
                prev_score = stack.pop()
                stack.append(prev_score)
                stack.append(prev_score*2)
            elif operation == "+":
                first_prev_score = stack.pop()
                second_prev_score = stack.pop()
                stack.append(second_prev_score)
                stack.append(first_prev_score)
                stack.append(first_prev_score + second_prev_score)
            else:
                stack.append(int(operation))
        
        total_score=0
        while(len(stack) != 0):
            total_score += stack.pop()
            
        return total_score
