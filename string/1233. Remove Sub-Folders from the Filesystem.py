class Solution:
    def removeSubfolders(self, folder):
        ret = []
        if len(folder) == 0:
            return ret
        folder_ = sorted(folder)
        print(folder_)
        ret.append(folder_[0])
        pivot = folder_[0] + '/'
        for f in folder_[1:]:
            ### if f is not the subdirectory of pivot (pivot is not substring of f)
            isSub = self.isSubstring(pivot, f)
            if isSub:
                pass
            else:
                ret.append(f)
                pivot = f + '/'
        return ret
    
    def isSubstring(self, s, t):
        if len(s) > len(t):
            return False
        else:
            for ss, tt in zip(s, t):
                if ss != tt:
                    return False
            return True


if __name__ == '__main__':
    sol = Solution()
    folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
    ret = sol.removeSubfolders(folder)
    print(ret)