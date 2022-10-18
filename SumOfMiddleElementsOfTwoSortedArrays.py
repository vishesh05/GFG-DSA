
class Solution:
    def findMidSum(self, ar1, ar2, n): 
        # code here 
        for i in range(len(ar1)):
            ar1.append(ar2[i])
        ar1.sort()
        return ar1[n-1]+ar1[n]
            
