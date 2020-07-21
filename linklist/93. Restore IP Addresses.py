class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        OverallStore = []
        TempStore = []
        self.restoreIpAddressesutil(s,0,TempStore,OverallStore)
        return OverallStore

    def restoreIpAddressesutil(self,s,AlreadyPart,TempStore,OverallStore):
        print(AlreadyPart,s,TempStore,OverallStore)
        if(AlreadyPart == 4):
            if(s == ''):
                Ip = self.Trans(TempStore)
                OverallStore.append(Ip)
            return
        else:
            for i in range(1,3+1):
                if(len(s)>=i and self.isValid(s[0:i])):
                    TempStore.append(s[0:i])
                    self.restoreIpAddressesutil(s[i:],AlreadyPart+1,TempStore,OverallStore)
                    TempStore.pop()
    
    def Trans(self,TempStore):
        total = TempStore[0]
        for three_digit in TempStore[1:]:
            total += '.'
            total += three_digit
        return total
    def isValid(self,s):
        if((s[0] == '0' and len(s)>1) or (int(s)>255)):
            return False
        return True

if(__name__ == '__main__'):
    sol = Solution()
    In = "25525511135"
    ans = sol.restoreIpAddresses(In)
    print(ans)