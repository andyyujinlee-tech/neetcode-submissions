class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)

        for num in nums:
            dic[num] = dic[num] + 1
        #[number | count]

        arr = []
        for num, count in dic.items():
            arr.append([count,num])
        arr.sort(reverse=True)

        result = []

        for i in range(k):
            result.append(arr[i][1])
        return result
        




