public class App {
    public static void main(String[] args) throws Exception {
        LinkedList lista = new LinkedList();
        System.out.println("Primera lista");
        lista.AddNode(5);
        lista.AddNode(2);
        lista.AddNode(10);
        lista.AddNode(3);
        lista.AddNode(6);
        lista.AddNode(11);
        lista.Escribir_lista();
        lista.Sort();
        lista.Escribir_lista();
        LinkedList lista2 = new LinkedList();
        System.out.println("Segunda lista");
        lista2.AddNode(9);
        lista2.AddNode(8);
        lista2.Escribir_lista();
        lista2.Sort();
        lista2.Escribir_lista();
    }
}
