
#linked list , infinate,
"""
store integer,
deleteme() => take Null pointer => delete that value from the linkedlist

linkedlis: val, next, previous

class linkedlist:
    self __init__(self, val, next):
        self.val = val
        self.next = next
7 => 5 => 4 => 3 ...
     ^
   node
   node.next = 4
   node.val = 5

   node.val = node.next
7 => 4 => 4 => 3 ...
     ^
     node
     node.next = 4
     node.next.next.val = 3
     node = node.next.next
7 => 4 => 3  ...


def deleteme(node):
    #copy the 4 to the 5
    node.val = node.next.val
    #7 => 4 => 4 => 3 ...

    #delete the old 4
    node.next = node.next.next


















val: 7
next: 5


temp pointer point to 7
run a loop iterate through the linkedlist
temp = temp.next
if temp.val == value:
    #remove
else:
    continue






7 => 4 => 3
"""

def deleteme():
