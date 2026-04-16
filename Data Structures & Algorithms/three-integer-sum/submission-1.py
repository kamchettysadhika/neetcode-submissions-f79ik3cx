class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        

        for i, number in enumerate(nums):
            # skip duplicate anchors
            if i > 0 and number == nums[i - 1]:
                continue

            target = -number
            l, r = i + 1, len(nums) - 1

            while l < r:
                s = nums[l] + nums[r]

                if s == target:
                    result.append([number, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # skip duplicates
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif s < target:
                    l += 1
                else:
                    r -= 1

        return result
