# https://www.hackerrank.com/challenges/30-binary-search-trees/problem?isFullScreen=true
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        cont1 = 0
        cont2 = 0
        if root.left is not None:
            cont1 = self.getHeight(root.left) + 1
        if root.right is not None:
            cont2 = self.getHeight(root.right) + 1

        return max([cont1,cont2])
        
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)
"""
Sample Input

7
3
5
2
1
4
6
7

Sample Output

3
"""