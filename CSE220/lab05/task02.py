def diamond_count(stack,string):
    stak = Stack()
    count_stak = Stack()
    leftbrac = ["<"]
    rightbrac = [">"]
    count = 1
    point = 0

    for i in string:
        if i in leftbrac:
            stak.push(i)
            count_stak.push(count)
        if i in rightbrac:
            if stak.pointer == -1:
                pass
            else:
                validate = False
                new = stak.pop()
                c = count_stak.pop()
                if new == '<' and i == ">":
                    validate = True
                    point += 1
                else:
                    validate = False

                if validate != False:
                    return point
        count += 1

    if stak.pointer == -1:
        return point
    else:
        return point



print('Test 01')
stack = Stack()
string = '<..><.<..>> '
returned_value = diamond_count(stack,string)
print(f'Number of Diamonds: {returned_value}') #This should print 3
unittest.output_test(returned_value, 3)
print('-----------------------------------------')


print('Test 02')
stack = Stack()
string = '<<<..<......<<<<....>'
returned_value = diamond_count(stack,string)
print(f'Number of Diamonds: {returned_value}') #This should print 1
unittest.output_test(returned_value, 1)
print('-----------------------------------------')


print('Test 03')
stack = Stack()
string = '>>><...<<..>>...>...>>>'
returned_value = diamond_count(stack,string)
print(f'Number of Diamonds: {returned_value}') #This should print 3
unittest.output_test(returned_value, 3)
print('-----------------------------------------')