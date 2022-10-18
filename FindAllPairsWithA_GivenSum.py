
class Solution:
    def allPairs(self, A, B, N, M, X):
        # Your code goes here 
        l=[]
        sum=0
        a,b =0,0
        for i in range(N):
            for j in range(M):
                sum=A[i]+B[j]
                if sum == X:
                    l.append([A[i],B[j]])
        l.sort()
        return l
                    
                

