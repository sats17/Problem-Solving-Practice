import java.util.HashMap;
import java.util.HashSet;

public class FibbonaciiNumber {
    
    public static int getFibbo(HashMap<Integer, Integer> cache, int n) {
        if(cache.containsKey(n)) {
            cache.get(n);
        }
        if (n == 0) {
            cache.put(n, 0);
            return 0;
        } else if (n == 1 || n == 2) {
            cache.put(n, 1);
            return 1;
        } else {
            int firstFibbo = getFibbo(cache, n - 1);
            int secondFibbo = getFibbo(cache, n - 2);
            return firstFibbo + secondFibbo;
        }

    }

    public static void main(String[] args) {
        HashMap<Integer, Integer> set = new HashMap<>();
        System.out.println(getFibbo(set, 6));
    }

}
