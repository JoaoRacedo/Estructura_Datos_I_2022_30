"""from Nodo import Nodo
Q = Nodo(1)
Z = Nodo(2)
X = Nodo(3)
print("before",Q.next)
Q.next = Z
Z.next = X
print("after",Q.next)"""

from LinkedList import LinkedList
lista = LinkedList()
lista.AddNode(5)
lista.AddNode(7)
lista.AddNode(10)

lista.Recorrido()
print(lista)
