class Solution:
    def simplifyPath(self, path: str) -> str:
        #print(path.split(sep='/'))
        pathNames = []
        for s in path.split(sep='/'):
            #print(len(s))
            if len(s) > 0:
                pathNames.append(s)
        #print(pathNames)
        ansStack = []
        for pathName in pathNames:
            if pathName == '.':
                continue
            elif pathName == '..':
                if len(ansStack)>0:
                    ansStack.pop()
            else:
                ansStack.append('/'+pathName)
        if len(ansStack) == 0:
            ansStack.append('/')
        #print(ansStack)
        #print(''.join(ansStack))
        return ''.join(ansStack)

if __name__ == '__main__':
    sol = Solution()
    ans = sol.simplifyPath(path = "/home//foo/")
    #ans = sol.simplifyPath(path = "/a/./b/../../c/")
    print(ans)