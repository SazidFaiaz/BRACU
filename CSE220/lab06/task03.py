
def hocoBuilder(height):
    if height == 0:
        return "No house"
    elif height == 1:
        return 8
    else:
        return 5 + hocoBuilder(height-1)

print("Total nymber of cards:",hocoBuilder(int(input("enter the height:"))))