class Solution:
    def fib(self, N: 'int') -> 'int':
        # 0 1 1 2 3 5 8 13 21
        
        val=[0,1]
    
        if N is 0:
            return 0
    
        else:
            for i in range(2,N+1):
                val.append(val[i-1] + val[i-2])
            return val[-1]
            
            
