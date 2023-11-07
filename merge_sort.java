public class Main {
    public static void main(String args[]) {
        int [] arr = {10, 7, 9, 2, 4};
        mergeSort(arr, 0, arr.length - 1);
        for(int i = 0; i < arr.length; i++){
            System.out.println(arr[i] + " ");
        }
    }
    public static int [] mergeSort(int [] arr, int low, int high) {
        if(low >= high)
            return arr;
        int mid = (low + high)/2;
        mergeSort(arr, low, mid);
        mergeSort(arr, mid + 1, high);
        arr = merge(arr, low, mid, high);
        return arr;
    }
    public static int [] merge(int [] arr, int low, int mid, int high) {
        int i = 0;
        int [] newarr = new int [arr.length - 1];
        int left = low;
        int right = mid + 1;
        while(left < mid || right  <= high) {
            if(arr[left] > arr[right]) {
                newarr[i] = arr[right];
                right++;
                i++;
            } else {
                newarr[i] = arr[left];
                left++;
                i++;
            }
        }
        while(left <= right) {
            newarr[i] = arr[left];
            left++;
            i++;
        }
        while(right <= high) {
            newarr[i] = arr[right];
            right++;
            i++;
        }

        return newarr;
    }
}