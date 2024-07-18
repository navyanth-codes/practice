import java.util.*;

public class linked {
    Node head;
    private int size;

    Linked(){
        this.size=0;
    }

    class Node{
        String data;
        Node next;
        Node(String data){
            this.data = data;
            this.next = null;
            size++;
        }
    }
    public void addFirst(String data){
        Node newNode = new Node(data);
        if(head == null){
            head = newNode;
            return ;
        }
        newNode.next = head;
        head = newNode;
    }

    public void addLast(String data){
        Node newNode = new Node(data);
        if(head == null){
            head = newNode;
            return;
        }
        Node currNode = head;
        while(currNode.next!=null){
            currNode = currNode.next;
        }
        currNode.next = newNode;
    }

    public void deleteFirst(){
        if(head == null){
            System.out.println(" the list is empty");
            return;
        }
        size--;
        head = head.next;
    }
    public void deleteLast(){
        if(head == null){
            System.out.println(" the list is empty");
            return;
        }
        size--;
        if(head.next == null){
            head=null;
            return;
        }

        Node SecondLast = head;
        Node lastNode = head.next;
        while(lastNode.next != null){
            lastNode = lastNode.next;
            SecondLast = SecondLast.next;
        }
        SecondLast.next = null;

    }
    public void printList(){
        Node currNode = head;
        if(head == null){
            System.out.println("list is empty");
            return;
        }
        while(currNode!= null){
            System.out.print(currNode.data +" -> ");
            currNode = currNode.next;
        }
        System.out.println("NULL");
    }
    public int getSize(){
        return size;
    }

    public static void main(String args[]){
        linked list = new linked();
        list.addFirst("a");
        list.addFirst("is");
        list.printList();
        System.out.println(list.getSize());
    }
}
