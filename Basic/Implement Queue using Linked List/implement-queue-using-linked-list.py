# A linked list (LL) node 
# to store a queue entry 
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    
    def __init__(self):
        self.front=None
        self.rear=None
        self.sz=0
    
    #Function to push an element into the queue.
    def push(self, item): 
        temp=Node(item)
        if self.rear==None:
            self.front=temp
        else:
            self.rear.next=temp
        self.rear=temp
        self.sz+=1
    
    #Function to pop front element from the queue.
    def pop(self):
        if self.front==None:
            return -1
        else:
            res=self.front.data
            self.front=self.front.next
            if self.front==None:
                self.rear=None
            self.sz-=1
            return res



         
         #add code here


#{ 
 # Driver Code Starts

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   
# } Driver Code Ends