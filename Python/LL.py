class Node:

    def __init__(self,val=None):

        self.val=val
        self.next=None

class LL:

    def __init__(self):
        
        self.head=None

    def insert(self,val):

        newnode=Node(val)
        if(self.head==None):
            self.head=newnode
        else:
            curr=self.head
            while (curr.next!=None):
                curr=curr.next
            curr.next=newnode
    
    def insert_beg(self,val):

        newnode=Node(val)
        newnode.next=self.head
        self.head=newnode
    
    def insert_spec(self,val2,index):

        newnode2=Node(val2)
        curr=self.head

        for i in range(1,index-1):
            curr=curr.next
        #print(curr.val)
        newnode2.next=curr.next
        curr.next=newnode2
        #curr.next=newnode2
    
    def del_head(self):

        temp=self.head
        self.head=self.head.next
        temp=None
        
    def del_tail(self):

        temp2=self.head

        while temp2 is not None:
            prev=temp2
            temp2=temp2.next
        prev.next=None
        temp2=None
 
    def disp(self):

        prnt=self.head
        while(prnt is not None):
            print(prnt.val,end=" ")
            prnt=prnt.next

lst=LL()
#lst.insert(1)
lst.insert(2)
lst.insert(3)
lst.insert_beg(1)
lst.insert_spec(4,4)
lst.del_head()
lst.del_tail()
lst.disp()