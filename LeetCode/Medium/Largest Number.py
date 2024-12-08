class Solution:
    def merge_sort(self, ls):
        if len(ls) > 1:
            mid = len(ls) // 2
            left = self.merge_sort(ls[:mid])
            right = self.merge_sort(ls[mid:])
            return self.merge(left, right)
        else: return ls

    def merge(self, left, right):
        ans, i, j = [], 0, 0
        while i < len(left) and j < len(right):
            if Solution.compare(left[i], right[j]):
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                j += 1
        while i < len(left):
            ans.append(left[i])
            i += 1
        while j < len(right):
            ans.append(right[j])
            j += 1
        return ans

    def compare(n1, n2):
        if n1 + n2 > n2 + n1:
            return True
        else:
            return False

    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        sorted_nums = self.merge_sort(nums)
        ans = ''.join(sorted_nums)

        if int(ans) == 0: return '0'
        return ans
