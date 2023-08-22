from typing import List


class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        jumps = [1] * len(arr)
        sorted_indexes = sorted(range(len(arr)), key=lambda k: -arr[k])
        for index in sorted_indexes:
            next_index = index + 1
            while next_index <= index + d and next_index < len(arr) and arr[next_index] < arr[index]:
                jumps[next_index] = max(jumps[index] + 1, jumps[next_index])
                next_index += 1

            next_index = index - 1
            while next_index >= index - d and next_index > -1 and arr[next_index] < arr[index]:
                jumps[next_index] = max(jumps[index] + 1, jumps[next_index])
                next_index -= 1
        return max(jumps)
