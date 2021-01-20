class Solution:
    def generate(self, numRows: int):
        triangle = []
        for r in range(1, numRows+1):
            row = []
            for c in range(1, r+1):
                if c == 1 or c == r:
                    row.append(1)
                else:
                    prev_row = triangle[(r-1) - 1]
                    row.append(prev_row[c-1] + prev_row[(c-1)-1])
            print(row)
            triangle.append(row)
        
        return triangle

if __name__ == '__main__':
    sol = Solution()
    t = sol.generate(5)
    print(t)