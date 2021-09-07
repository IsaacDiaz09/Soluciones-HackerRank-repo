# Clase nodo, de las cuales sus instancias forman parte de una linkedList
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
    
    # Elimina la primer ocurrencia encontrada
    def remove(self,value):
        if self.size == 0:
            # Levanta una excepcion si se trata de remover un elemento de una linkedList vacia
            raise IndexError("cannot remove node from empty list!")
        else:
            current = self.first
            # Para el primer nodo
            if current.value == value:
                # Por ser el primero no tiene ningun nodo detras de el, entonces self.first pasará a ser el segundo nodo
                self.first = current.next

            else:
                try:
                    # Funciona pero solo para los nodos despues del primero
                    while current.next.value != value:
                        # current es el nodo anterior al nodo a eliminar
                        current = current.next
                    # Se guarda el nodo a eliminar
                    nodeToRemove = current.next
                    # El nodo siguiente de current ahora sera el siguiente del nodo a eliminar, rompiendo la conexion
                    current.next = nodeToRemove.next
                except AttributeError:
                    # Se sobre-escribe la excepcion para dar un mensaje mas informativo
                    raise AttributeError("value {} not in list!".format(value))
        self.size -= 1
    
    # Regresa el tamaño de la linkedList
    def __len__(self):
        return self.size

    # Imprime la linkedList con el formato [nodo1,nodo2 ,nodo3 ...]
    def __str__(self):
        String = ""
        String += "["
        current = self.first

        while current != None:
            if current.next is None:
                String += str(current)
            else:
                String += str(current)
                String += ", "
            current = current.next

        String += "]"

        return String

lst = LinkedList()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.append(5)

lst.remove(1)
lst.remove(2)

lst.append(True)

print(lst)
print(len(lst))

"""
Salida:
[3, 4, 5, True]
4
"""