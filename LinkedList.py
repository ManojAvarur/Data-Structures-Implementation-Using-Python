# There are many changes to be done

import time as t

class Node:
    def __init__(self,dataval=None):
        self.nodeData = dataval
        self.nextNode = None

class SinglyLinkedList:
    def __init__(self):
        self.headNode = None

    def RemoveAnItemFromList(self, nodeValue):
        tempNode = self.headNode
        previousNode = None

        if self.headNode.nodeData == nodeValue:
            self.headNode = self.headNode.nextNode

        while not tempNode.nodeData is nodeValue:
            previousNode = tempNode
            tempNode = tempNode.nextNode
        
        previousNode.nextNode = tempNode.nextNode
            
    def printList(self):
        printVal = self.headNode
        while printVal is not None:
            print(printVal.nodeData)
            printVal = printVal.nextNode

    def InsertAtBeginning(self, nodeInfo):
        NewNode = Node(nodeInfo)
        NewNode.nextNode = self.headNode
        self.headNode = NewNode


    def InsertAtEnd(self, nodeInfo):

        newNode = Node(nodeInfo)

        if self.headNode == None:
            self.headNode = newNode
        
        nextNode = self.headNode

        while nextNode.nextNode is not None:
            nextNode = nextNode.nextNode

        nextNode.nextNode = newNode


    def InsertAtAnyPosition(self, position, nodeInfo):

        nextnode = self.headNode
        count = 2

        while nextnode.nextNode is not None :
            if( position == count ):
                newnode = Node(nodeInfo)
                newnode.nextNode = nextnode.nextNode
                nextnode.nextNode = newnode
                return
            elif count > position:
                print("You can;t insert at first position!")

            nextnode = nextnode.nextNode
            count += 1

        print('Position not found!')


            

       


# Linked List has been created

node1 = SinglyLinkedList()

# Node 1 is set as head node
node1.headNode = Node('Node 1')

# Created two new nodes
node2 = Node('Node 2')
node3 = Node('Node 3')

# Linking the next nodes
node1.headNode.nextNode = node2
node2.nextNode = node3


# nextNode = node1.nextNode

# print(node2.nodeData)
# node1.InsertAtBeginning('NewNodeInserted')

# node1.InsertAtEnd('Lastnode')

# node1.InsertAtAnyPosition(9,'None')

print()

node1.InsertAtEnd('NodeLast')

node1.printList()

print()

node1.RemoveAnItemFromList('NodeLast')

print()

node1.printList()