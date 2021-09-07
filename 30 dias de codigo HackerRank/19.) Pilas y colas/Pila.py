class Stack:
    def __init__ (self):
        # Elemento superior o el de mas arriba
        self.top = None
        # Donde se guardan los elementos
        self.stack = []
    
    # Regresa el elemento top de la pila
    def getTop(self):
        return self.top

    # Añade el elemento a la pila y actualiza el top
    def add(self,value):
        self.top = value
        self.stack.append(value)

    # Elimina el ultimo elemento
    def remove(self):
        self.stack.pop()
        self.top = self.stack[-1]
    
    # Metodo str, al momento de mostrar la pila
    def __str__(self):
        return str(self.stack)

    # Metodo len(pila) para saber la longitud de la pila
    def __len__(self):
        return len(self.stack)

# Creacion de la pila
myStack = Stack()
myStack.add(True)
myStack.add(50)
myStack.add(10)
myStack.add("saludos")

print(myStack.getTop())
print(myStack)

myStack.remove()
print(myStack)
print(myStack.getTop())

"""
Salida:
· Elemento Top: 'saludos'
· Pila antes de elimnar: [True, 50, 10, 'saludos']
· Pila despues de eliminar el elemento Top: [True, 50, 10]
· Nuevo elemento Top: 10
"""
