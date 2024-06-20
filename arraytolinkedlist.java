public class arraytolinkedlist {
    static class Node {
        int data;
        Node next;

        Node(int data1, Node next1) {
            this.data = data1;
            this.next = next1;
        }

        Node(int data1) {
            this.data = data1;
            this.next = null;
        }
    }

    public static class LinkedList {
        private static Node Convertarr2LL(int[] arr) {
            // if (arr == null || arr.length == 0) {
            //     return null; // Handle the case of empty array
            // }

            Node head = new Node(arr[0]);
            Node mover = head;
            for (int i = 1; i < arr.length; i++) { // Start from 1 to avoid duplicating head
                Node temp = new Node(arr[i]);
                mover.next = temp;
                mover = mover.next;
            }
            return head;
        }

        public static void main(String[] args) {
            int[] arr = {2, 3, 4, 5};
            Node head = Convertarr2LL(arr);
            System.out.println(head.data);
        }
    }
}








    // APPROACH 1
    // public static void main(String[] args){
    //     String[] str={"A","b","C"};
    //     List<String> list=Arrays.asList(str);
    //     LinkedList<String> linkedlist = new LinkedList<String>(list);
    //     System.out.println(linkedlist);
    // }

