from Node import Node

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple_nodes(values)
            
    def __str__(self):
        return ' -> '.join([str(node) for node in self])
    
    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count
    
    def __iter__(self):
        if self.head is None:
            yield None
        else:
            current = self.head
            yield current
            current = current.next
            while current != self.head:
                yield current
                current = current.next
            
    @property
    def values(self):
        return [node.value for node in self if self.head is not None]
    
    def add_node(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    
    def add_multiple_nodes(self, values):
        for value in values:
            self.add_node(value)
            
    def add_node_as_head(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        return self.head

class DoublyLinkedList(LinkedList):
    def __str__(self):
        return ' <-> '.join([str(node) for node in self])

    def add_node(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value, None, self.tail)
            self.tail = self.tail.next
        self.tail.next = self.head
        self.head.prev = self.tail
        return self
    
    def add_node_as_head(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            current_head = self.head
            self.head = Node(value, current_head)
            current_head.prev = self.head
        return self.head
    
    def exchange(self, n: int , k: int, pos: int):
        if self.head is None:
            return
        node = self.head
        n_count = 0
        while node and n_count != n:
            node = node.next
            n_count += 1
        print("node is",node)

        if node is not None:
            n_node = node
            k_count = 0
            if pos == 1: # look for next node
                while n_node and k_count != k:
                    n_node = n_node.next
                    k_count += 1
            elif pos == -1: # look for prev node
                while n_node and k_count != k:
                    n_node = n_node.prev
                    k_count += 1
            print("n_node is",n_node)
            node.value, n_node.value = n_node.value, node.value 

        
