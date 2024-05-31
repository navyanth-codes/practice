import java.io.*;
public class reverse{
    public static void rev(int[] arr){
        int[] revadd = new int[arr.length];
        for(int i=0;i<arr.length;i++){
            revadd[i]=arr[arr.length-i-1];
        }
        System.out.print("Reversed Array:");
        for( int i : revadd){
            System.out.print(i+" ");
        }
    }
    public static void main(String[] args){
        int[] arriginalArr = {1,2,3,4,5,6,7};
        rev(arriginalArr);
    }
}
