class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            #pop until we maintain the montonic decreasing stack order
            while stack and temperatures[i] > stack[-1][1]:
                temp = stack.pop()
                result[temp[0]] = i - temp[0]
            stack.append([i,temperatures[i]])
        return result 