from collections import defaultdict
import math

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Solution 3: Bucket Sort --> 
        # Create a mapping { count: list[value]}

        count_dict = defaultdict(int)
        for num in nums:
            count_dict[num] += 1
        
        # position[1] = [3] => 3 occured 1 time
        count_to_values_array = [[] for _ in range(len(nums) + 1)]

        for number,frequency in count_dict.items():
                count_to_values_array[frequency].append(number)

        result_array = []

        for item in reversed(count_to_values_array):
            if len(result_array) >= k:
                break
            if item == []:
                continue # empty array
            
            for number in item:
                result_array.append(number)

        return result_array[:k]
        
        # Solution 1: Brute Force
        # O(n + k) - Space
        # O(n * k) -
        # count_dict = defaultdict(int)
        # for num in nums:
        #     count_dict[num] += 1
        
        # print(count_dict)

        # result_array = []
        # for i in range(k):
        #     max_number, max_count = -math.inf,-math.inf
            
        #     for number,count in count_dict.items():
        #         if count > max_count:
        #             max_number = number
        #             max_count = count
            
        #     result_array.append(max_number)
        #     count_dict.pop(max_number)
        
        # return result_array


