class Queue:
    def __init__(self):
        self.initial = None
        self.bottom = None
        self.queue = []

    # Retorna el elemento final de la cola
    def getBottom(self):
        return self.bottom

    # Retorna el elemento inicial de la cola
    def getInitial(self):
        return self.initial    

    # Añade un elemento al final de la cola
    def add(self, value):
        self.queue.append(value)    
        self.bottom = value

    # Elimina un elemento al principio de la cola y actualiza el elemento inicial
    def remove(self):
        self.queue.pop(0)
        self.initial = self.queue[0]
    
    # Metodo str, al momento de mostrar la cola
    def __str__(self):
        return str(self.queue)

    # Metodo len(cola) para saber la longitud de la cola
    def __len__(self):
        return len(self.queue)

# Creacion de la cola
myQueue = Queue()
myQueue.add(False)
myQueue.add(12)
myQueue.add(5)
myQueue.add([])
myQueue.add("adios")

print(myQueue)
print(myQueue.getBottom())

myQueue.remove()
myQueue.remove()

print(myQueue)
print(myQueue.getInitial())
print(myQueue.getBottom())

"""
Salida:
· Cola inicial: [False, 12, 5, [], 'adios']
· Ultimo elemento de la cola: 'adios'
· Se ha eliminado dos veces el que fue primer elemento: [5, [], 'adios']
· Elemento inicial: 5
· Nuevo elemento final: 'adios'
"""