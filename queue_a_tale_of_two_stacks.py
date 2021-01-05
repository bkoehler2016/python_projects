"""
9/10 said they did whiteboarding
1/10 "no, we use live coding online..." == whiteboarding?
Queuejumper

U

Make a queue, by completing push/pop/peek, using 2 stacks

Stacks have push/pop, and act like a stack of pancakes. Last one on top, first one off.
Make two stacks act like a line/queue



Output: if peek, return element at front of queue

Input: the tests will call enqueue/dequeue/peek (put/pop/peek)

Constraints: we'll always call at least one of these methods, we'll only enqeue/put positive integers up to 10**9

Edge cases?? Dequeue/peek from empty queue, enqueue past memory limits.

P
Use Python array as stack by only using .push and .pop

How are we going to accomplish dequeue with two stacks that only have push and pop?

Enqueue/put
array.push - easy

Dequeue/pop
Pop each element out of stack 1, append it to stack 2
This reverses our stack, so we get the first element in, out first

Then pop out of stack 2, to remove the element

Restore all the items to stack 1.

Peek
return stack1[0], or stack2[-1]

E
- passed a bunch of tests first try!!

R
- can we make this faster??
- peek is O(1)
- put/enqueue is O(1)
- dequeue is O(2n)

- try while-loop instead of for-loop with range
- append the pop directly

        # if written in Python, no faster than our implementation
        # But a lot of stuff is delegated to C and that is faster
        # so....maybe faster??
        reversed_list = original_list[::-1]
        
        This turned out to be fast enough to pass the tests
        Check the implementation / interwebz, it's probably passed off to C
        
stack1 = [2, 3, 4, 5, 6]
stack2 = []
stack1.append()

stack1.pop()
stack2.append()
stack2.append(stack1.pop())

stack2.pop()
"""


class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    # they'll use this to test
    def peek(self):
        if len(self.stack1):
            return self.stack1[0]
        
    # dequeue - this should be O(1) but it's gonna be O(2n) == O(n)
    
    # 1. Make a new array
    # 2. Loop backwards over old array, append to new array
    # 3. Return new array
    def pop(self):
       self.stack2 = self.stack1[::-1]
       return_value = self.stack2.pop()
       self.stack1 = self.stack2[::-1]
       return return_value
   
       """
       # Pop each element out of stack 1, append it to stack 2
       while len(self.stack1):
            self.stack2.append(self.stack1.pop())
       # Then pop out of stack 2, to actually dequeue the element
       return_value = self.stack2.pop()
       # Restore all the items to stack 1.
       while len(self.stack2):
            self.stack1.append(self.stack2.pop())
            

       # do we have to return the value? idk
       return return_value
      """  
      
    # enqueue
    def put(self, value):
        self.stack1.append(value)
        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())