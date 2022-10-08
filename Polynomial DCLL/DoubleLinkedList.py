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
        P = self.PTR
        print("ULT", end = "<->")
        print(P.coef, P.exp, end="<->")
        P = P.next
        while(P != self.PTR):
            print(P.coef, P.exp, end="<->")
            P = P.next
        print("PTR")

    def Combine(self, lista):
        P = lista.PTR
        self.AddNode([P.coef,P.exp])
        P = P.next
        while(P != lista.PTR):
            self.AddNode([P.coef,P.exp])
            P = P.next
    
    def add_poly(self, lista2):
        P2 = lista2.PTR
        PTR3 = DoubleLinkedList()
        while (P2.next != lista2.PTR):
            P = self.PTR
            sw = 0
            while(P.next != self.PTR):
                if (P.exp == P2.exp):
                    P.coef = P.coef + P2.coef
                    sw = 1
                P = P.next
            if (P2.exp == P.exp):
                P.coef = P.coef + P2.coef
                sw = 1
            if (sw == 0):
                PTR3.AddNode([P2.coef, P2.exp])
            P2 = P2.next
        P = self.PTR
        sw = 0
        while(P.next != self.PTR):
            if (P.exp == P2.exp):
                P.coef = P.coef + P2.coef
                sw = 1
            P = P.next
        if (P2.exp == P.exp):
            P.coef = P.coef + P2.coef
            sw = 1
        if (sw == 0):
            PTR3.AddNode([P2.coef, P2.exp])
        self.Combine(PTR3)

        