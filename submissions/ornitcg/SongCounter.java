import java.io.*; 
import java.util.InputMismatchException;
import java.util.HashMap;

public class SongCounter {
    public static int findIndex(String str, String[] searchArray){
        for (int i=0; i< searchArray.length ; i++){
            if(searchArray[i].equals(str)){
                return i;
            }
        }
        return -1;
    } //findIndex
    
    public static void main(String[] args) {
        String path = "./spotify-2023.csv";
        try {
            BufferedReader reader =new BufferedReader(new FileReader(path));
         
            String line = "";
            line=reader.readLine();
            String[] titles = line.trim().split(",");
            int keyLocation= findIndex("key", titles);            
            int songsCounter = 0;
            int eKeyCounter = 0;
            
            while((line=reader.readLine())!=null){
                songsCounter++;
                String[] songData = line.trim().split(",");
                if (songData[keyLocation].equals("E")){
                    eKeyCounter++;
                }
                
            }
            
            System.out.println("Number of songs: "+ songsCounter);
            System.out.println("Number of songs with E key: "+ eKeyCounter);
            
            
            
            
        }
        catch(Exception e){
            System.out.println("csv failed to load");
            
        }
    }
}