
random_numbers=[56,0,63,34,6253,81,2,8,35,16,23,65]

user_input=input("enter the number you will like to search for \n ")
if user_input in random_numbers:

 print(True,f'",{user_input},found"')
else:
    print(False,",name not found")


def MyBinarySearchFunction(list, start, end, x):

    if end >= start:
        mid = start + (end - start) // 2

        if list[mid] == x:
            return mid
        elif list[mid] > x:
            return MyBinarySearchFunction(list, start, mid - 1, x)
        else:
            return MyBinarySearchFunction(list, mid + 1, end, x)

    else:
        return - 2


n = user_input
x=int(n)

result = MyBinarySearchFunction(random_numbers, 0, len(random_numbers) - 1, x)
if result != -2:
    print("Key is present at index " + str(result))
else:
    print("Key is not present in this List. ")