class Solution(object):
    def threeSum( nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        Negative, Positive, Zero = [], [], []
        for num in nums:
            if num>0:
                Positive.append(num)
            elif num == 0:
                Zero.append(num)
            else:
                Negative.append(num)
        output = []
        if len(Zero) > 2:
            output.append([0,0,0])
            print ("+ 0 -", Positive, Negative, Zero)
        elif len(Zero):
            for i in range (0, len(Positive)):

                if -1*Positive[i] in Negative:
                    if len(Positive) > 1 and i+1<len(Positive) and Positive[i] == Positive[i+1]:
                        continue
                    output.append([Positive[i], 0, -1*Positive[i]])

        for i in range (0, len(Positive)):
            for j in range (i+1, len(Positive)):
                target = -1*(Positive[i]+Positive[j])
                if target in Negative:
                    output.append([Positive[i], Positive[j], target])
        for i in range (0, len(Negative)):
            for j in range (i+1, len(Negative)):
                target = -1*(Negative[i]+Negative[j])
                if target in Positive:
                    output.append([Negative[i], Negative[j], target])

        return output

    nums = [-2,0,0,2,2]
    print("output", threeSum(nums))