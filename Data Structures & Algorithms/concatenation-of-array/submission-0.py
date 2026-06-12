class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        a = []
        for i in nums:
            a.append(i)

        c = nums + a

        return c