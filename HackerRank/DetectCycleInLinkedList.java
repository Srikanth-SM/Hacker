/*
Detect a cycle in a linked list. Note that the head pointer may be 'null' if the list is empty.

A Node is defined as: 
    class Node {
        int data;
        Node next;
    }
    
https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem
*/

boolean hasCycle(Node head) {
HashSet<Node> set = new HashSet();
    Node current = head;
    while(current!=null){
        if(set.contains(current)){
           return true;
        }
        set.add(current);
        current = current.next;
        
    }
    return false;
}
