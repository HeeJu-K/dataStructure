class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve( A, B):
        sum = 0
        for i in range (B):
            sum += A[i]
        print("sum: ", sum)
        newSum = sum
        for j in range (B):
            newSum = newSum - A[B-j-1] + A[len(A)-1-j]
            print("newsum: ", newSum)
            if newSum > sum:
                sum = newSum
            print("sum after comp: ", sum)
        return sum

if __name__ == '__main__':
    print("result: ", Solution.solve( [5, -2, 3, 1, 2], 3))