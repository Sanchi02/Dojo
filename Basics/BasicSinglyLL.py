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
        
listy = SinglyLL()

listy.insertAtHead(90)
listy.insertAtHead(46)
listy.insertAtHead(78)
listy.printList()
    