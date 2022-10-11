# ----- Linked List -----

#array: data stored at memories next to each other
#linked list: each nodes store memory and path to next node
##dynamic storage, linear search

#time complexity
##O(1) for insertnig at the head as no iteration needed
## O(n) for inserting at the bottom as have to iterate till the end of the list and check if next node exists

class Node:
    def __init__(self, data=None, next=None): #using __init__ to override system default function
        self.data = data
        self.next = next

class LinkedList: 
    def __init__(self):
        self.head = None

    def insert_head(self, data): 
        #data is the only param as inserting at head
        #current head becomes next list
        new_node = Node(data, self.head)
        self.head = new_node #current head is the node that previous head is next list
    
    def insert_end(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next: #stops before itr.next becomes none
            print("looking at the last node", itr.next)
            itr = itr.next
        itr.next = Node(data, None)

    def insert(self, data, index):
        if index<0 or index>=self.getLength():
            raise Exception("invalid index")

        if index == 0:
            self.insert_head(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                new_node = Node(data, itr.next) # in inserting new node is replacing next node
                itr.next = new_node
                break

            itr = itr.next
            count += 1

    def removeList(self, index):
        if index<0 or index>=self.getLength():
            raise Exception("invalid index")

        if index == 0: #when removing head
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1: #find the element before the index you wish to delete
                itr.next = itr.next.next #bring the element after the index to the index
            
            itr = itr.next
            count += 1

    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count = count+1
        return count

    def printLL(self):
        if self.head == None:
            return
        
        itr = self.head #assign head to iterate
        llstr = '' # holds data to print from linked list

        while itr: 
            llstr += str(itr.data) + "->"
            itr = itr.next #iterate through the list

        print (llstr)

if __name__ == '__main__':
    ll = LinkedList()
    print(ll)
    ll.insert_head(99)
    ll.insert_head(17)
    ll.insert_end(100)
    ll.insert_end(101)
    ll.printLL()
    print(ll.getLength())
    ll.removeList(2)
    ll.printLL()
    ll.insert("bye", 2)
    ll.insert("hello", 0)
    ll.printLL()



