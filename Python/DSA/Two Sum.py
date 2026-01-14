class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Brute force approach
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if (nums[i]+nums[j] == target):
        #             return [i,j]
        #HashMap Approach - We check if target - nums[i] is already present in our mapping or not.
        remaining_value_index = {}
        for i,num in enumerate(nums):
            if((target - num) in remaining_value_index):
                return [remaining_value_index[target-num],i]
            elif((target - num) not in remaining_value_index):
                remaining_value_index[num] = i



            

        