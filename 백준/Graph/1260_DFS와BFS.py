from collections import deque

len_node,len_edge,st_p = map(int,input().split())
adj_lst = [[] for _ in range(len_node+1)]

dfs_done = []
bfs_done = []
for _ in range(len_edge):
    s,e = map(int,input().split())
    adj_lst[s].append(e)
    adj_lst[e].append(s)

for i in range(1,len_node):
    adj_lst[i].sort()

#DFS
dfs_done = [st_p]
def DFS(x,lst):
    global dfs_done
    for i in lst[x]:
        if i not in dfs_done:
            dfs_done.append(i)
            DFS(i,lst)
    return dfs_done
dfs_done = DFS(st_p,adj_lst)
#BFS
next = deque([st_p])
bsf_done = []
while len(next) > 0:
    for _ in range(len(next)):
        now = next.popleft()
        bsf_done.append(now)
        for i in adj_lst[now]:
            if i not in bsf_done and i not in next:
                next.append(i)
for i in dfs_done:
    print(i,end = ' ')
print('')
for i in bsf_done:
    print(i,end = ' ')