class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        merged.append(intervals[0])

        order = 0
        for i in range(1, len(intervals)):
            if merged[order][1] >= intervals[i][0]:
                merged[order][1] = max(merged[order][1], intervals[i][1])
            else:
                merged.append(intervals[i])
                order += 1
        
        return merged
