"""
https://leetcode.com/discuss/interview-question/492652/microsoft-oa-2019-plane-seat-reservation
"""
import string


class Solution:
    @staticmethod
    def check_aisle(arr, middle_open=False):
        if middle_open:
            return sum(arr[1:3]) == 0 and sum(arr[5:9]) == 0
        else:
            return sum(arr[1:3]) == 0 or sum(arr[5:9]) == 0

    @staticmethod
    def check_middle(arr):
        return sum(arr[3:7]) == 0

    @staticmethod
    def build_reserve(arr):
        dic = {}
        for t in arr:
            if t[0] not in dic:
                dic[t[0]] = t[1]
            else:
                dic[t[0]] += t[1]
        return dic

    def solution(self, N: int, S: string) -> int:
        seat_chart = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'J': 8, 'K': 9}
        row_temp = [0,0,0,0,0,0,0,0,0,0]
        temp = S.split(' ')
        reserv = self.build_reserve(temp)
        found = 0

        for row in reserv.values():
            temp = row_temp.copy()
            for seat in row:
                temp[seat_chart[seat]] = 1
            if self.check_middle(temp):
                found += 1
                if self.check_aisle(temp, middle_open=True):
                    found += 1
            elif self.check_aisle(temp):
                found += 1
        # two seating possibilities for all rows not used
        for i in range(1, N+1):
            if str(i) not in reserv:
                found += 2
        print(found)
        return found


rows = 5
res = '1A 2F 1C 4A 3C 3E 3K 4K'
s = Solution()
s.solution(rows, res)
