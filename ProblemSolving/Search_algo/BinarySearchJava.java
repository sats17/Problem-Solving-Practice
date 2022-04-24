import java.util.Arrays;

public class BinarySearchJava {

    public static int search(int[] array, int midIndex, int value) {

        int midValue = array[midIndex];
        if(midValue == value) {
            return midIndex;
        } else if (array.length == 1) {
            return -1;
        } else if(midValue > value) {
            int[] newArray = Arrays.copyOfRange(array, 0, midIndex);
            int newMidIndex = newArray.length / 2;
            return search(newArray, newMidIndex, value);
        } else {
            int[] newArray = Arrays.copyOfRange(array, midIndex, array.length);
            int newMidIndex = newArray.length / 2;
            return search(newArray, newMidIndex, value);
        }
    }

    public static int[] insertAtIndex(int[] array, int index, int value) {
        int[] newArray = new int[array.length + 1];
        int currentIndex = 0;
        int currentIndexOfArray = 0;
        while(currentIndex < array.length) {
            if(currentIndex == index) {
                newArray[index] = value;
                currentIndexOfArray++;
                index = -1;
            } else {
                newArray[currentIndexOfArray] = array[currentIndex];
                currentIndex++;
                currentIndexOfArray++;
            }
        }
        return newArray;
    }

    public static void main(String[] args) {
        // int val = 10 / 3;
        // System.out.println(val);
        int[] arr = new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int[] updatedArr = insertAtIndex(arr, 3, 11);
        System.out.println(Arrays.toString(updatedArr));
        // System.out.println(search(arr, arr.length / 2, 1));
        // for(int i = 0; i <= 19; i++) {
        //     System.out.println(search(arr, arr.length / 2, i));
        // }
        /**
         * while() {
         *  
         * }
         */
        
    }
}