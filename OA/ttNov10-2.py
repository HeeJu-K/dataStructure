def getMessageStatus(n, timestamps, messages, k):
    res = []
    d = {}
    
    for i in range(n):
        print("d", d)
        if messages[i] in d:
            if timestamps[i] - d[messages[i]] < k:
                res.append("false")
            else:
                res.append("true")
        else: 
            res.append("true")
        d[messages[i]] = timestamps[i]
    return res

t = [1, 4, 5, 10, 11, 14]
m = ["hello", "bye", "bye", "hello", "bye", "hello"]
ans = getMessageStatus(6, t, m, 5)
print(ans)