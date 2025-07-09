class Node:

    def __init__(self,val=None):

        self.val=val
        self.next=None

class LL:
    
    def __init__(self):

        self.head=None

    def disp(self):

        prnt=self.head

        while prnt is not None:
            print(prnt.val)
            prnt=prnt.next

    def atBegin(self,val):

        NewNode=Node(val)
        NewNode.next=self.head
        self.head=NewNode

lst=LL()
lst.head=Node(1)
e2=Node(2)
e3=Node(3)

lst.head.next=e2
e2.next=e3

#lst.disp()

lst.atBegin(0)
lst.atBegin(-1)
lst.disp()

