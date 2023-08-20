
def get_hash(key):
    h = 0
    for i in key:
        h += ord(i)
    return h % 100

print(get_hash("march 6"))