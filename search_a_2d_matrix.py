class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # this solution is to change the 2d matrix to linear and then applying binary search on it
        # combined = []
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         combined.append(matrix[i][j])
        # start = 0
        # end = len(combined)-1
        

        # while(start<=end):
        #     mid = (start+end)//2
        #     print(mid)
        #     if combined[mid] == target:
        #         return True
        #     elif combined[mid] < target:
        #         start = mid+1
        #     else:
        #         end = mid-1
        # return False

        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
