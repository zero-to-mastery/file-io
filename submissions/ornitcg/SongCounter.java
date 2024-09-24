import java.io.*; 
import java.util.InputMismatchException;
import java.util.Map;
import java.util.HashMap;

public class SongCounter {
    
    public static String mostCommon(HashMap<String,Integer> strMap){
        int maxOccurence = 0;
        String maxName = "";
        for (Map.Entry<String, Integer> entry : strMap.entrySet()) {
            String key = entry.getKey();
            Integer value = entry.getValue();
            // System.out.println("Key: " + key + ", Value: " + value);
            if(value>maxOccurence){
                maxOccurence= value;
                maxName = key;
            }
        }
        return maxName;
    }
    
    
    
    
    
    
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
            HashMap<String,Integer> artistOcc = new HashMap<String, Integer>();
            String line = "";
            line=reader.readLine();
            String[] titles = line.trim().split(",");
            int keyIndex= findIndex("key", titles);   
            int artistIndex= findIndex("artist(s)_name", titles);            
            
            int songsCounter = 0;
            int eKeyCounter = 0;
            
            
            while((line=reader.readLine())!=null){
                songsCounter++;
                String[] songData = line.trim().split(",");
                if (songData[keyIndex].equals("E")){
                    eKeyCounter++;
                }
                String artist = songData[artistIndex];
                if(artistOcc.containsKey(artist)){
                    artistOcc.put(artist, artistOcc.get(artist) + 1);
                }
                else{
                    artistOcc.put(artist, 1);
                    
                }
                
            }
            String mostCommonArtist = mostCommon(artistOcc);
            
            System.out.println("Number of songs: "+ songsCounter);
            System.out.println("Number of songs with E key: "+ eKeyCounter);
            System.out.println("The artist with the higest occurence is: " + mostCommonArtist + " with " + artistOcc.get(mostCommonArtist) + " tracks");
            
            
            
            
        }
        catch(Exception e){
            System.out.println("csv failed to load");
            
        }
    }
}