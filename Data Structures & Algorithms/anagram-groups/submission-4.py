class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # loop all string, store them in the character dictionary that counts the number of character occured.
        # the dictionary array hold format of [0] * 26 where each index represent the occurence of the character.

        # If they are the same, they will formed same dictionary, so put that in the value, if key is first time shown, then add


        result_dic = defaultdict(list)

        for s in strs:
            occurance_array = [0] * 26
            for c in s:
                position = ord(c) - ord('a')
                occurance_array[position] += 1

            result_dic[tuple(occurance_array)].append(s)

        return list(result_dic.values())

                