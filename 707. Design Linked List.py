class MyLinkedList:
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        ptr = self.head
        for i in range(index):
            if(ptr):
                ptr = ptr.right
            else:
                break
        if ptr:
            return ptr.val
        else:
            return -1
        
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = self.Node(val)
        node.right = self.head
        node.left = None
        if self.head:
            self.head.left = node
        self.head = node
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if(not self.head):
            node = self.Node(val)
            self.head = node
        else:
            pre, ptr = None, self.head
            while(ptr):
                pre = ptr
                ptr = ptr.right
            node = self.Node(val)
            pre.right = node
            node.left = pre
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        ptr, cancel = self.head, False
        for i in range(index):
            if ptr:
                ptr = ptr.right
            else:
                cancel = True
                break
        if not cancel:
            if ptr == self.head:
                self.addAtHead(val)
            elif ptr == None:
                self.addAtTail(val)
            else:
                node = self.Node(val)
                node.right = ptr
                node.left = ptr.left
                ptr.left.right = node
                ptr.left = node
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        ptr = self.head
        for i in range(index):
            if ptr:
                ptr = ptr.right
            else:
                break
        if ptr:
            if ptr == self.head:
                if(ptr.right):
                    ptr.right.left = None
                self.head = ptr.right
            elif ptr.right == None:
                ptr.left.right = None
            else:
                ptr.left.right = ptr.right
                ptr.right.left = ptr.left
            ### free ptr
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

if __name__ == '__main__':
    obj = MyLinkedList()
    obj.addAtHead(7)
    obj.addAtHead(2)
    obj.addAtHead(1)
    obj.addAtIndex(3, 0)
    obj.deleteAtIndex(2)

    ### 1 2 7 0
    ptr = obj.head
    while(ptr):
        print(ptr.val)
        ptr = ptr.right
    
    #print(obj.get(1))