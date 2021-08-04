class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # bit combinations?
        # except there are restrictions on the combination.
        
        # oh! bit combinations depending on the start parentheses
        # possible positions are 0...n * 2 - remaining opened parentheses
        comboList = []
        Solution.generateCombos(n, "", comboList, 1, 1)
        
        return comboList
        
    def generateCombos(n, string, comboList, o, notClosed):
        current = string
        if n == 1:
            comboList.append("()")
        elif len(current) == n * 2 - 1:
            current += ")"
            comboList.append(current)
        elif current == "":
            current += "("
            if o < n:
                Solution.generateCombos(n, current + "(", comboList, o + 1, notClosed + 1)  
            if notClosed > 0:
                Solution.generateCombos(n, current + ")", comboList, o, notClosed - 1)
        else:
            if o < n:
                Solution.generateCombos(n, current + "(", comboList, o + 1, notClosed + 1)  
            if notClosed > 0:
                Solution.generateCombos(n, current + ")", comboList, o, notClosed - 1)

                
            