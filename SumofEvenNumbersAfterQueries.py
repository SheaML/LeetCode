class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        
        ans=[]
        
        S = sum([i for i in A if i %2 is 0])
        
        for v,i in queries: 
            
            oldval = A[i]
            newval = A[i] + v

            if oldval % 2 is 0 and newval % 2 is 0:
                S += v

            if oldval % 2 is 0 and newval % 2 is 1:
                S -= oldval

            if oldval % 2 is 1 and newval % 2 is 0:
                S += newval

            A[i] = newval
            ans.append(S)
        
        return(ans)
        
  # I beat 98.7% of submissions in runtime and 100% of submissions in memory usage!
