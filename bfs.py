from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.edges=defaultdict(list)
    def addedge(self,start,end):
        self.edges[start].append(end)
    def bfs(self,start):
        visited=[False]*(len(self.edges))
        queue=[]
        visited[start]=True
        queue.append(start)
        while queue:
            top=queue.pop(0)
            print(top)
            for i in self.edges[top]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
n=int(input("Enter the Number of Vertices "))
obj=Graph(n)
n=int(input("Enter the Number of Edges"))
for i in range(n):
    obj.addedge(int(input()),int(input()))
print("The Breadth First Search ")
obj.bfs(int(input()))



        
        
    
