


class Node:
    
    def __init__(self,data) -> None:
        self.data = data
        self.next_node = None
        
        

class LinkedList:
    
    def __init__(self) -> None:
        self.head = None
        self.size = 0
        
    def insert_start(self,data):
        self.size +=1
        new_node = Node(data)
        
        # if the linked list is empty
        if self.head is None:
            self.head = new_node
            
        else:
            new_node.next_node = self.head
            self.head = new_node            
        
        
    def insert_end(self,data):
        self.size +=1
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            
        else:
            self.insert_node(self.head,new_node)
            # node = self.head
            
            # while node.next_node:
            #     node = node.next_node
                
            # node.next_node = new_node
            
    def insert_node(self,node,actual_node):
        
        if node.next_node:
            self.insert_node(node.next_node)
            
        else:
            node.next_node = actual_node
            
    
    # def traverse(self):
        
    #     if self.head is None:
            