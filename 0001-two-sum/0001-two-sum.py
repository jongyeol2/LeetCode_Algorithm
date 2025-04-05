class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            subtarget = target - num

            if subtarget in nums:
                sub_tg_idx = nums.index(subtarget)
                if idx != sub_tg_idx:
                    return [idx, sub_tg_idx]



        