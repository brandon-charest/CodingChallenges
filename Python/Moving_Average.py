"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:
1 MovingAverage m = new MovingAverage(3);
2 m.next(1) = 1
3 m.next(10) = (1 + 10) / 2
4 m.next(3) = (1 + 10 + 3) / 3
5 m.next(5) = (10 + 3 + 5) / 3
"""


class MovingAverage:
    def __init__(self, size: int):
        self._size = size
        self._arr = []
        self._sum = 0

    def next(self, val: int) -> float:
        self._sum += val
        self._arr.append(val)

        if len(self._arr) > self._size:
            self._sum -= self._arr.pop(0)
        avg = round(self._sum/len(self._arr),2)
        print(f"Average: {avg}")
        return avg

    def display(self):
        print("Values stored: ")
        for i in self._arr:
            print(i, end=" ")


m = MovingAverage(3)
m.next(5)
m.next(3)
m.next(1)
m.next(10)
m.next(2)

m.display()





