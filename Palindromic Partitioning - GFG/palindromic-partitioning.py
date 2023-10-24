#User function Template for python3

from collections import Counter
class Solution:
    def palindromicPartition(self, s):
        a = []
        for i in range(1,len(s)+1):
            j = 0
            while(j<len(s)):
                if(j+i<len(s)):
                    x = s[j:j+i]
                    c = x[::-1]
                    if(c==s[j:j+i]): # if palindrome
                        a.append(s[j:j+i])
                    j+=1
                elif(j!=len(s)):
                    x = s[j:len(s)]
                    c = x[::-1]
                    if(c==s[j:len(s)]):
                        a.append(s[j:len(s)])
                    j = len(s)
        count = 0
        x = s
        for i in reversed(range(len(a))):
            if(a[i] in x):
                x = x.replace(a[i],"#")
                cnt = Counter(x)
                count+=cnt["#"]
                if cnt["|"]==len(s):
                    break
                x = x.replace("#","|")
        return count-1




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        string = input()
        
        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends