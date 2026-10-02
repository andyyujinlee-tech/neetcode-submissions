class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)


        
        for s in strs:
            count = [0] * 26
            for c in s:
                position = self.alp_position(c)
                count[position] += 1
            result[tuple(count)].append(s)
            
        return list(result.values())
    
    def alp_position(self,c):
        return ord(c) - ord('a')
                