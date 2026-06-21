 
import math

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Input: [2, 20, 4, 10, 3, 4, 5]
        # LCS: [2,3,4,5] --> 4 Output
        
        # Brute Algorithm: 
        #  [2, 3, 4, 5, 10, 20]



        # Algorithm : convert the list to a set

        nums_set = set(nums)
        longest_sequence = 0
        
        for num in nums:
            if num - 1 in nums_set:
                # not the start of a sequence
                continue
            else:
                # start of the sequence
                sequence_length = 1
                next_sequence_number = num + 1
                while (next_sequence_number in nums_set):
                    sequence_length += 1
                    next_sequence_number += 1
                
                longest_sequence = max(sequence_length, longest_sequence)
                
        return longest_sequence
        