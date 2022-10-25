from collections import defaultdict

class Solution:
    def topKFrequent(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # count = {i:0 for i in range(len(nums))}
        count = defaultdict(int) # defaultdict have values of int
        max = 0

        for num in range(len(nums)):
            count[nums[num]] += 1
            if max < count[nums[num]]:
                max = count[nums[num]]
            print ("debug00", count)
            
        # frequency = dict.fromkeys(range(max+1), []) #when appending on dict.fromkeys, it will append to every objects so avoid using this
        frequency = { x:[] for x in range( len(nums)+1) }  #making dictionary of index 0 to max+1, initialized as {k:[]}
        for i, j in count.items():  #python items() enumerates indices and data
            print("debug 0", i, j, count)
            print("debug 1", frequency, frequency[j])
            frequency[j].append(i)

        solution=[]
        print("debug 2", frequency, len(frequency))
        i = len(frequency)-1
        # for i in range(len(frequency)-1, len(frequency)-k-1, -1):
        while len(solution) != k and i != 0:
            print("debug 3", len(solution), i, k, len(solution) != 0)
            if frequency[i]:
                for j in range((len(frequency[i]))):
                    solution.append(frequency[i][j])
            i -= 1
            
        return solution
        

    nums = [1, 1, 1, 2, 2, 3]
    # nums = [1,2]
    nums = [-1, -1]
    nums = [1]
    k = 1
    # print("res",topKFrequent(nums, 2))
    print(topKFrequent(nums, k))