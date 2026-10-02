class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        top = 0 
        bot = rows - 1

        while top <= bot:
            mid_row = (top + bot) // 2
            print(mid_row)
            if matrix[mid_row][-1] < target:
                top = mid_row + 1
            elif matrix[mid_row][0] > target:
                bot = mid_row - 1
            else:
                break

        if not (top <= bot):
            return False
        
        l = 0
        r = columns - 1
        row = (top + bot) //2
  

        while l <= r:
            mid = (l+r) // 2
            if matrix[row][mid] > target:
                r = mid -1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True

        return False

            
            
                