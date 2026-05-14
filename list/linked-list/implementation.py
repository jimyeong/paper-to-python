
## todo Iterator add 

class LinkedListIterator: 
    def __init__(self, head_node): 
        self.cur_node = head_node
    
    def __next__(self):
        if(self.cur_node is None):
            raise StopIteration
        
        val = self.cur_node.val
        self.cur_node = self.cur_node.next
        return val
    def __iter__(self):
        return self

class Node: 
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val
        
    
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    def add(self, node_val):
            new_node = Node(node_val)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node

    def remove(self, target_val):
        node = self.head
        while node:
            if node.prev:
                node.prev.next = node.next
            else:
                self.head = node.next
            if node.next:
                node.next.prev = node.prev
            else:
                self.tail = node 
            node = node.next
    def update(self, target_val, new_val):
        node = self.head
        while node:
            if node.val == target_val:
                node.val = new_val
            node = node.next
            
    def __iter__(self): 
        return LinkedListIterator(self.head)
            
    