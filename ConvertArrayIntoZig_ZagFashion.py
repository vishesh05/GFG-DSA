class Solution:
    def zigZag(self,arr, n):
        # code here
        c=0
        for i in range(len(arr)):
            if i+1== len(arr):
                break
            if i%2==0 and arr[i] > arr[i+1]:
                arr[i], arr[i+1]= arr[i+1], arr[i]
            elif i%2==1 and arr[i]<arr[i+1]:
                arr[i], arr[i+1]= arr[i+1], arr[i]
        return arr
                
