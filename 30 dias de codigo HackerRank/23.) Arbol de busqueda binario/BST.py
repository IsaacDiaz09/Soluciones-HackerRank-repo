# https://www.hackerrank.com/challenges/30-binary-search-trees/problem?isFullScreen=true

"""
Estructura de datos en la cual sus nodos se organizan en forma de arbol, un nodo padre y dos hijos, asi
sucesivamente. El nodo hijo que va a la izquiera debe ser menor que su nodo padre, el de la derecha debe ser mayor;
a esto se le conoce como 'Propiedad abb' y siempre se cumple.
"""

# Clase nodo de los cuales se conformara el arbol de busqueda binario
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.result = ""
# arbol de busqueda binario
class BST:
    def __init__(self):
        self.root = None
    
    def getLeft(self,node):
        return node.left
        
    def getRight(self,node):
        return node.right

    def getRootNode(self):
        return self.root

    # Añade un nuevo nodo al arbol
    def add(self,value):
        __newNode = Node(value)

        # Si no hay un nodo principal el nuevo nodo pasa a ser el
        if self.root is None:
            self.root = __newNode
        else:
            # Si uso recursion tendria que añadir un tercer argumento al metodo (root) y quedaria asi --> else: self.add(current.left/right,value) 
            current = self.root
            if current.left is None:
                    current.left = __newNode

            elif value <= current.left.value:
                    while current.left != None:
                        current = current.left
                    current.left = __newNode
            else:

                if current.right is None:
                    current.right = __newNode
                else:
                    while current.right != None:
                        current = current.right
                    current.right = __newNode

    # Muestra el contenido de un nodo (lo visita) al momento de recorrer el arbol
    def visit(self,node):
        print(node.value)

    # Recorrido en pre-order del arbol -> Visita nodo, recorre por la izquierda -> encuentra 
    # un None, recorre por la derecha hasta el final
    """Recibe el nodo root como argumento"""
    def preOrder(self,current):
        # Mientras recorre el arbol se encontrará con nodos.left o right que estaran vacios y por ende va a fallar
        # diciendo que NoneType no posee tal atributo, asi que solo se le ordena ignorarlo 
        try:
            self.visit(current)
            self.preOrder(current.left)
            self.preOrder(current.right)
        except AttributeError:
            pass
    
    # Recorrido en in-Order -> llega al ultimo nodo de la izquierda, extrae nodo (visita) derecha 
    # y asi sucesivamente
    """Recibe el nodo root como argumento"""
    def inOrder(self,current):
        try:
            self.inOrder(current.left)
            self.visit(current)
            self.inOrder(current.right)
        except AttributeError:
            pass

    # Recorrido en post-order del arbol -> recorre toda la izquierda llega a None,busca por la 
    # derecha y cuando no hay mas visita nodo
    """Recibe el nodo root como argumento"""
    def postOrder(self,current):
        try:
            self.postOrder(current.left)
            self.postOrder(current.right)
            self.visit(current)
        except AttributeError:
            pass


myTree = BST()

myTree.add(7)
myTree.add(5)
myTree.add(3)
myTree.add(4)
myTree.add(6)
myTree.add(12)
myTree.add(8)
myTree.add(13)

print("· Pre-Order ·\n")

myTree.preOrder(myTree.getRootNode())

print("\n· In-Order ·\n")

myTree.inOrder(myTree.getRootNode())

print("\n· Post-Order ·\n")

myTree.postOrder(myTree.getRootNode())


"""
7
5
3
4
6
12
8
13

· In-Order ·

4
3
5
7
6
12
8
13

· Post-Order ·

4
3
5
13
8
12
6
7
"""