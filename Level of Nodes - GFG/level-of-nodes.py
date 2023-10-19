#User function Template for python3

class Solution:
    def nodeLevel(self, V, adj, X):
        q= [[0, 0]]
        pos, len1 = 0, 1
        visited = set()

        while pos<len1:
            top, level = q[pos]
            visited.add(top)
            for i in adj[top]:
                if i==X: return level+1
                elif i not in visited:
                    q.append([i, level+1])
                    len1+=1
            pos+=1
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
            adj[b].append(a)
        X=int(input())
        ob = Solution()
        
        print(ob.nodeLevel(V, adj, X))
# } Driver Code Ends