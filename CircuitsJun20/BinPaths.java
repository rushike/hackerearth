/* IMPORTANT: Multiple classes and nested static classes are supported */

/**
5
3
7
11 
2
16

1
3
4
0
7
 */

// uncomment this if you want to read input.
//imports for BufferedReader
import java.io.BufferedReader;
import java.io.InputStreamReader;

//import for Scanner and other utility classes
import java.util.*;


// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail

class BinPaths {
    
    public static void main(String args[] ) throws Exception {
        /* Sample code to perform I/O:
         * Use either of these methods for input
        */
        //BufferedReader
        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // String name = br.readLine();                // Reading input from STDIN
        // System.out.println("Hi, " + name + ".");    // Writing output to STDOUT

        //Scanner
        Scanner sc = new Scanner(System.in);
        // String name = s.nextLine();                 // Reading input from STDIN
        // Write your code here

        int T = Integer.parseInt(sc.nextLine().trim());
        int[] Ns = new int[T];
        for(int i = 0; i < T; i++){
            Ns[i] = Integer.parseInt(sc.nextLine().trim());
        }

        for(int i = 0; i < T; i++){
            int val = paths(Ns[i]);
            print(val);
        }
        
        // print(Integer.toString(T));
        // print(Arrays.toString(Ns));
    }
    public static void print(String str){
        System.out.println(str);
    }
    public static void print(int str){
        System.out.println(str);
    }
    public static int paths(int a){
        int n_2 = (int)Math.floor(a / 2);
        int base = 1;
        int accumalate = 0;
        Set int_pools = new HashSet<Integer>();
        HashMap<Integer, HashSet> map = new HashMap<>(); 
        // print("a : " + a + " n / 2 " + n_2);
        while(base <= n_2){
            int mover = base;
            Set temp_pool = new HashSet<Integer>();
            if(int_pools.contains(base)){
                base += 2;    
                continue;
            }
            while(mover <= a){            
                int_pools.add(mover);
                temp_pool.add(mover);
                mover = (mover << 1 | 1);
            }
            // print(temp_pool.size());
            int temp_size = temp_pool.size();
            if (temp_size > 1) {
                map.put(base, (HashSet)temp_pool);
                accumalate += ( (temp_size) * (temp_size - 1)) / 2;
                // print("temp size : " + temp_size + " cal : " + ( (temp_size / 2) * (temp_size - 1)) + " acc : " + accumalate  + ", pool : " + temp_pool.toString());
            }
            base += 2;
        }
        // print(int_pools.toString());
        // print(map.toString());
        return accumalate;
    }
}
