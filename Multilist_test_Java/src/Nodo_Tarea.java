public class Nodo_Tarea {
    String DptoSolicitante;
    String Descripciontarea;
    Nodo_Tarea next_tarea;

    public Nodo_Tarea(String dptoSolicitante, String descripciontarea) {
        this.DptoSolicitante = dptoSolicitante;
        this.Descripciontarea = descripciontarea;
        this.next_tarea = null;
    }

    @Override
    public String toString() {
        return DptoSolicitante;
    }
}
