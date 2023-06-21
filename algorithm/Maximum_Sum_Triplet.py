import math
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(A):
        right_max = []
        right_max.insert(0, A[len(A)-1])
        # right = A[len(A)-1]
        for i in range (len(A)):
                right_max.insert(0, max(A[len(A)-1-i], right_max[0]))
        
        print("len(A): ", len(A))
        maxSum = 0
        # right_idx = len(A)-1
        # index = 0
        sortedSet = []
        for i in range(len(A)-1):
            print("for: ", i, A[i])
            sortedSet.append(A[i])
            sortedSet = sorted(sortedSet)
            print("sortedSet: ", sortedSet)
            if A[i] < right_max[i+1]:
                for j in range(i+1):
                    if list(sortedSet)[j] == A[i]:
                        break
                
            # if A[len(A)-1-i] > right:
            #     right = A[len(A)-1-i]
            #     right_idx = len(A)-1-i
            #     print("right: ", right)
            # for j in range(i+1):
            #     if j < right_idx:
            #         print("j: ", j, " right_idx:", right_idx)
            #         # list(sortedSet)[j]
            #         if list(sortedSet)[j] == A[i]:
            #             index = j
            #             print("index: ", index, A[i])
            # # index = sortedSet.find(A[i])
            # print("check if: ", i, index, A[i]+right+list(sortedSet)[index-1], maxSum, A[i], right, list(sortedSet)[index-1])
            if i != 0 and j!=0 and A[i]+right_max[i+1]+list(sortedSet)[j-1] > maxSum and A[i]<right_max[i+1] and list(sortedSet)[j-1]<A[i]:
                maxSum = A[i]+right_max[i+1]+list(sortedSet)[j-1]
                print("maxSum: ", maxSum, "from ", list(sortedSet)[j-1], "+", A[i], "+", right_max[i+1])
        return maxSum
if __name__ == '__main__':
    print(Solution.solve([ 22649, 27447, 23806, 15891, 6730, 24371, 15351, 15007, 31102, 24394, 3549, 19630, 12624, 24085 ]))
    # print(Solution.solve( [ 25668, 26300, 17036, 9895, 28704, 23812, 31323, 30334, 17674, 4665, 15142, 7712, 28254, 6869, 25548, 27645, 32663, 32758, 20038, 12860, 8724, 9742, 27530, 779, 12317, 3036, 22191, 1843, 289, 30107, 9041, 8943 ]))
    # print(Solution.solve([ 154, 293, 12383, 17422, 18717, 19719, 19896, 5448, 21727, 14772, 11539, 1870 ]))
    # print(Solution.solve([18468, 6335, 26501, 19170, 15725, 11479, 29359, 26963, 24465, 5706, 28146, 23282, 16828, 9962, 492, 2996, 11943, 4828, 5437, 32392, 14605]))