#User function Template for python3

class Solution: 
    # def select(self, arr, i):
        # code here 
        # n = len(arr)
        # for i in range(n):
        #     for j in range(0,n-i-1):
        #         if arr[j] > arr[j+1]:
                    
        #             arr[j],arr[j+1] = arr[j+1],arr[j]
        # return arr            
    
    def selectionSort(self, arr,n):
        #code here
        
        for i in range(n):
            minn = i
            for j in range(i+1,n):
                if arr[minn] > arr[j]:
                    minn = j
                    
            arr[i],arr[minn] = arr[minn],arr[i]    
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends