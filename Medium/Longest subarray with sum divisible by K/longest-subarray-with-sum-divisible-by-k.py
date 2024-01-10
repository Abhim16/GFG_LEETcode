#User function Template for python3
# class Solution:
# 	def longSubarrWthSumDivByK (self,arr,  n, K) : 
# 		#Complete the function
# 		sumi = sum(arr)
	
# 		front,rear = 0,len(arr)
# 		while front<=rear:
# 		    if sumi%K == 0:
# 		        return rear-front
# 		    if sumi-rear%K !=0:
# 		        n-=1
# 		        rear-=1
# 		    else:
# 		        n-=1
# 		        return n
# 		    if sumi-front%K !=0:
# 		        n-=1
# 		        front+=1
# 		    else:
# 		        n-=1
# 		        return n
#         return -1       

class Solution:
    def longSubarrWthSumDivByK (self,arr,  n, k) : 
		#Complete the function
        m = {0:-1}
        running, ans = 0, 0
        for i, e in enumerate(arr):
            running = (running+e)%k
            if running not in m:
                m[running] = i
            else:
                ans = max(ans, i-m[running%k])

        return ans  # Return -1 if no valid subarray is found




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	for _ in range(0,int(input())):
		n, K = map(int ,input().split())
		arr = list(map(int,input().strip().split()))
		ob = Solution()
		res = ob.longSubarrWthSumDivByK(arr, n, K)
		print(res)




# } Driver Code Ends