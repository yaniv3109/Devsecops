# homework

## 1
# number = int(input("Enter a number: "))
# for i in range(1, number):
#     if number % i == 0:
#         print(i)

## 2
# counter = 1
# sum_numbers = 0
# while True:
#     number = int(input("Enter a number: "))
#     if number < 0:
#         print("Thanks")
#         break
#     sum_numbers += number
#     print(f"#{counter} (average: {sum_numbers/counter}, sum: {sum_numbers}) number: {number}")
#     counter += 1


## 3
# list_words = []
# while True:
#     word = input("Enter a word: ")
#     if list_words.count(word) > 1:
#         print("DRY - dont repeat yourself")
#         break
#     list_words.append(word)

## 4
# list_1 = [4,4,4,6,7]
# list_2 = [-1,3,2,1,9,34,67]
# counter = 0
# if len(list_1) > len(list_2):
#     smallest_list = len(list_2)
# else:
#     smallest_list = len(list_1)


# for i in range(smallest_list):
#     if list_1[i] > list_2[i]:
#         print(f"{list_1[i]}(list1) is bigger than {list_2[i]}(list2)")
#         counter += 1
#     else:
#         print(f"{list_2[i]}(list2) is bigger than {list_1[i]}(list1)")

# if (counter) > (len(list_1)/2):
#     print("list_1 is bigger")
# else:
#     print("list_2 is bigger")