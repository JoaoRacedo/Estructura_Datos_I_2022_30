from classess import LinkedList

lista_simple = LinkedList(["Calculo 3","Fisica Mec","POO"])

print(lista_simple)
print(len(lista_simple))
#print(lista_simple.head.Lista_matriculados)
#print(lista_simple.head.Lista_espera)

values = [["Sebas",1],["Sebas1",2],["Sebas3",3]]

P = lista_simple.head
for i in range(len(values)):
    P.Lista_matriculados.check_if(values[i], P)
    P = P.next

lista_simple.head.Lista_matriculados.check_if(["sebas4",5], lista_simple.head)


lista_simple.head.Lista_matriculados.check_if(["sebas5",6], lista_simple.head)
lista_simple.head.Lista_matriculados.check_if(["sebas6",7], lista_simple.head)


for _, obj in enumerate(lista_simple):
    print("-----------------------------------")
    print("Nombre curso:",obj.nombre_curso)
    print("Lista de matriculados:",obj.Lista_matriculados)
    print("Cupos dispo",obj.capacidad_curso - obj.Lista_matriculados.matriculados)
    if (len(obj.Lista_espera) != 0):
        print("Lista de espera:",obj.Lista_espera)
