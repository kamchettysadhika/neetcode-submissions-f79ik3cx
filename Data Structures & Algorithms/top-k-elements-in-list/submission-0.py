class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # instead of building a hashmap you build a hashmap in an array format
        array = [[] for i in range(len(nums) + 1)]
        numMap = {}
        res = []

        for num in nums:
            numMap[num] = 1 + numMap.get(num, 0)
        for number, idx in numMap.items():
            array[idx].append(number)
        # go through the array in the reverse order
        for i in range(len(array) - 1, 0, -1):
            for numb in array[i]:
                res.append(numb)
            if len(res) == k:
                return res
        