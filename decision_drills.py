def loves_code(value):
    if value:
        print('I love to code!')
    else:
        print('coding has its challenges')

loves_code(True)
loves_code(False)


bryans_age = 36
krystles_age = 33
bryansbirthyear = 1989
krystlesbirthyear = 1992

def age_check():
    if bryans_age < krystles_age:
        print ('Krystle Is oldest')
    elif bryans_age == krystles_age:
        print ('They are the same age')
    else:
        print('Bryan is oldest')
age_check()



def item_list():
    return [10, 20, 30, 40, 50, 60]

def first_item(array):
    if array:
        print(array[0])
    else:
        print("The list is empty.")

def last_item_removed():
    items = item_list()
    items.pop()
    print()
    print("list after removing last item:", items)

first_item(item_list())
last_item_removed()


def family():
    members = ['Bryan', 'Krystle', 'Reagan', 'Blythe', 'Peter', 'Mimi', 'PJ', 'Gina']
    for member in members:
        print (member)
family()

def num_list():
    numbers = [1,2,3,6,22,98,45,23,22,12]
    evenarray = []
    for number in numbers:
        if number % 2 == 0:
            evenarray.append(number)
    print(evenarray)
num_list()


def grade():
    if score >= 90:
        print ('A')
    elif score >= 80:
        print ('B')
    elif score >= 70:
        print ('C')
    elif score >= 60:
        print ('D')
    else:
        print ('F')

score = 74
grade()

change_my_mind = True
def mind_check():
    global change_my_mind
    if change_my_mind == True:
         change_my_mind = False
    else:
        change_my_mind = True
    print(not change_my_mind)

mind_check()



def my_favorite_numbers():
    return [4,8,12,16,20,24]
def some_number(array):
    if len(array) < 7:
        print('There are not enough elements in this array')
    else:
        some_num = array[4]
        print(f'The 5th element is: {some_num}')
my_favorite_numbers()
some_number(my_favorite_numbers())


def is_div_by_3():
    for number in numbers_list:
        if number % 3 == 0:
            print(f"{number} is divisible by 3")
numbers_list = [1,2,3,4,5,6,7,8,9,10,11,12]
is_div_by_3()




def back_loop():
    for letter in reversed(letters):
        print (letter)
letters = ['A', 'B', 'C', 'D', 'E']
back_loop()


letter_grade = 'A'

match letter_grade:
    case "A":
        print("Excellent!")
    case "B":
        print("Good Job!")
    case "C":
        print("you Passed.")
    case "D":
        print("Try Harder.")
    case "F":
        print("failed.")
    case _:
        print("Invalid Grade.")


def fizz_buzz():
    for numb in array:
        if numb % 3 == 0 and numb % 5 == 0:
            print('DevMountain')
        elif numb % 5 == 0:
            print('Mountain')
        elif numb % 3 == 0:
            print('Dev')
        else:
            print(numb)
array = list(range(1, 101))
fizz_buzz()