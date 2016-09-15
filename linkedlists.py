# QUESTION 1
# Write code to remove duplicates from an unsorted linked list


def remove_dupes(lnkedlst):

    temp = set()

    current = lnkedlst.head

    if current is None:
        return

    prev = None

    while current is not None:
        if current.data not in temp:
            temp.add(current.data)
            prev = current
            current = current.next
        else:
            prev.next = current.next
            current = current.next


def remove_dupes_followup(lnkedlst):

    current = lnkedlst.head

    if current is None:
        return

    prev = None

    while current:
        iterator = current
        while iterator.next:
            if iterator.next.data == current.data:
                prev.next = iterator.next.next
            else:
                prev = iterator
                iterator = iterator.next
        current = current.next


# QUESTION 2
# Implement an algorithm to find the kth to last element of a singly linked list

def kth_to_last(lnkedlst, k):

    if lnkedlst.head is None:
        return

    current = lnkedlst.head

    length = 0
    counter = 0

    while current:
        length += 1
        current = current.next

    sought = (length - k) + 1

    current = lnkedlst.head

    while counter != sought:
        counter += 1
        current = current.next

    return current

def kth_to_last_better(lnkedlst, k):

    # set your beginning value
    current = lnkedlst.head
    # set your runner
    runner = current

    # go through the list and push runner forward
    for i in range(k):
        if runner is None:
            return None
        runner = runner.next

    # move runner and current together at the same time, until runner becomes None
    while runner:
        current = current.next
        runner = runner.next

    return current

# QUESTION 3
# Implement an algorithm to delete a node in the middle (ie, any node but first or last, not the exact middle)
# of a singly linked list, given only access to that node


def delete_middle_node(node):

    if not node or node.next:
        return False

    next_node = node.next
    node.data = next_node.data
    node.next = next_node.next

    return

# QUESTION 4
# Write code to partition a linked list around value x, such that nodes less than x
# come before all nodes greater than or equal to x. If x is within the list, the values
# of x only need to be after the elements less than x. The partition element x can appear anywhere in the
# right partition, it does need to appear between the left and right partitions

def partition_list(lnkedlst, partition_pt):

    current = lnkedlst.head

    if not current:
        return False

    end = lnkedlst.tail
    prev = None

    while current:
        if current.data < partition_pt:
            prev = current
            current = current.next
        else:
            prev.next = current.next.next
            next = current.next
            new_tail = current
            end.next = new_tail
            new_tail.next = None
            end = new_tail
            current = next


def partition(ll, x):

    current = ll.tail = ll.head

    while current:
        nextNode = current.next
        current.next = None
        if current.value < x:
            current.next = ll.head
            ll.head = current
        else:
            ll.tail.next = current
            ll.tail = current
        current = nextNode

    ll.tail.next = None

# QUESTION 5
# You have two numbers represented by a linked list, where each node contains a single digit
# The digits are stored in reversed order, such that the 1's digit is at the head of the list
# Write a function that adds the two numbers and returns the sum as a linked list

def sum_lists(lnkedlst1, lnkedlst2):

    current1 = lnkedlst1.head
    current2 = lnkedlst2.head

    # pretending we have imported a linked list class
    new_lnkedlst = LinkedList()
    new_current = new_lnkedlst.head = None

    remainder = 0

    # below assumes that the two lists are the same length
    while current1 or current2:
        our_sum = current1.data + current2.data
        if remainder == 0:
            if our_sum < 9:
                if not new_current:
                    new_current.data = our_sum
                    new_current.next = None
                    current1 = current1.next
                    current2 = current2.next
                else:
                    new_current.next.data = our_sum
                    new_current.next.next = None
                    new_current = new_current.next
                    current1 = current1.next
                    current2 = current2.next
            else:
                if not new_current:
                    new_current.data = str(our_sum)[1]
                    new_current.next = None
                    current1 = current1.next
                    current2 = current2.next
                    remainder = 1
                else:
                    new_current.next.data = str(our_sum)[1]
                    new_current.next.next = None
                    new_current = new_current.next
                    current1 = current1.next
                    current2 = current2.next
                    remainder = 1
        if remainder == 1:
            if our_sum < 8:
                if not new_current:
                    new_current.data = our_sum + remainder
                    new_current.next = None
                    current1 = current1.next
                    current2 = current2.next
                else:
                    new_current.next.data = our_sum + remainder
                    new_current.next.next = None
                    new_current = new_current.next
                    current1 = current1.next
                    current2 = current2.next
            else:
                if not new_current:
                    new_current.data = str(our_sum + remainder)[1]
                    new_current.next = None
                    current1 = current1.next
                    current2 = current2.next
                    remainder = 1
                else:
                    new_current.next.data = str(our_sum + remainder)[1]
                    new_current.next.next = None
                    new_current = new_current.next
                    current1 = current1.next
                    current2 = current2.next
                    remainder = 1

# much simpler & cleaner way to do what I did clumsily above
def sum_lists(ll_a, ll_b):
    n1, n2 = ll_a.head, ll_b.head
    ll = LinkedList()
    carry = 0
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next

        ll.add(result % 10)
        carry = result // 10

    if carry:
        ll.add(carry)

    return ll

#QUESTION 6
#Implement a function to check if a linked list is a palindrome

def check_palindrome(ll):
    """Figure out how to do this recursively"""

    # if given whole list (or head and tail) rather than just a node
    if ll.head.data != ll.tail.data:
        return False

    #set a fast and a slow runner
    #go through list and push first half onto stack

    stack = []

    fast = slow = ll.head

    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    # skips over middle value if there is an odd number of nodes in the list
    if fast:
        slow = slow.next

    # goes through the stack and compares the rest of the LL to the stack values
    while slow:
        top = stack.pop()
        if top != slow.data:
            return False
        slow = slow.next

    return True

# QUESTION 7 
# Write a function to check if two singly linked lists intersect

def check_intersection(ll1, ll2):
    # assumes you don't have access to tail initially (instead you loop through and get it)

    ll1_length = 0
    ll1_tail = None

    ll2_length = 0
    ll2_tail = None

    # gets length and tail nodes
    while ll1_node:
        ll1_length += 1
        ll1_tail = ll1_node
        ll1_node = ll1_node.next

    while ll2_node:
        ll2length += 1
        ll2_tail = ll2_node
        ll2_node = ll2_node.next

    # confirm whether this would work or if you'd have to say "is not" to reference exact thing in memory
    if ll1_tail != ll2_tail:
        return False

    shorter = (ll1, ll1_length) if ll1_length < ll2_length else (ll2, ll2_length)

    longer = (ll1, ll1_length) if ll1_length > ll2_length else (ll2, ll2_length)

    diff = longer[1] - shorter[1]

    shorter_node, longer_node = shorter[0].head, longer[0].head

    # goes through and advances longer list so you can go through both simultaneously
    for i in range(diff):
        longer_node = longer_node.next

    #since you already know the tails are the same, you just need the intersection
    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    # you could also return shorter node here, it doesn't matter
    return longer_node

# QUESTION 8
# Given a circular linked list, return the node at the beginning of the loop

def circular_ll_node(ll):




