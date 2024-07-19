import java.util.ArrayList;
public class arraylist {
    
    public static void main(String args[]){
        ArrayList<Integer> list = new ArrayList<>();
        // add element 
        list.add(0);


        // System.out.println(list);
       // int element =  list.get(0);
        // System.out.println(element);

        // add in between
        list.add(2);
        list.add(2,1);
        System.out.println(list);

        // delete
        list.remove(2);
        System.out.println(list);

        // size
        int size = list.size();
        System.out.println(size);

        Collections.sort(list); 
    }
}
