class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Brute Force - o(n^2) where you compare very element with every element - Bad
        #Slightly optimised
        # counter = {}
        # for i,num in enumerate(nums):
        #     counter[num] = counter.get(num,0)+1 ##As it is a dict so if counter has not seen num previously, we give it 0, if has seen it previously then we give the value(remeber num would be the key, not the value) 
        #     if counter[num]>1:
        #         return False
        # return True

        #Interviewer expectation - Use set
        seen = set()
        for i,num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
        return False
            