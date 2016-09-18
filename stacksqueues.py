# QUESTION 1
# Describe how you could use a single array to implement three stacks.

# Not perfect in terms of runtime:

class StackOfThree(object):

    def __init__(self):
        self.pos1 = 0
        self.pos2 = 1
        self.pos3 = 2
        self.stack = [None, None, None]

    def pop_one(self):
        if self.pos1 - 1 > 0:
            to_ret = self.stack.pop(self.pos1)
        self.pos2 -= 1
        self.pos3 -= 1

        return to_ret

    def push_one(self, value):
        self.stack.insert(self.pos1, value)
        self.pos2 += 1
        self.pos3 += 1

    # and so push_one

