import fhm_unittest as unittest
import numpy as np
class Node:
  def __init__(self,elem,next = None):
    self.elem,self.next = elem,next
def createList(arr):
  head = Node(arr[0])
  tail = head
  for i in range(1,len(arr)):
    newNode = Node(arr[i])
    tail.next = newNode
    tail = newNode
  return head
def printLinkedList(head):
  temp = head
  while temp != None:
    if temp.next != None:
      print(temp.elem, end = '-->')
    else:
      print(temp.elem)
    temp = temp.next
  print()
  def conga_line(head):

      temp = head
      while temp.next:
          if temp.elem > temp.next.elem:
              return False
          temp = temp.next
      return True

  head = createList(np.array([10, 15, 34, 41, 56, 72]))
  print('Original Conga Line: ', end=' ')
  printLinkedList(head)
  returned_value = conga_line(head)
  print(returned_value)  # This should print True
  unittest.output_test(returned_value, True)
  print()

  head = createList(np.array([10, 15, 44, 41, 56, 72]))
  print('Original Conga Line: ', end=' ')
  printLinkedList(head)
  returned_value = conga_line(head)
  print(returned_value)  # This should print False
  unittest.output_test(returned_value, False)
  print()