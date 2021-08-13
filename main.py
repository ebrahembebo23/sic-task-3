# ask user to enter the size of the list
li_size = int(input("How many numbers are in the list : "))
# Define "number entered" list and list of final result
numbers_li = []
final_li = []
# loop to ask user to enter items of list depended on size of list
for i in range(0, li_size):
    numbers_li.append(int(input("Enter list item {} : ".format(i + 1))))
# ask user to input the number that divisible numbers of
n = int(input("Enter divider : "))


# define function that include loop that make the equation
def divisible(n_li, s_li, f_li, x):
    for ctr in range(0, s_li):
        if n_li[ctr] % x == 0:
            f_li.append(n_li[ctr])


# calling function
divisible(numbers_li, li_size, final_li, n)
# printing the final result
print("Numbers that are divisible by {} is : ".format(n), final_li)
