class LNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def preInsert(head, val):
    elem = LNode(val)
    if head:
        elem.next = head
    return elem

def lastInsert(head, val):
    p = head
    while p.next != None:
        p = p.next
    elem = LNode(val)
    p.next = elem
    return head

def insert(head, val, index):
    if index <= 0:
        raise RuntimeError('index must be positive')
    elif index == 1:
        return preInsert(head, val)
    else:
        p = head
        while p != None and index - 2 != 0:
            p = p.next
            index -= 1
        if p == None:
            raise RuntimeError('index is too big')
        else:
            elem = LNode(val)
            elem.next = p.next
            p.next = elem
            return head

def printList(head):
    while head != None:
        print(str(head.val) + '->', end='')
        head = head.next

def deleteList(head):
    head = None
    return head

def isEmpty(head):
    return head == None
    
def preDelete(head):
    return head.next if head != None else head

def delete(head, val):
    p = head
    while p != None and p.next != None and p.next.val != val:
        p = p.next
    p.next = p.next.next if p.next != None else p.next
    return head

def locateElem(head, val):
    if head == None:
        return head
    else:
        p, index = head, 1
        while p != None and p.val != val:
            p = p.next
            index += 1
        return -1 if p == None else index

if __name__ == '__main__':
    head = LNode(10)
    for i in range(10):
        head = lastInsert(head, i)
    head = insert(head, 22, 11)
    printList(head)