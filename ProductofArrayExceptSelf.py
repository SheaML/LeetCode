class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        p=1
        output=[]
        
        #everybody but you, to the left
        for i in range(len(nums)):
            output.append(p)
            p *= nums[i]
        
        p=1
        #times everybody but you, to the right
        for i in range(len(nums)-1,-1,-1):
            output[i] *= p
            p *= nums[i]
        
        return output
        
        
        
