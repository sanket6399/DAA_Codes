// "static void main" must be defined in a public class.
public class Main {
    public static void main(String[] args) {
        int [] arr = {-9, 10, -8, 10, 5, -4, -2, 5};
        List<Integer> lis = new ArrayList<Integer>();
        printSub(0, lis, arr.length, arr, 2, 0);
    }
    public static void printSub(int index, List<Integer> lis, int n, int [] arr, int sum, int total){
        if(index >= n){
            if(sum == total)
                System.out.println(lis);
            return;
        }
        lis.add(arr[index]);
        total += arr[index];
        printSub(index + 1, lis, n, arr, sum, total);
        lis.remove(lis.size() - 1);
        total -= arr[index];
        printSub(index + 1, lis, n, arr, sum, total);
        return;
    }
}