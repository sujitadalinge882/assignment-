#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#You are given a graph and a number x as input. Your task is to print the DFS traversal nodes of the input graph starting
#from node x. Complete the following function in order to give the required output.

#Input Format:

#The first line of input contains a list containing sets representing a graph. The second line of input contains 
#the number x. 

#Output Format:

#Complete the function in order to return the required output.

#Sample Input 0:

#[[1,0],[2,0],[3,0],[3,2]]

#3

#Sample Output 0:

#3 0 2 


n=int(input("Enter the number of elemnts:: "))
graph=[]
for i in range(n):
    graph.append(list(map(int,input("Enter two elements as space seperated ").split())))
print(graph)

x=[]
for i in graph:
    x.extend(i)
nodes=list(set(x))
print(nodes)
 

d_graph={}
for i in range(len(graph)):
    if graph[i][0] in d_graph.keys():
        t= graph[i][1]
        d_graph[graph[i][0]].append(t)
    else:
        d_graph.update({graph[i][0]:[graph[i][-1]]})
print(d_graph)

for i in nodes:
    if i not in d_graph.keys():
        d_graph.update({i:[]})
print(d_graph)


visited_root = set()
root=int(input("enter the root node"))   
def Depth_First_Sesrch(visited_root,graph, root):
    if root not in visited_root:
        print (root,end=' ')
        visited_root.add(root)
        for node in d_graph[root]:
            Depth_First_Sesrch(visited_root, graph, node)


Depth_First_Sesrch(visited_root,d_graph, root)


# In[ ]:




