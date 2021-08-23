class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # iterate over each char in search word build the substring
        # get top 3 results for current substring
        # compare prefixes to all strings to build running list
        # running list as heap
        
        import heapq
        
        output = []
        searchString = searchWord[0]
        # searchString = 'h'
        runningList = [word for word in products if word[0] == searchString]
        # runningList = ['havana']
        heapq.heapify(runningList)
        # runningList = ['havana']
        popAmount = min(len(runningList), 3)
        # popAmount = 1
        output.append(heapq.nsmallest(popAmount, runningList))
        # ['havana']
        for i in range(1, len(searchWord)):
            searchString += searchWord[i]
            
            runningList = [word for word in runningList if word[0:i+1] == searchString]
            #havana
            heapq.heapify(runningList)
            
            popAmount = min(len(runningList), 3)
            output.append(heapq.nsmallest(popAmount, runningList))
            # ['havana']
            
        return output
        