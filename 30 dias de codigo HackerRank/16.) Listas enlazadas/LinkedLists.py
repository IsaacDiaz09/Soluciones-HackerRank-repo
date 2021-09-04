class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        # El primer elemento es ninguno y tamaño cero porque inicialmente está vacia
        self.first = None
        self.size = 0
    
    def append(self,value):
        newNode = Node(value)
        # Si la lista esta vacia, el nodo creado pasa a ser el primero
        if self.size == 0:
            self.first = newNode
        # De lo contrario: recorre la lista y añade el nodo al final
        else:
            current = self.first
            while current.next != None:
                current = current.next
            current.next = newNode
        self.size += 1
    
    def remove(self,value):
        if self.size == 0:
            raise ValueError("{} not in list".format(value))
