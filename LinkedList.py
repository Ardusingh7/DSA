class Node:

    def __init__(self,val=None):

        self.val=val
        self.next=None

class LinkL:

    def __init__(self):

        self.head=None

    def disp(self):

        prnt= self.head

        while prnt is not None:

            print(prnt.val,end=" ")
            prnt=prnt.next

h=LinkL()

h.head=Node(1)
e1=Node(2)
t=Node(3)

h.head.next=e1
e1.next=t

h.disp()