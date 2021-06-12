from collections import deque
num_node = int(input())
num_edge = int(input())

adj_lst = [[] for _ in range(num_node+1)]

for i in range(num_edge):
    a,b = map(int,input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)

next = deque([1])
cnt = 0
done = []
while len(next)>0:
    for i in range(len(next)):
        now = next.popleft()
        if now not in done:
            done.append(now)
        cnt += 1
        for j in adj_lst[now]:
            if j not in done:
                next.append(j)
                
print(len(done)-1)  