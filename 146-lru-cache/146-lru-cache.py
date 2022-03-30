class Node:
    def __init__(self, key = 0, value= 0, prev = None, next = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.lruNode = None
        self.mruNode = None
        self.key2node = {}
        
    def addFirst(self, node):
        self.key2node[node.key] = node
        if self.mruNode:
            node.next = self.mruNode
            self.mruNode.prev = node
            self.mruNode = self.mruNode.prev
        else:
            self.lruNode, self.mruNode = node, node
        
    def remove(self, node):
        previousNode = node.prev
        nextNode = node.next
        if previousNode:
            previousNode.next = nextNode
        else:
            self.mruNode = node.next
        if nextNode:
            nextNode.prev = previousNode
        else:
            self.lruNode = node.prev
        node.prev = None
        node.next = None
        del self.key2node[node.key]
            
    def moveToMRU(self, node):
        self.remove(node)
        self.addFirst(node)
    
    def removeLRU(self):
        del self.key2node[self.lruNode.key]
        self.lruNode = self.lruNode.prev
        if self.lruNode:
            self.lruNode.next = None
        else:
            self.mruNode = None
        

    def display(self):
        head = self.mruNode
        tail = self.lruNode
        print('         ')
        print('--START--')
        while(head != None):
            print(head.key, head.value, end  = "->")
            head = head.next
        while(tail != None):
            print(tail.key, tail.value, end= "<-")
            tail = tail.prev
        print('        ')
        print('--END--')
        

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.count = 0
        self.dll = DLL()
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dll.key2node:
            node = self.dll.key2node[key]
            self.dll.moveToMRU(node)
            # self.dll.display()
            return node.value
        else:
            # self.dll.display()
            return -1
        
        
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = Node(key, value, None, None)
        if key in self.dll.key2node:
            node = self.dll.key2node[key]
            node.value = value
            self.dll.moveToMRU(node)
        elif self.count < self.capacity:
            self.dll.addFirst(node)
            self.count += 1
        elif self.count == self.capacity:
            self.dll.removeLRU()
            self.dll.addFirst(node)
        # self.dll.display()
        
            