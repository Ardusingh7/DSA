def TOH(n,fro,to,aux):

    cnt=0
    if n==0:
        return
    
    TOH(n-1,fro,aux,to)
    print("Disk {}; from {} to {}".format(n,fro,to))
    TOH(n-1,aux,to,fro)

TOH(2,"A","B","C")