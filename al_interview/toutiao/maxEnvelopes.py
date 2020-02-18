from typing import *


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if len(envelopes) == 0:
            return -1
        envelopes = sorted(envelopes, key=lambda x: x[0])
        res = []
        max_count = 0
        for i in range(len(envelopes)):

            for j in range(i + 1, len(envelopes)):
                if j[0] > i[0] and j[1] > i[1]:
                    pass


