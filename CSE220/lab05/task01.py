def balance_parenthesis(string):
  stak = Stack()
  contr_stack = Stack()
  leftbrac = ['(',"{","["]
  rightbrac = [")","}","]"]
  count = 1
  for i in string:
    if i in leftbrac:
      stak.push(i)
      contr_stack.push(count)

    if i in rightbrac:
      if stak.pointer == -1:
        return False
      else:
        validity = False
        new = stak.pop()
        c = contr_stack.pop()
        if new == "(" and i == ")":
          validity = True
        elif new == "{" and i == "}":
          validity = True
        elif new == "[" and i == "]":
          validity = True
        else:
          validity = False

        if validity != True :
          return False

    count += 1
  if stak.pointer == -1:
    return True
  else:
    return False


print('Test 01')
s = '1+2*(3/4)'
returned_value = balance_parenthesis(s)
print('Balanced') if returned_value else print('Unbalanced') #This should print Balanced
unittest.output_test(returned_value, True)
print('-----------------------------------------')

print('Test 02')
s = '1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14' #mismatch
returned_value = balance_parenthesis(s)
print('Balanced') if returned_value else print('Unbalanced') #This should print Unbalanced
unittest.output_test(returned_value, False)
print('-----------------------------------------')

print('Test 03')
s = '[10*[3-(5-2)]' #unpaired opening bracket
returned_value = balance_parenthesis(s)
print('Balanced') if returned_value else print('Unbalanced') #This should print Unbalanced
unittest.output_test(returned_value, False)
print('-----------------------------------------')

print('Test 04')
s = '(A+B)-C)' #unpaired closing bracket
returned_value = balance_parenthesis(s)
print('Balanced') if returned_value else print('Unbalanced') #This should print Unbalanced
unittest.output_test(returned_value, False)
print('-----------------------------------------')

print('Test 05')
s = '([A+B]-C)/{D*E}+[2*[(2A+5){5B}]-{7C-9AB}]'
returned_value = balance_parenthesis(s)
print('Balanced') if returned_value else print('Unbalanced') #This should print Balanced
unittest.output_test(returned_value, True)
print('-----------------------------------------')