class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix) -1 

        target_array = -1
        while bot >= top:
            mid = (top + bot) // 2
            print(mid)
            current = matrix[mid]

            first = current[0]
            last = current[-1]

            if target > last:
                top = mid + 1
            elif target < first:
                bot = mid - 1
            else:
                target_array = mid
                break

        l = 0
        r = len(matrix[target_array]) -1 

        while r >= l:
            mid = (r + l) // 2
            current = matrix[target_array][mid]

            if target > current:
                l = mid + 1
            elif target < current:
                r = mid - 1
            else:
                return True
        return False


        
 