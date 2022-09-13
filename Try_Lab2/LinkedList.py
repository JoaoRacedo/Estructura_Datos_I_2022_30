from Nodo import Nodo

class LinkedList:
    def __init__(self):
        self.PTR = None
        self.ULT = None

    def AddNode(self,data):
        P = Nodo(data)
        if (self.PTR == None):
            self.PTR = P
            self.ULT = P 
        else:
            self.ULT.next = P
            self.ULT = P  

    def DeleteNode(self, data):
        if (self.PTR == None):
            print("Empty list")
        anteP = None
        P = self.PTR
        while(P != None):
            if (self.PTR.data == data):
                self.PTR = P.next
                del P
                P = self.PTR
            else:
                while(P != None and P.data != data):
                    anteP = P
                    P = P.next
                if (P != None and P.data == data):
                    anteP.next = P.next
                    P.next = None
                    del P
                    P = anteP.next
                else:
                    print("dato no en lista") 


            

    def Recorrido(self):
        P = self.PTR
        while(P != None):
            print(P.data, end="->")
            P = P.next
        print("None")
    
    def __repr__(self):
        respuesta = ""
        P = self.PTR
        while(P != None):
            respuesta = respuesta + str(P.Barrio.nombre) + "->"
            P = P.next
        respuesta = respuesta + "None"
        return respuesta
