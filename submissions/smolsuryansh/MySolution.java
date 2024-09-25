import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;

public class MySolution{
    public static void main(String[] args) {
        String filecsv = "spotifycsvfile.csv";
        String line;
        int songs = -1;
        try(BufferedReader br = new BufferedReader(new FileReader(filecsv))){
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