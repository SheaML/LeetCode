class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        
        striplist=[]
        
        for i in emails:
            local,domain = i.split("@")
            local = local.replace(".","")
            localplus=[]
            for j in local:
                if j is not "+":
                    localplus.append(j)
                if j is "+":
                    break
            
            local = ''.join(localplus)
            
            stripped = local+"@"+domain
            striplist.append(stripped)
        return len(set(striplist))
            

                    
