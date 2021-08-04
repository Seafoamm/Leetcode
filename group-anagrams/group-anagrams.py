class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}
        
        for word in strs:
            key = "".join(sorted(word))
            if key in anagramDict:
                anagramDict[key].append(word)
            else:
                anagramDict[key] = []
                anagramDict[key].append(word)
                
                
        return [value for value in anagramDict.values()]