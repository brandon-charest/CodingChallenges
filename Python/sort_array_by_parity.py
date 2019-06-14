



class Solution(object):
    def sortArrayByParity(self, A):
        size = len(A)
        if size < 2:
            return A
        slow = 0
        fast = 1

        while fast < size:
            if A[slow] % 2 == 0:
                slow += 1
            elif A[fast] % 2 == 0:
                A[slow], A[fast] = A[fast], A[slow]
                slow += 1
            fast += 1
        return A
