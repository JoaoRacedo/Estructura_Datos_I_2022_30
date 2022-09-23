import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;

public class LinkedList {
  Nodo PTR;
  Nodo ULT;

  public LinkedList(){
      this.PTR = null;
      this.ULT = null;
  }

  public void AddNode(int data){
     Nodo P = new Nodo(data);
     if (this.PTR == null){
          this.PTR = P;
          this.ULT = P;
      }else{
          this.ULT.next = P;
          this.ULT = P; 
      }
    this.ULT.next = this.PTR;
  }
  public void Escribir_lista(){
        Nodo P = this.PTR;
        System.out.print(P.data + "->");
        P = P.next;
        while(P != this.PTR){
            System.out.print(P.data +"->");
            P = P.next;
        }
        System.out.println(P.data);
    }

    public void Sort(){
        ArrayList<Integer> numeros = new ArrayList<>();
        Nodo P = this.PTR;
        numeros.add(P.data);
        P = P.next;
        while(P != this.PTR){
            numeros.add(P.data);
            P = P.next;
        }
        Collections.sort(numeros);
        P = this.PTR;
        int i = 0;
        P.data = numeros.get(i);
        P = P.next;
        while(P != this.PTR){
            i = i + 1;
            P.data = numeros.get(i);
            P = P.next;
        }
    }

}
