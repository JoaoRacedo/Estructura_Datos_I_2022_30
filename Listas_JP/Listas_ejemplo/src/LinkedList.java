public class LinkedList {
    Nodo PTR;
    Nodo ULT;

    public LinkedList(){
        this.PTR = null;
        this.ULT = null;
    }

    public void AddNode(String data){
       Nodo P = new Nodo(data);

       if (this.PTR == null){
            this.PTR = P;
            this.ULT = P;
        }else{
            this.ULT.next = P;
            this.ULT = P; 
        }
    }

    public void Escribir_lista(){
        Nodo P = this.PTR;
        while(P != null){
            System.out.print(P.data +"->");
            P = P.next;
        }
        System.out.println("null");
    }

    public void Combinar(LinkedList lista1, LinkedList lista2){
        //LinkedList lista_combinada = new LinkedList();

        Nodo P1 = lista1.PTR;
        Nodo P2 = lista2.PTR;
        //Nodo PTR3 = this.PTR;

        while(P1 != null){
            this.AddNode(P1.data);
            P1 = P1.next;
        }
        while(P2 != null){
            this.AddNode(P2.data);
            P2 = P2.next;
        }
    }
}
