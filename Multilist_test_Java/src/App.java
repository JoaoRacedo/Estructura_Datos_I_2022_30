import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class App {
    public static void main(String[] args) throws Exception {
        // if Arrays.asList is used then the elements of the list can not be
        // changed, that includes adding or deleting! if any of the above is needed
        // then change to ArrayList, Stack, Queue, LinkedList
        List<List<String>> values = Arrays.asList(
            Arrays.asList("E1", "1"),
            Arrays.asList("E2", "2"),
            Arrays.asList("E3", "1")
        );
        LL_Empleados lista = new LL_Empleados(values);
        System.out.println(lista.size());
        System.out.println(lista.valueList());
        lista.head_empleados.tareas.add_node_tarea(Arrays.asList("D1", "Haga cosas"));
        System.out.println(lista.head_empleados.tareas.valueList());
    }
}
