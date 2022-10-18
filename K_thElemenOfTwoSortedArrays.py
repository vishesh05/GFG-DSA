 
class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        lis=[]
        for i in range(n):
            lis.append(arr1[i])
        for i in range(m):
            lis.append(arr2[i])
        lis.sort()
        k=k-1
        return lis[k]
        
        
        
