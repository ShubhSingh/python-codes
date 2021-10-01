class Solution922(object):
    def sortArrayByParityII(self, nums):
        i = 0 # pointer for even misplaced
        j = 1 # pointer for odd misplaced
        sz = len(nums)

        # invariant: for every misplaced odd there is misplaced even
        # since there is just enough space for odds and evens

        while i < sz and j < sz:
            if nums[i] % 2 == 0:
                i += 2
            elif nums[j] % 2 == 1:
                j += 2
            else:
                # a[i] % 2 == 1 AND a[j] % 2 == 0
                nums[i],nums[j] = nums[j],nums[i]
                i += 2
                j += 2

        return nums
