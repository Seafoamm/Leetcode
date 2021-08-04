class Solution:
    def maxArea(self, height: List[int]) -> int:
        # shorter stick will determine height
        
        #area formula = min(h1, h2) * abs(i1 - i2)
        
        # find a max
        # once we have a max, search through the rest and calculate area at each one
        # running max area
        
        
        
        # pointer on left, pointer on right
        # while not crossing
        # caclulate Area()
        # if left < right  leftForward()
        # elif left >= right  rightBack()
        
        left = 0
        right = len(height) - 1
        maxHeight = 0
        
        while left < right:
            maxHeight = max(self.calculateArea(left, right, height), maxHeight)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return maxHeight
    
    def calculateArea(self, left, right, height):
        return (right - left) * min(height[left], height[right])