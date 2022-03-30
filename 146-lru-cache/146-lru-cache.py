class Node:
    def __init__(self, key = 0, value= 0, prev = None, next = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self, head=None, tail = None):
        self.head = head
        self.tail = tail
        
    def addfirst(self, node):
        nbr = self.head.next
        node.next = nbr
        
        nbr.prev = node
        self.head.next = node
        node.prev = self.head
        
    def remove(self, node):
        prevnbr = node.prev
        nextnbr = node.next
        prevnbr.next = nextnbr
        nextnbr.prev = prevnbr
        node.next = None
        Node.prev = None
        
    def moveinfront(self, node):
        # print(self.display())
        self.remove(node)
        # print(self.display())
        self.addfirst(node)  
        # print(self.display())
        # print()

    # def display(self):
    #     head = self.head
    #     tail = self.tail
    #     while(head != None):
    #         print(head.key, head.value, end  = "->")
    #         head = head.next
    #     print()
    #     while(tail != None):
    #         print(tail.key, tail.value, end= "<-")
    #         tail = tail.prev
    #     print()

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict1 = {}
        self.dl = DLL()
        head = Node()
        tail = Node()
        head.next = tail
        tail.prev= head
        self.dl.head = head
        self.dl.tail = tail
        

    def get(self, key):
        k = key
        if k in self.dict1:
            node = self.dict1[k]
            self.dl.moveinfront(node)
            return(node.value)

        else:
            return(-1)
        """
        :type key: int
        :rtype: int
        """
        

    def put(self, key, value):
        k = key
        v = value
        if k in self.dict1:
            node = self.dict1[k]
            node.value = v
            self.dl.moveinfront(node)
            #size check
        else:
            if len(self.dict1)<self.capacity:
                add = Node(k,v)
                self.dl.addfirst(add)
            else:
                node = self.dl.tail.prev
                rem_k = node.key
                self.dict1.pop(rem_k)
                self.dl.remove(node)
                add = Node(k,v)
                self.dl.addfirst(add)
            self.dict1[k] = add
        """
        :type key: int
        :type value: int
        :rtype: None
        """