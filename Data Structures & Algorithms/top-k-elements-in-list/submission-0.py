class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)

        for num in nums:
            dic[num] = dic[num] + 1
        #dictinoary built complete


        sorted_dict_desc = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))

        result = []
        counter = 0
        for val in sorted_dict_desc:
            if counter >= k:
                break
            result.append(val)
            counter += 1
        return result


        