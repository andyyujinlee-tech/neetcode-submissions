class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        #loop through
        for s in strs:
            sort = ''.join(sorted(s))

            result[sort].append(s)
        return list(result.values())