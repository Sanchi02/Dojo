class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None
        
    def printList(self):
        currNode = self.head
        val = currNode.data
        while currNode is not None:
            print(val)
            currNode = currNode.next
            if(currNode is not None):
                val = currNode.data
        
    def insertAtHead(self, data):
        tempNode = Node(data)
        if(self.head is None):
            self.head = tempNode
        else:
            tempNode.next = self.head
            self.head = tempNode
            
    def sizeOfList(self):
        currNode = self.head
        num = 1
        while(currNode.next):
            currNode = currNode.next
            num +=1
        return num
            
    def insertAtLoc(self,data, position):
        if(position==0):
            self.insertAtHead(data)
        if(position>self.sizeOfList()+1):
            print("Number out of range")
            return
        currNode = self.head
        for i in range(2,position):
            currNode = currNode.next
        nextNode = currNode.next
        tempNode = Node(data)
        currNode.next = tempNode
        tempNode.next = nextNode
        
    def reverseList(self): 
        prevNode = None
        currNode = self.head 
        while(currNode is not None): 
            nextNode = currNode.next
            currNode.next = prevNode 
            prevNode = currNode
            currNode = nextNode
        self.head = prevNode
        
    def reverseUtil(self, curr, prev): 
        if curr.next is None : 
            self.head = curr  
            curr.next = prev 
            return 
        next = curr.next  
        curr.next = prev 
        self.reverseUtil(next, curr)  
  
    def reverse(self): 
        if self.head is None: 
            return 
        self.reverseUtil(self.head, None)
                 
listy = SinglyLL()

listy.insertAtHead(90)
listy.insertAtHead(46)
listy.insertAtHead(78)
listy.insertAtLoc(45,4)
listy.printList()
print("Reversing")
listy.reverseList()
listy.printList()
print("Recursive reversal")
listy.reverse()
listy.printList()
# listy.sizeOfList()

    