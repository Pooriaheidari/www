class Node:
    def __init__(self, data):
        self.data = data
        self.next=None
        
         
class CircularLinkedList:

    def __init__(self):
         self.head=None
# append data to list.
    def append(self, data):
        node=Node(data)
        self.insert_at_end(node)

# The next two def are for head and previous node.

# find the first element to move on nodes.
    def get_node (self, index, start):
        if self.head is None:
            return None
        current = start
        for i in range (index) :
            current=current.next
        return current

# find last elemnt.
    def get_prev_node (self, ref_node):
        if self.head is None:
            return None
        current=self.head
        while current.next!= ref_node:
            current = current.next

        return current

   
    def insert_after(self , ref_node , new_node):

        new_node.next= ref_node.next
        ref_node.next = new_node

    def insert_before(self , ref_node , new_node):

        prev_node = self.get_prev_node(ref_node)
        self.insert_after(prev_node , new_node)

    def insert_at_end(self , new_node):

        if self.head == None:
            self.head = new_node
            new_node.next = new_node
        else:
            self.insert_before(self.head , new_node)

    def remove(self , node):

        if self.head.next == self.head:
            self.head = None
        else:
            prev_node=self.get_prev_node (node)
            prev_node.next=node.next
            if self.head==node:
                self.head=node.next

  
def has_one_node(cllist):

    if cllist.head.next==cllist.head:
        return True
    else:
        return False

def get_josephus_solution(cllist,k):

    if cllist.head is None:
        return None

    start=cllist.head

    while not has_one_node(cllist):
        to_remove=cllist.get_node (k-1, start)
        start=to_remove.next
        cllist.remove(to_remove)

    return cllist.head.data

a_cllist=CircularLinkedList ()

n = int(input ("Enter number of people here: "))
k = int(input ("The kth person will be executed. Enter k: "))

for i in range(1,n+1):
    a_cllist.append(i)
 
ans=get_josephus_solution(a_cllist,k)
print ("The person at position {} wont be killed.".format (ans) )
