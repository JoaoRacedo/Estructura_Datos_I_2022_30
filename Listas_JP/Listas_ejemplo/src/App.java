public class App {
    public static void main(String[] args) throws Exception {
        LinkedList lista1 = new LinkedList();
        lista1.AddNode("1");
        lista1.AddNode("3");
        lista1.AddNode("2");
        lista1.AddNode("10");
        lista1.Escribir_lista();

        LinkedList lista2 = new LinkedList();
        lista2.AddNode("-1");
        lista2.AddNode("-3");
        lista2.AddNode("-4");
        lista2.AddNode("-7");
        lista2.Escribir_lista();

        // Combinen dos listas
        LinkedList lista3 = new LinkedList();
        lista3.Combinar(lista1, lista2);
        lista3.Escribir_lista();
        // Organice la lista resultante (DESC/ASC)
    }

}
