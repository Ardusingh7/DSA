class Node:

    def __init__(self,val):
        
        self.val=val
        self.next=None
        #self.preq=None

class LL:

    def __init__(self):
        
        self.head=None

    def insert(self,val):

        newnode=Node(val)

        if self.head==None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
        
    def rev_(self):

        preq=None
        curr=self.head

        while curr is not None:

            next=curr.next
            curr.next=preq
            preq=curr
            curr=next
        
        self.head=preq

    def disp(self):

        prnt=self.head

        while prnt is not None:

            print(prnt.val,end=" ")
            prnt=prnt.next

lst=LL()
lst.insert(1)
lst.insert(2)
lst.insert(3)
print("Before:")
lst.disp()
lst.rev_()
print(  )
print("After:")
lst.disp()