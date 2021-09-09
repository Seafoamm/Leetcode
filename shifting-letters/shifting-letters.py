class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        output = [char for char in s]
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        toAscii = {
            char: ord(char) % 97 for char in alphabet
        }
        
        toChar = {
            i: alphabet[i] for i in range(26)
        }

        for i in range(len(shifts) - 2, -1, -1):
            shifts[i] = shifts[i+1] + shifts[i]
    
        def shift(char, x):
            newChar = toChar[((toAscii[char] + x) % 26)]
            return newChar
      
        for i in range(len(shifts)):
            output[i] = shift(output[i], shifts[i])
        
        return "".join(output)