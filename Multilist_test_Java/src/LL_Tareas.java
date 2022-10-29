import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class LL_Tareas implements Iterable<Nodo_Tarea>{
    Nodo_Tarea head_tareas;
    Nodo_Tarea tail_tareas;

    public LL_Tareas(List<List<String>> values){
        this.head_tareas = null;
        this.tail_tareas = null;

        if(values.size() != 0){
            this.add_multiple_nodes_tareas(values);
        }
    }

    public void add_multiple_nodes_tareas(List<List<String>> values) {
        for(List<String> value: values){
            this.add_node_tarea(value);
        }
    }

    public void add_node_tarea(List<String> value) {
        if(this.head_tareas == null)
            this.tail_tareas = this.head_tareas = new Nodo_Tarea(
                value.get(0),
                value.get(1));
        else{
            this.tail_tareas.next_tarea = new Nodo_Tarea(
                value.get(0),
                value.get(1));
            this.tail_tareas = this.tail_tareas.next_tarea;
        }
    }

    public int size(){
        Nodo_Tarea P = this.head_tareas;
        int count = 0;
        while(P != null){
            count++;
            P = P.next_tarea;
        }
        return count;
    }

    public List<String> valueList(){
        List<String> lista_values = new ArrayList<>();
        for (Nodo_Tarea tarea : this){
            lista_values.add(tarea.DptoSolicitante);
        }
        return lista_values;
    }

    @Override
    public Iterator<Nodo_Tarea> iterator() {
        List<Nodo_Tarea> lista = new ArrayList<Nodo_Tarea>();
        Nodo_Tarea P = this.head_tareas;
        while(P != null){
            lista.add(P);
            P = P.next_tarea;
        }
        return lista.iterator();
    }
}
