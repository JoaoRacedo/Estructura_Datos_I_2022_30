package test_files;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;

public class File_first_example {
    
    public static void Llenar(Scanner sc, String file_name){
        String Id, name, Nro;
       
        try {
            FileWriter outFile = new FileWriter(file_name + ".txt", false);  //Archivo.txt
            // if false the file will be deleted and created everytime
            // if true the registers will be appended to the end of the file
            PrintWriter register = new PrintWriter(outFile);
            
            // LOGICA
            boolean hay_voto = false;
            System.out.println("Hay votos? true = si ; false = no");
            hay_voto = Boolean.parseBoolean(sc.nextLine());
            while(hay_voto){
                System.out.println("Id");
                Id = sc.nextLine();
                System.out.println("Name");
                name = sc.nextLine();
                System.out.println("Nro Candidate");
                Nro = sc.nextLine();
                if (!Id.isEmpty() && !name.isEmpty() && !Nro.isEmpty()){
                    register.println(Id +"\t"+ name +"\t"+ Nro);
                }
                System.out.println("Hay votos? true = si ; false = no");
                hay_voto = Boolean.parseBoolean(sc.nextLine());  
            }
           register.close();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    
    }
    
    public static void Leer(Scanner sc, String file_name){
        boolean hay = false;
        while(hay == false){
            try {
                BufferedReader br = new BufferedReader(new FileReader(file_name+".txt"));
                String line = null;

                while((line = br.readLine()) != null){
                    String temp[] = line.split("\t");
                    // String temp[] ={1,2,3,4}
                    System.out.println(temp[0] + ","+ temp[1] + ","+temp[2]);
                }
                br.close();
                hay = true;

            } catch (IOException ex) {
                System.out.println("No se encontro archivo");
                hay = false;
                file_name = sc.nextLine(); // Archivo
            }
        }
        
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String file_name = sc.nextLine(); // Archivo
        //System.out.println("Se llama a funcion crear o llenar archivo");
        //Llenar(sc, file_name);
        System.out.println("Escribir datos de archivo a consola");
        Leer(sc, file_name);
        sc.close();
    }
    
}
