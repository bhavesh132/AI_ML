import math

# Maximum and Minimum value
maximum, minimum = 10000000, -10000000

def alpha_beta(curr_depth, node, total_depth, maxP , score, max_v, min_v):
    if (curr_depth == total_depth):
        return score[node]
    
    if maxP:
        best = min_v
        for i in range(0,total_depth-1):
            value = alpha_beta(curr_depth+1, node*2+i, total_depth, False, score, max_v, min_v)
            best = max(best, value)
            max_v = max(max_v, best)
            if(min_v <= max_v):
                break
        return best
   
    else:
        best = max
        for i in range(0, total_depth-1):
            value = alpha_beta(curr_depth+1, node*2+i, total_depth, True, score, max_v, min_v)
            best = min(best, value)
            min_v = min(min_v, best)
            if(min_v <= max_v):
                break
        return best


score = []
x = int (input("Total Number of Leaf Nodes: "))

for i in range(x):
    y = int(input(f"Enter {i+1}th node value: "))
    score.append(y)

curr_depth = int(input("Enter current Depth: "))
total_depth = int(math.log(len(score),2))
node = int(input("Enter current Node: "))

print("The optimal value is: ", alpha_beta(curr_depth, node, total_depth, True, score, maximum, minimum))