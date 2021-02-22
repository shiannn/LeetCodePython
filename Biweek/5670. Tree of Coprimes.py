class Solution:
    def getCoprimes(self, nums, edges):
        graph = {}
        ### use DFS to get parent
        for edge in edges:
            s, t = edge
            if s not in graph:
                graph[s] = []
            graph[s].append(t)
            if t not in graph:
                graph[t] = []
            graph[t].append(s)
        #print(graph)
        parents = self.getParents(graph)
        #print('parents', parents)
        ret = []
        for i in range(len(nums)):
            #print('i', i)
            p = parents[i]
            while(p!=-1 and not self.isCoprime(nums[i], nums[p])):
                #print('p', p)
                p = parents[p]
            if p==-1:
                ret.append(-1)
            else:
                ret.append(p)
        #print(ret)
        return ret
    
    def getParents(self, graph):
        st = 0
        vis = {0}
        parents = {0:-1}
        parents = self.dfs(graph, st, vis, parents)
        print(parents)
        return parents

    def dfs(self, graph, st, vis, parents):
        for adjs in graph[st]:
            if adjs not in vis:
                #print(adjs)
                parents[adjs] = st
                vis.add(adjs)
                parents = self.dfs(graph, adjs, vis, parents)
                vis.remove(adjs)
        return parents

    def isCoprime(self, a, b):
        for i in range(2, min(a, b)+1):
            if a%i==0 and b%i==0:
                return False
        return True

if __name__ == '__main__':
    sol = Solution()
    nums = [5,6,10,2,3,6,15]
    edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
    #nums = [2,3,3,2]
    #edges = [[0,1],[1,2],[1,3]]
    ret = sol.getCoprimes(nums, edges)
    print(ret)