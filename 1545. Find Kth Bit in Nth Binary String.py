class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        ### recursion half
        num_n = 2**n - 1
        if k == (num_n // 2 + 1):
            return "1"
        elif k < (num_n // 2 + 1):
            return self.findKthBit(n - 1, k)
        elif k > (num_n // 2 + 1):
            ### find position in previous layer
            prev_N = num_n // 2
            target_idx = k - (num_n // 2 + 1)
            idx = prev_N + 1 - target_idx
            ret = self.findKthBit(n - 1, idx)
            if ret == "1":
                return "0"
            elif ret == "0":
                return "1"

if __name__ == '__main__':
    sol = Solution()
    #n = 3
    #k = 1
    #n = 4
    #k = 11
    #n = 1
    #k = 1
    n = 2
    k = 3
    ret = sol.findKthBit(n, k)
    print(ret)