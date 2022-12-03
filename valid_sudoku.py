class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row check 
        for row in board:
            items = set()
            count = 0
            for number in row:
                if number!=".":
                    items.add(number)
                    count+=1
            if len(items) != count:
                print("row issue")
                return False
        for i in range(9):
            items = set()
            count = 0
            for j in range(9):
                if board[j][i]!=".":
                    items.add(board[j][i])
                    count +=1
            if len(items) != count:
                print("column issue")
                return False
        for i in range(0,9,3):
            for j in range(0,9,3):
                items = set()
                count = 0
                piece = []
                piece += board[i][j:j+3]
                piece += board[i+1][j:j+3]
                piece += board[i+2][j:j+3]
                # print(piece)
                # print(type(board[i][j:j+3]))
                for number in piece:
                    if number!= ".":
                        items.add(number)
                        count+=1
                

                # print(board[i][j:j+3])
                # print(board[i+1][j:j+3])
                # print(board[i+2][j:j+3])
                if len(items) != count:
                    return False
                # print("board")
                
                
            # print("space")
        
        

        return True
        
