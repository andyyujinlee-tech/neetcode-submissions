class TimeMap:


    def __init__(self):
        self.dic = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        
        key_list = self.dic.get(key,[])
        #[[1,happy],[3,sad]]
 

        l = 0
        r = len(key_list) - 1
        mid = -1

        while l <= r: 
            mid = (l + r) // 2
            if timestamp >= key_list[mid][0]:
                l = mid + 1
            else:
                r = mid - 1
        if r == -1:
            return "" 

        return key_list[r][1]

