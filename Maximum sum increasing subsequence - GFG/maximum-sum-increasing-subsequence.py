#User function Template for python3
class Solution:
    def maxSumIS(self, Arr, n):
        Arr=[0]+Arr
        dp=[0]*(n+1)
        for i in range(1,n+1):
            mx=-float('inf')
            for j in range(i):
                if Arr[j]<Arr[i] and mx<dp[j]+Arr[i]:
                    mx=dp[j]+Arr[i]
            dp[i]=mx
        return max(dp)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxSumIS(Arr,n)
		print(ans)

# } Driver Code Ends