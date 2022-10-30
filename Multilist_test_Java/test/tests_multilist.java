import static org.junit.Assert.assertEquals;
import org.junit.Test;

import java.util.Arrays;
import java.util.List;

public class tests_multilist {
    
    @Test
    public void test_multilevel_creation(){
        List<List<String>> values = Arrays.asList(
            Arrays.asList("E1", "1"),
            Arrays.asList("E2", "2"),
            Arrays.asList("E3", "1")
        );
        LL_Empleados lista = new LL_Empleados(values);
        assertEquals(lista.size(), 3);
    }

    // if you want to run it in terminal. Go to the project
    // and run:
    // java -cp "bin:lib/*" org.junit.runner.JUnitCore PackageName.ClassName
    // : if mac ; if windows
    // if code not compiled please compiled first. 
    //    this will create the bin folder
    // lib is the folder where the junit library is installed. 
}
