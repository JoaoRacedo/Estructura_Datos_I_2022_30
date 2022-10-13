from app.Classess import LinkedList
#from Classess import LinkedList

def test_len_list():
    lista = LinkedList([1,2,3,4])
    assert len(lista) == 4

def test_add_node():
    lista = LinkedList()
    lista.add_node(1)
    assert lista.values == [1]