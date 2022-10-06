from Nodo import Nodo

class DoubleLinkedList:
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
            P.prev = self.ULT
            self.ULT = P  
        self.ULT.next = self.PTR
        self.PTR.prev = self.ULT
    
    def Recorrido(self):
        P = self.ULT
        print("PTR", end = "<->")
        print(P.data, end="<->")
        P = P.prev
        while(P != self.ULT):
            print(P.data, end ="<->")
            P = P.prev
        print("ULT")

"""
sub Buscar(PTR, ULT, valor)
    P <- PTR
    Q <- ULT
    sw <- 0 # if found
    sw1 <- 0 # if in middle
    MQ(sw = 0 and sw1 = 0)
        si (P.data = valor o Q.data = valor)
            sw <- 1
            escr("encontrado")
        sino
            si (P = Q or P.next = Q or Q.prev = P)
                sw1 <- 1
                escr("no encontrado)
            sino
                P <- P.next
                Q <- Q.prev
            FinSi
        FinSi
    FinMQ
FinSub
"""