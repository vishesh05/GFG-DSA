class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        arr=[]

        arr.append(A[N-1])

        for i in range(N-2, -1, -1):

            l=len(arr)

          

            if arr[l-1]<=A[i]:


                arr.append(A[i])

        

        arr1=arr[::-1]

        return arr1
                
                