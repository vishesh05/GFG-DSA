
class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        j=0
        ans=0
        for i in range(n):
            if arr[i] > dep[j]:
                j+=1
            else:
                ans+=1
        return ans
