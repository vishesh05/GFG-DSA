
class Solution:    
    def binarysearch(self, arr, n, k):
        # code here
        z=0
        for i in range(len(arr)):
            if arr[i]==k:
                z=i
        if arr[z]==k:
            return z
        else:
            return -1
                
                  
