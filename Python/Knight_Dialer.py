""" 935. Knight Dialer
This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight
makes N-1 hops.  Each hop must be from one key to another numbered key.

Each time it lands on a key (including the initial placement of the knight), it presses the number
of that key, pressing N digits total.

How many distinct numbers can you dial in this manner?

Since the answer may be large, output the answer modulo 10^9 + 7.
"""


def knight_dialer(N: int) -> int:
    if N <= 0:
        return 0

    lookup = {}
    total = 0
    MOD = 10 ** 9 + 7
    neighbors = {
        0: {4, 6},
        1: {6, 8},
        2: {7, 9},
        3: {4, 8},
        4: {0, 3, 9},
        5: {},
        6: {0, 1, 7},
        7: {2, 6},
        8: {1, 3},
        9: {2, 4}
    }

    def get_neighbor(keypad_num):
        return neighbors[keypad_num]

    def count_sequences(position, hop_num):
        val = (position, hop_num)
        if hop_num == 0:
            return 1
        if val in lookup:
            return lookup[val]
        count = 0
        for p in get_neighbor(position):
            count += count_sequences(p, hop_num-1)

        lookup[val] = count
        return lookup[val]

    for i in range(10):
        total += count_sequences(i, N-1)
    return total % MOD


print(knight_dialer(3))