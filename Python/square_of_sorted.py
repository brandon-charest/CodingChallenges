import collections

class Solution:
    def sortedSquares(self, A):
        #double ended queue
        result = collections.deque()
        leftPointer = 0
        rightPointer = len(A)-1

        while leftPointer <= rightPointer:
            left, right = abs(A[leftPointer]), abs(A[rightPointer])
            if left > right:
                result.appendleft(left*left)
                leftPointer += 1
            else:
                result.appendleft(right*right)
                rightPointer -= 1

        return list(result)

if __name__ == "__main__":
    test =  [-4,-1,0,3,10]

    print(Solution.sortedSquares(__name__,test))