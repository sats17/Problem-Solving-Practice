import java.util.HashMap;
import java.util.HashSet;

public class FibbonaciiNumber {
    
    public static int getFibbo(HashMap<Integer, Integer> cache, int n) {
        if(cache.containsKey(n)) {
            System.out.println(n + " for returning from cache");
            return cache.get(n);
        }
        if (n == 0) {
            System.out.println(n + " for returning from actual call");
            cache.put(n, 0);
            return 0;
        } else if (n == 1 || n == 2) {
            System.out.println(n + " for returning from actual call");
            cache.put(n, 1);
            return 1;
        } else {
            System.out.println(n + " for returning from actual call");
            int firstFibbo = getFibbo(cache, n - 1);
            System.out.println("At fibbonaci "+n+" started secondfibbo");
            int secondFibbo = getFibbo(cache, n - 2);
            int answer = firstFibbo + secondFibbo;
            cache.put(n, answer);
            return firstFibbo + secondFibbo;
        }

    }

    public static void main(String[] args) {
        HashMap<Integer, Integer> cache = new HashMap<>();
        System.out.println(getFibbo(cache, 6));
        for(int i = 0; i < 150; i++) {
            System.out.println("Getting fibbonaci for "+i);
            // System.out.println(cache.toString());
            System.out.println(getFibbo(cache, i));
        }
        // [1, 1, 3, 4, 5, 5, 1, 2]
    }
}