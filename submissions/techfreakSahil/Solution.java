import java.io.BufferedReader;  
import java.io.FileReader;  
import java.io.IOException;

public class Solution{
    public static void main(String[] args) {
        String file = "spotify-2023.csv";
        int songs = -1; //first line includes the content
        String line;
        try(BufferedReader br = new BufferedReader(new FileReader(file))){
            while((line = br.readLine()) != null){
                songs+=1;
            }
            System.out.println("Total number of songs are: " + songs);
        }
        catch(Exception e){
            System.out.println(e);
        }
    }
}