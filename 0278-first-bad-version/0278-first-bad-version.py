# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        minimum = 1
        maximum = n
        mid = (minimum + maximum) // 2
        if isBadVersion(maximum) == True and isBadVersion(maximum - 1) == False:
            return maximum
        while isBadVersion(mid) == isBadVersion(mid - 1):
            if isBadVersion(mid) == False:
                minimum = mid
            else:
                maximum = mid
            mid = (minimum + maximum) // 2
        return mid