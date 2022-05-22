import java.util.HashMap;
import java.util.HashSet;

public class GetDuplicates {
   
    public static HashSet<Integer> get(int[] array) {
        HashMap<Integer, Integer> indexedArr = new HashMap<>(array.length);
        HashSet<Integer> output = new HashSet<>(array.length);
        for(int i = 0; i < array.length; i++) {
            System.out.println(array[i] % array.length + 1+" = "+array[i] % array.length);
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

    public static void print(int[] numRay) {
        for (int i = 0; i < numRay.length; i++) {
            numRay[numRay[i] % numRay.length]
                = numRay[numRay[i] % numRay.length]
                  + numRay.length;
        }
        System.out.println("The repeating elements are : ");
        for (int i = 0; i < numRay.length; i++) {
            if (numRay[i] >= numRay.length * 2) {
                System.out.println(i + " ");
            }
        }
    }

    public static void main(String[] args) {
        int[] array = new int[]{1, 2, 3, 5, 6, 5, 2, 1, 24, 51, 12};
        // HashSet<Integer> output = get(array);
        print(array);
        // output.forEach(answer -> {
        //     System.out.println(answer);
        // });
    }

}
