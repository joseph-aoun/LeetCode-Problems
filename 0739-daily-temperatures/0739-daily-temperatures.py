class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [[temperatures[0], 0]]
        
        ans = [0]*len(temperatures)
        
        for i in range(1, len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                temp = stack.pop()
                ans[temp[1]] = i - temp[1]
            stack.append([temperatures[i], i])
        return ans