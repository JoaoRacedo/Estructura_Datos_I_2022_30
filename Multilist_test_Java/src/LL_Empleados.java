import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class LL_Empleados implements Iterable<Nodo_Empleado>{
    Nodo_Empleado head_empleados;
    Nodo_Empleado tail_empleados;
    /** 
     * Constructor method of LL_Empleados class.
     * @param values List of List of Strings
     * Example: [["Employee Code 1", "Number of task assigned to the employee 1"],
     *           ["Employee Code 2", "Number of task assigned to the employee 2"]
     *          ]
     */
    public LL_Empleados(List<List<String>> values){
        this.head_empleados = null;
        this.tail_empleados = null;

        if(values.size() != 0){
            this.add_multiple_nodes_empleados(values);
        }
    }

    /** 
     * This method is used to create nodes in a queue format and takes a
     * List of List of Strings with the information of each employee.
     * @param values List of List of Strings
     * Example: [["Employee Code 1", "Number of task assigned to the employee 1"],
     *           ["Employee Code 2", "Number of task assigned to the employee 2"]
     *          ]
     */
    public void add_multiple_nodes_empleados(List<List<String>> values) {
        for(List<String> value: values){
            this.add_node_empleado(value);
        }
    }

    /** 
     * This method is used to create a node in a queue format and takes a
     * List of Strings with the information of each employee.
     * @param value List of Strings
     * Example: ["Employee Code", "Number of task assigned to the employee"]
     * 
     */
    public void add_node_empleado(List<String> value) {
        if(this.head_empleados == null)
            this.tail_empleados = this.head_empleados = new Nodo_Empleado(
                value.get(0),
                value.get(1));
        else{
            this.tail_empleados.next_empleado = new Nodo_Empleado(
                value.get(0),
                value.get(1));
            this.tail_empleados = this.tail_empleados.next_empleado;
        }
    }

    /** 
     * This method computes the size of the Linkedlist of employees.
     * @return int This returns the number of employees that are in the linkedlist
     */
    public int size(){
        Nodo_Empleado P = this.head_empleados;
        int count = 0;
        while(P != null){
            count++;
            P = P.next_empleado;
        }
        return count;
    }

    /** 
     * This method return a List of String where each element is an employee code
     * @return List<String> List of employees codes
     */
    public List<String> valueList(){
        List<String> lista_values = new ArrayList<>();
        for (Nodo_Empleado empleado : this){
            lista_values.add(empleado.Codigo_Empleado);
        }
        return lista_values;
    }
    
    /** 
     * This method override the iterator() Java method. It creates
     * a List iterator with each object Nodo Empleado that is 
     * in the LinkedList Empleados
     * @return Iterator<Nodo_Empleado>
     */
    @Override
    public Iterator<Nodo_Empleado> iterator() {
        List<Nodo_Empleado> lista = new ArrayList<Nodo_Empleado>();
        Nodo_Empleado P = this.head_empleados;
        while(P != null){
            lista.add(P);
            P = P.next_empleado;
        }
        return lista.iterator();
    }
}