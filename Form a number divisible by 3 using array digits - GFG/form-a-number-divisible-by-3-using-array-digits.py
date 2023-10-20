#User function Template for python3

class Solution:
    def isPossible(self, N, arr):
        # code here
        # i = 0
        # j = N-1
        # count = 0
        # while i<=j:
        #     if int(str(arr[i])+str(arr[j]))%3 == 0:
        #         count+=1
        #     elif int(str(arr[j])+str(arr[i]))%3 == 0:  
        #         count+=1
        # return count
        if sum(arr)%3 == 0:
            return 1
            
        return 0



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.isPossible(N, arr))
# } Driver Code Ends