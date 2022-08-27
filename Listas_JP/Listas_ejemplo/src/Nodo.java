public class Nodo{
    String data;
    Nodo next;

    public Nodo(String data) {
        this.data = data;
        this.next = null;
    }

    @Override
    public String toString() {
        return this.data;
    }
    
}
