from collections import defaultdict
class Solution:
    def groupStrings(self, strings):
        diffMap = defaultdict(list)
        res = []
        for string in strings:
            tmp = ""
            for i in range(len(string)-1):
                # minus values -> 26+val
                if ord(string[i+1]) - ord(string[i])<0:
                    tmp += str(ord(string[i+1]) - ord(string[i])+26)
                else:
                    tmp += str(ord(string[i+1]) - ord(string[i])) 
                tmp+="."
            diffMap[tmp].append(string)
        print(diffMap)
        for k in diffMap.keys():
            # print("here", k)
            tmp = []
            for item in diffMap[k]:
                tmp.append(item)
            res.append(tmp)

        return res