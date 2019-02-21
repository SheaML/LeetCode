#Collaborative effort with Insight fellows Andy Upton and Jason Sosa. We beat 100% of python submissions! (32ms)


class Solution:
    def integerBreak(self, n: 'int') -> 'int':
        
        maxlength= (n // 2) + 1
        products=[]
        
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        for i in range(1,maxlength):
            
            s1 = n // i
            sum_ = [s1] * i
            remainder = n % i
            counter=0
            while remainder > 0:
                sum_[counter] +=1
                counter += 1
                remainder -= 1
                
            prod=1
            for i in sum_:
                prod *= i
            products.append(prod)
        
        return(max(products))
        
        
    
