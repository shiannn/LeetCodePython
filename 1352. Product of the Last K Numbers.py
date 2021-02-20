class ProductOfNumbers:
    def __init__(self):
        self.que = []
        self.prod = 1

    def add(self, num: int) -> None:
        if num == 0:
            self.que = []
            self.prod = 1
        else:
            self.prod *= num
            self.que.append(self.prod)

    def getProduct(self, k: int) -> int:
        if k > len(self.que):
            return 0
        elif k == len(self.que):
            return self.que[-1]
        else:
            ret = self.que[len(self.que)-1] // self.que[len(self.que)-1-k]
            return ret

        
if __name__ == '__main__':
    methods = ["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
    params = [[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]
    ans = []
    for method, num in zip(methods, params):
        if method == "ProductOfNumbers":
            obj = ProductOfNumbers()
            ret = None
        elif method == "add":
            ret = obj.add(num[0])
        elif method == "getProduct":
            ret = obj.getProduct(num[0])
        ans.append(ret)
    print(ans)

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)