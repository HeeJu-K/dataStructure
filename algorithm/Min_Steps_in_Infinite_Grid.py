class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints( A, B):
        count = 0
        for i in range(len(A)-1):
            # if abs(A[i+1] - A[i]) <= 1 and abs(B[i+1] - B[i]) <= 1:
            #     count+=1
            # else:
            count += max(abs(A[i+1] - A[i]), abs(B[i+1] - B[i]))
                # count += max(abs(A[i+1] - A[i]), abs(B[i+1] - B[i])) - min(abs(A[i+1] - A[i]), abs(B[i+1] - B[i]))
            print("count: ", count)
        return count

if __name__ == '__main__':
    print("Ans: ", Solution.coverPoints([ -4, 1, -4, 8, -11, -12, -13, -3, -4, -4, -14, 7, -2, -2, -5, 5, -1, 0 ], [ -8, -15, -4, 3, 11, 8, -15, 4, 1, 7, 3, 9, -9, -9, -13, 10, -14, -8 ]))