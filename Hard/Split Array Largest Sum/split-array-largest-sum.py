#User function Template for python3

class Solution:
    def check(self,arr,mid):
        
        summ = 0
        count = 1
        for i in range(len(arr)):
            if summ+arr[i]<=mid:
                summ+=arr[i]
            else:
                count+=1
                summ = arr[i]
            
               
        return count 
           
    def splitArray(self, arr, N, K):
        if K>N:
            return -1
        low = max(arr)
        high = sum(arr)
        while low<=high:
            mid = (low+high)//2
            need=self.check(arr,mid)
            if  need>K:
                low = mid+1
            else:
                high = mid-1
        return low        
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.splitArray(arr,N,K))
# } Driver Code Ends