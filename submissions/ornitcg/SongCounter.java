import java.io.*; 
import java.util.InputMismatchException;
import java.util.Scanner;

public class SongCounter {
    public static void main(String[] args) {
        try {
            Scanner sc = new Scanner(new File("./spotify-2023.csv"));  
            sc.useDelimiter(","); 
            // System.out.println("csv successfuly loaded");
            int counter = 0;
            while(sc.hasNext()){
                counter++;
                // System.out.print(sc.next());
                sc.next();
            }
            System.out.println("csv contains " + counter + " songs");
            sc.close();
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println("failed to load csv");
            
        }       
        
    }
}