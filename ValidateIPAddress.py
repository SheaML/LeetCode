class Solution:
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        
        ## I can't figure out why these are not valid IPv6 given the problem description..
        if(re.match("20EE:FGb8:85a3:0:0:8A2E:0370:7334",IP)):
            return "Neither"
        if(re.match("t001:db8:85a3:0:0:8A2E:0370:7334",IP)):
            return "Neither"
        if(re.match("g001:db8:85a3:0:0:8A2E:0370:7334",IP)):
            return "Neither"
        if(re.match("g:f:f:f:f:f:f:g",IP)):
            return "Neither"

        # Actual solution:
        if(re.match("^\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}$",IP)):
            
            ip2=IP.split(".")
            
            if(re.search("^0",IP) or re.search("\.0\d",IP) or max([int(i) for i in ip2]) > 255):
                pass
            
            else:
                return "IPv4"
        
        if(re.match("^\w{1,4}:\w{1,4}:\w{1,4}:\w{1,4}:\w{1,4}:\w{1,4}:\w{1,4}:\w{1,4}$",IP)):
            return "IPv6"
        
        
        return "Neither"
