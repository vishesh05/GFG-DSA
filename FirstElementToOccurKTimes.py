

class Solution:
    def firstElementKTime(self,  a, n, k):
        # code here
        map = dict()
        for ele in a:
            map[ele] = map.get(ele,0) + 1
            if map[ele] == k:
                return ele
        return -1
    

