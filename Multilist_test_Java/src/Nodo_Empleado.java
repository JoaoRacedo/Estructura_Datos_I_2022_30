import java.util.ArrayList;

public class Nodo_Empleado {
    String Codigo_Empleado;
    String num_tareas;
    Nodo_Empleado next_empleado;
    LL_Tareas tareas;

    public Nodo_Empleado(String codigo_Empleado, String num_tareas) {
        this.Codigo_Empleado = codigo_Empleado;
        this.num_tareas = num_tareas;
        this.next_empleado = null;
        this.tareas = new LL_Tareas(new ArrayList<>());
    }

    @Override
    public String toString() {
        return Codigo_Empleado;
    }
    
}
