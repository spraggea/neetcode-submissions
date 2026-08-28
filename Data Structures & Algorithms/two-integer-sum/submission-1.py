class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       #Cant two pointer because unsorted, if we sorted it it would be o(nlogn) not logn
#
#Need nums[i] + nums[j] == target
#Rearrange eq --> nums[i] = target - nums[j] --> needed = target - num
#Plan
#keep track of seen values
#check whther that value appear before
#e.g nums = [3, 4, 5, 6] and target = 7
# 3 with target = 7, need 4 store {3 : 0}
# we see 4 next, need 3, we already have 3 stored so we return 3 and 4 #indices, [0, 1]
        seen = {}

        for i, num in enumerate(nums):
            needed = target - num

            if needed in seen:
                return [seen[needed], i]

            seen[num] = i