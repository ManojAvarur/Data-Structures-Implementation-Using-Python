class Node:
    def __init__(self,nodeValue=None):
        self.nodeData = nodeValue
        self.nextNode = None
        self.previousNode = None

class DDLL:
    def __init__(self):
        self.headNode = None

    def InsertElement(self,nodeValue):

        if self.headNode == None:
            self.headNode = Node(nodeValue)
        else:
            newNode = Node(nodeValue)
            
            nn = self.headNode
            # pn = None

            while nn.nextNode is not None:
                # pn = nn
                nn = nn.nextNode

            newNode.previousNode = nn
            nn.nextNode = newNode

    def printList(self):

        tempNode = self.headNode

        while tempNode is not None:
            print(tempNode.nodeData)
            tempNode = tempNode.nextNode




if __name__ == "__main__":
    Doubly = DDLL()
    Doubly.headNode = Node('Node 1')
    Doubly.InsertElement('Node 2')

    Doubly.printList()

        
