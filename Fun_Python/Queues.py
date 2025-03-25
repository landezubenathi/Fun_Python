class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(data)

class Queue:
    def __init__(self):
        self.last = None
        self.first = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def dequeue(self):
        if self.first is None:
            return None
        else:
            r = self.first.data
            self.first = self.first.next
            return r
    def emptyqueue(self):
        #if queue is None
        if self.first is None: 
            return True
        else:
            return False

q = Queue()
q.enqueue("a")
q.enqueue("b")
q.enqueue("c")
print (q.dequeue())
print (q.dequeue())
print (q.dequeue())
print (q.dequeue())
print(q.emptyqueue())
