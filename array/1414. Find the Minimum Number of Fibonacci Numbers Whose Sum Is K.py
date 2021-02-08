class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        A = [1, 1]
        prev1, prev2 = 0, 1
        tail = 1
        while(A[tail] <= k):
            A.append(A[prev1]+A[prev2])
            prev1 += 1
            prev2 += 1
            tail += 1
        A.pop()
        ret = 0
        while(k > 0):
            last = A.pop()
            if k >= last:
                k -= last
                ret += 1
        return ret

if __name__ == '__main__':
    sol = Solution()
    k = 7
    ret = sol.findMinFibonacciNumbers(k)
    print(ret)