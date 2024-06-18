public class second{
    int secondLargest(int[] a, int n) {
        int largest = a[0];
        int slargest = -1;
        for (int i = 1; i < n; i++) {
            if (a[i] > largest) {
                slargest = largest;
                largest = a[i];
            } else if (a[i] < largest && a[i] > slargest) {
                slargest = a[i];
            }
        }
        return slargest;
    }

    int secondSmallest(int[] a, int n) {
        int smallest = a[0];
        int ssmallest = Integer.MAX_VALUE;
        for (int i = 1; i < n; i++) {
            if (a[i] < smallest) {
                ssmallest = smallest;
                smallest = a[i];
            } else if (a[i] != smallest && a[i] < ssmallest) {
                ssmallest = a[i];
            }
        }
        return ssmallest;
    }

    public static void main(String[] args) {
        second sec = new second();
        int[] a = {12, 35, 1, 10, 34, 1}; // Example array
        int n = a.length;
        
        int slargest = sec.secondLargest(a, n);
        int ssmallest = sec.secondSmallest(a, n);
        
        System.out.println("Second Largest: " + slargest);
        System.out.println("Second Smallest: " + ssmallest);
    }
}
