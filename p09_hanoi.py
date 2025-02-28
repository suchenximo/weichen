
def hanoi(panes,src,buffer,dst):
    if panes == 1:
        print('Move %s == %d ==> %s' % (src,1,dst))
    else:
        hanoi(panes-1,src,dst,buffer)
        print('Move %s == %d ==> %s' % (src, panes, dst))
        hanoi(panes - 1,buffer, src, dst)






if __name__ == '__main__':
    hanoi(4,'A','B','C')