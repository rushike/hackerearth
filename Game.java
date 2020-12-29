// uncomment this if you want to read input.
//imports for BufferedReader
import java.io.BufferedReader;
import java.io.InputStreamReader;

//import for Scanner and other utility classes
import java.util.*;

public class Game {
    static HashMap<Integer, Integer> frequency(int arr[], int size) 
    { 
        // Creating a HashMap containing integer 
        // as a key and occurrences as a value 
        HashMap<Integer, Integer> freqMap 
            = new HashMap<Integer, Integer>(); 
  
        for (int i=0; i<size; i++) { 
            if (freqMap.containsKey(arr[i])) { 
  
                // If number is present in freqMap, 
                // incrementing it's count by 1 
                freqMap.put(arr[i], freqMap.get(arr[i]) + 1); 
            } 
            else { 
  
                // If integer is not present in freqMap, 
                // putting this integer to freqMap with 1 as it's value 
                freqMap.put(arr[i], 1); 
            } 
        } 
        return freqMap;
    } 
    public static void main(String[] args) {
        
    }
}