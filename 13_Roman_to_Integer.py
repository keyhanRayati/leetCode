class Solution:
    def romanToInt(self, s: str) -> int:
        value = {'I' : 1 , 'V' : 5 , 'X': 10 , 'L': 50 , 'C' : 100 , 'D':500 , 'M' : 1000  }
        str = s + 'Z'
        result = 0
        i = 0
        while i < (len(str)):
            char = str[i]
            if char == 'Z':
                return result
            else:
                flag = True
                if char=='C' and flag:
                    flag = False
                    if str[i+1] == 'D' or str[i+1] == 'M' :
                        result += (value.get(str[i+1]) - value.get(str[i]))
                        i+=2
                    else:
                        while(str[i] == char):
                            result+= value.get(char)
                            i+=1
                if (str[i] == 'D' or str[i] == 'M') and flag:
                    flag = False
                    result += value.get(str[i])
                    i+=1
                #---------------------------------------------------------------
                if char=='X' and flag:
                    flag = False
                    if str[i+1] == 'L' or str[i+1] == 'C' :
                        result += value.get(str[i+1]) - value.get(str[i]) 
                        i+=2
                    else:
                        while(str[i] == char):
                            result += value.get(char)
                            i+=1
                if (str[i] == 'L' or str[i] == 'C') and flag:
                    flag = False
                    result += value.get(str[i])
                    i+=1
                #---------------------------------------------------------------
                if char=='I' and flag:
                    flag = False
                    if str[i+1] == 'V' or str[i+1] == 'X' :
                        result += value.get(str[i+1]) - value.get(str[i]) 
                        i+=2
                    else:
                        while(str[i] == char):
                            result += value.get(char)
                            i+=1
                if (str[i] == 'V' or str[i] == 'X') and flag:
                    flag = False
                    result += value.get(str[i])
                    i+=1
            

class __main__():
    instance = Solution()
    print(instance.romanToInt('LVIII'))

