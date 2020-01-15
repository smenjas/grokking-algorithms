def print_items(list):
    for item in list:
        print(item)

from time import sleep
def print_items2(list):
    for item in list:
        sleep(1)
        print(item)

list = [2, 4, 8, 6, 10]

print_items(list)
print_items2(list)
