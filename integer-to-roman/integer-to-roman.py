class Solution:
    def intToRoman(self, num: int) -> str:
        dictionary = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        
        answer = ""
        leftover = num
        place = 1
        while leftover > 0:
            if leftover in dictionary:
                answer = dictionary[leftover * place] + answer
                break
            elif leftover % 10 == 0:
                leftover = leftover // 10
                place = place * 10
            else:
                tail = leftover % 10 * place
                if tail in dictionary:
                    answer = dictionary[tail] + answer
                else:
                    addFive = False
                    if leftover % 10 > 5:
                        addFive = True
                        leftover = leftover - 5
                        tail = tail - (5 * place)
                    three = (leftover % 10) % 3 == 0
                    two = (leftover % 10) % 2 == 0
                    counter = 1
                    if three:
                        counter = 3
                    elif two:
                        counter = 2
                    if counter in dictionary:
                        answer = dictionary[counter * place] + answer
                    else:
                        for i in range(counter):
                            answer = dictionary[tail // counter] + answer
                    if addFive:
                        answer = dictionary[5 * place] + answer
                leftover = leftover // 10
                place = place * 10
            
            
        return answer