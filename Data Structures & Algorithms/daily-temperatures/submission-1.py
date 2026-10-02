class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i,t in enumerate(temperatures):

            while stack and t > temperatures[stack[-1]]:
                stackIndex = stack.pop()
                result[stackIndex] = i - stackIndex
            stack.append(i)
        return result     
                
