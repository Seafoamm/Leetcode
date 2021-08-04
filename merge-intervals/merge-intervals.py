class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # brute force:
        # iterate intervals:
        # merge/absorb when comparing to all other intervals
        
        # is there duplication when comparing with all other intervals?
        # could an interval expand to a point where you do need to compare to previously visited intervals
        
        returnList = []
        
        # grabbing the widest interval?
        
        # sorting first:
        # 
        
        sortedIntervals = sorted(intervals, key=lambda x: x[0])
        print(sortedIntervals)
        # iterate through
        # while next element can be absorbed
        # absorb
        # else: move to next element
        left = 0
        right = 1
        while left < len(intervals):
                while right < len(intervals) and sortedIntervals[right][0] <= sortedIntervals[left][1]:
                    sortedIntervals[left][1] = max(sortedIntervals[left][1], sortedIntervals[right][1])
                    right += 1
                returnList.append(sortedIntervals[left])
                left = right
                right += 1
        
        return returnList