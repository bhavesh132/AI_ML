import math

def min_max(curr_depth, node_value, max_turn, score, total_depth):
    if curr_depth == total_depth:
        return score[node_value]
    
    if (max_turn):
        print("Max-turn to choose")
        return max(min_max(curr_depth+1, node_value*2, False, score, total_depth), min_max(curr_depth+1, node_value*2+1, False, score, total_depth))
    
    else: 
        print("Min-turn to choose")
        return min(min_max(curr_depth+1, node_value*2, True, score, total_depth), min_max(curr_depth+1, node_value*2+1, True, score, total_depth))

score = []
x = int(input("Enter the number of leaf nodes: "))

for i in range(x):
    y = int(input(f"Enter the {i+1} Leaf Value: "))
    score.append(y)

total_depth = math.log(len(score),2)

current_depth = int(input("Enter current Depth value: "))

node_value = int(input("Enter the node value: "))

max_turn = True

print("The maximum output is: ", end=" ")
answer = min_max(current_depth, node_value, max_turn, score, total_depth)
print(answer)
