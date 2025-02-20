class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        if nums[0][0] == "1":
            string = "0"
        else:
            string = '1'
        n = len(nums) - 1
        for i in range(n):
            if not any((string + "0") in num for num in nums):
                string = string + ("0" * (n - i))
                return string
            elif not any((string + "1") in num for num in nums):
                string = string + ("1" * (n - i))
                return string
            else:
                string += "1"
        return string