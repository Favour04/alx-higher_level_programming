class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        
        if not isinstance(value, int):
            raise TypeError('data must be an integer')

        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
    
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value

class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def __str__(self):
        current = self.__head
        node = []
        while current:
            node.append(str(current.data))
            current = current.next_node
        return '\n'.join(node)
    
    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value, None)
        elif value < self.__head.data: 
            new = Node(value, self.__head)
            self.__head = new
        else:
            current = self.__head
            while current.next_node and value > current.next_node.data:
                current = current.next_node
            temp = current.next_node
            current.next_node = Node(value, temp)

