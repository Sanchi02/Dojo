class Node:
    def __init__(self, data=None):
        self.prev = None
        self.data = data
        self.next = None
        
class DoublyLL:
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
            self.head.prev = tempNode
            self.head = tempNode
            
    def insertAtTail(self, data):
        tempNode = Node(data)
        currNode = self.head
        while currNode and currNode.next is not None:
            currNode = currNode.next
        currNode.next = tempNode
        tempNode.prev = currNode    
            
listy = DoublyLL()

listy.insertAtHead(90)
# listy.insertAtHead(46)
# listy.insertAtHead(78)
listy.insertAtTail(45)
listy.insertAtTail(66)
listy.printList()

        