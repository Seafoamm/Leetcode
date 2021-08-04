class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        returnArr = []
        permutations = {}
        def recurse(self, numbersLeft, finalArr):
            if numbersLeft == []:
                returnArr.append(finalArr)
                    
            else:
                for i in range(len(numbersLeft)): 
                    tempFinalArr = finalArr.copy()
                    tempNumbersLeft = numbersLeft.copy() 
                    tempFinalArr.append(numbersLeft[i]) 
                    tempNumbersLeft.pop(i)
                    
                    if not permutations.get(str(tempFinalArr), False):
                        permutations[str(tempFinalArr)] = True
                        recurse(self, tempNumbersLeft, tempFinalArr)
                        
                

        recurse(self, nums, [])

        return returnArr

