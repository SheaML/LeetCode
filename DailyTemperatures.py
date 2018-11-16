class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        D=len(T)
        if(D == 0):
            return 0
        
        result = [0] * (D)
        
        for i in range(D - 2, -1, -1):
            
            start = i 
            end = i + 1
            days = 0
            
            while(True):
                if(T[start] < T[end]):
                    days = end - start
                    break
                    
                else:
                    if(result[end] == 0):
                        break
                        
                    else:
                        end += result[end]
        
            result[i] = days
        
        return result
