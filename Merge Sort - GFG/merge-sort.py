#User function Template for python3

class Solution:
    def mergeSort(self,arr, l, r):
        #code here
            if len(arr)>1:
                mid=len(arr)//2
                L=arr[:mid]
                R=arr[mid:]
                self.mergeSort(L,l,r)
                self.mergeSort(R,l,r)
                i=j=k=0

#computing value in arr

                while i<len(L) and j<len(R):
                    if R[j]>=L[i]:
                        arr[k]=L[i]
                        i+=1
                    else:
                        arr[k]=R[j]
                        j+=1
                    k+=1

#adding for remaining left
                while i<len(L):
                    arr[k]=L[i]
                    i+=1
                    k+=1


                while j<len(R):
                    arr[k]=R[j]
                    j+=1
                    k+=1
            return
        
        #code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends