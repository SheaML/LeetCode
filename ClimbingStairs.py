class Solution:
    def climbStairs(self, n: 'int') -> 'int':
    #FIBONNACI!
        n=n+1       
        val=[0,1]

        for i in range(2,n+1):
            val.append(val[i-1] + val[i-2])
        return val[-1]

