 
import math

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Input: [2, 20, 4, 10, 3, 4, 5]
        # LCS: [2,3,4,5] --> 4 Output
        
        # Brute Algorithm: 
        #  [2, 3, 4, 5, 10, 20]

        # Edge Case -  []
        if len(nums) == 0:
            return 0

        sorted_nums : List[int] = sorted(nums)
        longest_consec_count = -math.inf
        consecutive_count = 1
        previous_member = sorted_nums[0]
    
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == previous_member + 1:
                print(sorted_nums[i], previous_member)
                consecutive_count += 1
                previous_member = sorted_nums[i]
            elif sorted_nums[i] == previous_member:
                continue
            else:
                # Non Consecutive
                longest_consec_count = max(longest_consec_count, consecutive_count)
                consecutive_count = 1
                previous_member = sorted_nums[i]
        
        return max(longest_consec_count, consecutive_count)

        