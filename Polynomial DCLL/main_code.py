from DoubleLinkedList import DoubleLinkedList

lista = DoubleLinkedList()
lista.AddNode([3,323])
lista.AddNode([4,212])
lista.AddNode([-2,211])
lista.AddNode([1,122])
lista.AddNode([-1,111])
lista.Recorrido()

lista2 = DoubleLinkedList()
lista2.AddNode([2,333])
lista2.AddNode([1,312])
lista2.AddNode([-4,212])
lista2.AddNode([1,121])
lista2.AddNode([-1,110])
lista2.AddNode([5,000])
lista2.Recorrido()

lista.add_poly(lista2)
print("Result is:")
lista.Recorrido()

