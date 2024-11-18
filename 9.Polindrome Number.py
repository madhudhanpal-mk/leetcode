class Solution:
    def isPolindrome(self, x:int) -> bool:
        if x < 0: return False

        div = 1
        while x >= 10 * div:
            div *= 10
        
        while x:
            right = x % 10
            left = x // div

            if left != right: return False

            x = (x % div) // 10
            div = div / 100
            
        return True

c1 = Solution()
num = 121
print(c1.isPolindrome(num))