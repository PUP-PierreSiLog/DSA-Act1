class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        
        removed_item = self.front.data
        self.front = self.front.next
        self.size -= 1

        if self.is_empty():
            self.rear = None
        
        return removed_item

    def front_element(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data

    def rear_element(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.rear.data