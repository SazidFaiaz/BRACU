import head

def remove_block(st, n):
    temp_stack = Stack()

    for _ in range(n-1):
        temp_stack.push(st.pop())

    st.pop()

    while not temp_stack.isEmpty():
        st.push(temp_stack.pop())


def print_stack(st):
    temp_stack = Stack()

    while not st.isEmpty():
        element = st.pop()
        print(element)
        temp_stack.push(element)

    while not temp_stack.isEmpty():
        st.push(temp_stack.pop())


print('Test 01')
st = Stack()
st.push(4)
st.push(19)
st.push(23)
st.push(17)
st.push(5)
print('Stack:')
print_stack(st)
print('------')
remove_block(st,2)
print('After Removal')
print_stack(st)
print('------')

print()
print('======================================')
print()

print('Test 02')
st = Stack()
st.push(73)
st.push(85)
st.push(15)
st.push(41)
print('Stack:')
print_stack(st)
print('------')
remove_block(st,3)
print('After Removal')
print_stack(st)
print('------')

print()
print('======================================')
print()