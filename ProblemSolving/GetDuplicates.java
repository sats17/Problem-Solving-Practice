import java.util.HashMap;
import java.util.HashSet;

public class GetDuplicates {
   
    public static HashSet<Integer> get(int[] array) {
        HashMap<Integer, Integer> indexedArr = new HashMap<>(array.length);
        HashSet<Integer> output = new HashSet<>(array.length);
        for(int i = 0; i < array.length; i++) {
            if(indexedArr.containsKey(array[i])) {
                indexedArr.put(array[i], indexedArr.get(array[i]) + 1);
            } else {
                indexedArr.put(array[i], 1);
            }
        }
        indexedArr.forEach((key, value) -> {
            if(value > 1) {
                output.add(key);
            }
        });
        return output;
    }

    public static void main(String[] args) {
        int[] array = new int[]{1, 2, 3, 4, 5, 6, 1, 2, 4, 5, 11, 102};
        HashSet<Integer> output = get(array);
        output.forEach(answer -> {
            System.out.println(answer);
        });
    }

}
