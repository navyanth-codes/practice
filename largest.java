import java.util.*;
import java.io.*;
public class largest {
    static int arr[] = {10,20,23,44,56,57};
    static int largestt(){
        int largest = arr[0];
        for(int i=0;i<arr.length;i++){
            if(arr[i]>largest){
                largest = arr[i];
            }
        }
        return largest;
    }
    public static void main(String[] args){
        System.out.println("the largest element is :"+largestt());
    }
}
