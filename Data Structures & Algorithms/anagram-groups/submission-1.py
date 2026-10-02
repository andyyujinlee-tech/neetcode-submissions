class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                alp_num = ord(c) - ord('a')
                count[alp_num] = count[alp_num] + 1
            result[tuple(count)].append(s)
        return list(result.values())