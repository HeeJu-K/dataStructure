def maximumProductSum(memory):
    l = len(memory)
    for i in range(l//2):
        memory[i], memory[l-i-1] = min(memory[i], memory[l-i-1]), max(memory[i], memory[l-i-1])
    print(memory)
    return sum((i+1)*memory[i] for i in range (l))

mem = [3, 2, 1, 2, 4, 4, 1, 5]
ans = maximumProductSum(mem)
print("here", ans)