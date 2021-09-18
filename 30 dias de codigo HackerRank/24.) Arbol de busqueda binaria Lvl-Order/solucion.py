# https://www.hackerrank.com/challenges/30-binary-trees/problem?isFullScreen=false
import sys

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
        
    def levelOrder(self,root):
        l = []
        res = []
        # Se añade el nodo root
        l.append(root)

        # Cuando ya no hayan nodos por recorrer saldra del bucle
        while len(l)>0:
            res.append(l[0].data)
            # Se elimina y recupera el primer nodo
            node = l.pop(0)

            # Se busca si tiene nodos hijos y si si, se añaden
            if node.left is not None:
                l.append(node.left)
            if node.right is not None:
                l.append(node.right)

            # El proceso se repite sucesivamente y cada vez se elimina el primer elemento avanzando asi de nivel
        del l

        print(" ".join([str(x) for x in res]))


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
print()
myTree.levelOrder(root)
"""
6
3
5
4
7
2
1

"""
# 3 2 5 1 4 7 
