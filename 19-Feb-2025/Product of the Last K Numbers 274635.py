# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        self.stream = []

    def add(self, num: int) -> None:
        self.stream.append(num)
        

    def getProduct(self, k: int) -> int:
        
        return prod(self.stream[len(self.stream)-k:])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)