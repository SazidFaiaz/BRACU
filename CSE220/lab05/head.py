import fhm_unittest as unittest
import numpy as np

class Node:
  def __init__(self,elem=None,next=None):
    self.elem = elem
    self.next = next

class Stack:
  head = None
  pointer = -1

  def __init__(self):
    pass

  def push(self,elem):
    if self.head == None:
        self.head = Node(elem, None)
        self.pointer += 1
    else:
        n = Node(elem, None)
        n.next = self.head
        self.head = n
        self.pointer += 1

  def pop(self):
    if self.head == None:
      return None

    temp = self.head
    self.head = self.head.next
    temp.next = None
    self.pointer -= 1
    return temp.elem


  def peek(self):
    if self.head == None:
      return None
    return (self.head.elem)

  def isEmpty(self):
    if self.head == None:
      return True


st = Stack()
st.push(4)
st.push(3)
st.push(5)
st.push(1)
st.push(9)


print('Peeked Element: ',st.peek()) #This should print 9
print('Popped Element: ',st.pop()) #This should print 9
print('Popped Element: ',st.pop()) #This should print 1
print('Popped Element: ',st.pop()) #This should print 5
print('Peeked Element: ',st.peek()) #This should print 3
print('Popped Element: ',st.pop()) #This should print 3
print('Popped Element: ',st.pop()) #This should print 4
print('Peeked Element: ',st.peek()) #This should print None
print('Popped Element: ',st.pop()) #This should print None
print(st.isEmpty()) #This should print True
