class Node():
    def __init__(self,val, next):
        self._val = val
        self._next = next

def ll_2_array(head):
    ret = []
    current = head
    while current:
        ret.append(current._val)
        current = current._next
    return ret

def list_2_ll(_list):
    if len(_list) == 0:
        return None
    print("The problem is " + str(_list))
    ret = Node(0,None)
    curr = ret
    for x in range(0,len(_list)):
        curr._val = _list[x]
        if not x == len(_list)-1:
            curr._next = Node(0,None)
        curr = curr._next
    return ret


def linked_add(head1, head2):
    list1 = []
    list2 = []

    while head1:
        list1.append(head1._val)
        head1 = head1._next
    print(str(list1))
    while head2:
        list2.append(head2._val)
        head2 = head2._next
    
    print(str(list2))
    sum1 = 0
    multiplier = 1

    for x in range (len(list1)-1,-1,-1):
        sum1 += list1[x]*multiplier
        multiplier *=10
        # print(sum1)

    sum2 = 0
    multiplier = 1
    for x in range (len(list2)-1,-1,-1):
        sum2 += list2[x]*multiplier
        multiplier *=10
    print (sum1)
    print (sum2)
    total = sum1 + sum2
    return total

def numeric_convert(input_int):
    current_int = input_int
    vals = []
    while current_int > 0:
        remainder = current_int % 10
        print ("digit is " + str(remainder))
        current_int = current_int // 10
        if current_int == 0:
            break 
        vals.append(remainder)
    vals.reverse()
    return list_2_ll(vals)



def string_convert(input_int):
    int_str = str(input_int)
    ret = None
    current = None
    for x in range (0,len(int_str)):
        if ret == None:
            ret = Node(int(int_str[x]),None)
            current = ret
        else:
            next = Node(int(int_str[x]),None)
            current._next = next
            current = next
    return ret


node_1d = Node(3,None)
node_1c = Node(2,node_1d)
node_1b = Node(4,node_1c)
node_1a = Node(8,node_1b)

node_2d = Node(8,None) 
node_2c = Node(5,node_2d)
node_2b = Node(0,node_2c)
node_2a = Node(3,node_2b)

result = linked_add(node_1a,node_2a)
str_list = ll_2_array(string_convert(result))
numeric_list = ll_2_array(numeric_convert(result))
print(str(str_list))
print(str(numeric_list))

# print(result)

