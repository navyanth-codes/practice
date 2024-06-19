import java.util.Scanner;

public class movelastspace {

    public void rotate(int[] nums, int k) {
        int n = nums.length;
        // Adjust k to be within the bounds of the array length
        k = k % n;
        // If k is 0, no rotation is needed
        if (k == 0) return;

        int temp;
        for (int i = 0; i < k; i++) {
            temp = nums[0];
            for (int j = 1; j < n; j++) {
                nums[j - 1] = nums[j];
            }
            nums[n - 1] = temp;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the length of the array: ");
        int length = sc.nextInt();
        
        int[] nums = new int[length];
        System.out.println("Enter the elements of the array: ");
        for (int i = 0; i < length; i++) {
            nums[i] = sc.nextInt();
        }

        System.out.print("Enter the rotation value k: ");
        int k = sc.nextInt();

        movelastspace mls = new movelastspace();
        mls.rotate(nums, k);

        System.out.println("Array after rotation: ");
        for (int num : nums) {
            System.out.print(num + " ");
        }
    }
}
