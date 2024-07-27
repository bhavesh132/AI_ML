ad_max = [
    #0 1 2 3 4 5
    [0,1,1,1,0,0],#0
    [1,0,0,0,1,1],#1
    [1,0,0,0,0,1],#2
    [1,0,0,0,0,0],#3
    [0,1,0,0,0,0],#4
    [0,1,1,0,0,0] #5
]

visited = [0,0,0,0,0,0]

def dfs(n):
    if visited[n] != 0:
        return
    else:
        visited[n] = 1
        num = 0
        for relation in ad_max[n]:
            if relation != 0:
                dfs(num)
            num = num + 1 
        print(n)

src_node = int(input("Enter starting Node: "))

dfs(src_node)