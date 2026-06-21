class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        max_area = 0
        while L < R:
            computed_area = self.computeAreaFromIndex(L, R, heights)
            max_area = max(computed_area, max_area)
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return max_area
    
    def computeAreaFromIndex(self, i : int, j: int, heights: List[int]) -> int: 
        return (j - i) * min(heights[i], heights[j])